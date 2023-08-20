"""
Class to fetch data from graphql and store in db
"""

import json
from typing import Dict, List, Tuple, Optional

import requests
from django.db import transaction
from requests import Response

from api.queries import GraphQLConfig, ReferenceFormat, StarWarsModel, Link, SwapiData


class ScraperData:
    """ Fetch data from graphql and store in db"""

    def __init__(self, target_data):
        self.target_data: SwapiData = target_data

    def reset_data(self) -> None:
        """ Clear all data and re-scrap data from apollo server"""
        for model in self.target_data:  # Delete all data
            model.objects.all().delete()

        for model, data in self.target_data.items():  # Fetch data from graphql and store in db
            self.populate_model(model, data['query'], data['field'])

    def populate_model(self, model: StarWarsModel, query: str, field: str) -> None:
        """
        Fetch data from graphql and store in db

        :param model: Model to store data in
        :type model: StarWarsModel
        :param query: Query to fetch data from graphql
        :type query: str
        :param field: field name in the response object where the data is stored
        :type field: str
        """
        response: Response = requests.post(url=GraphQLConfig.url, json={"query": query})
        if response.status_code != 200:
            raise Exception(f"Error fetching rows for: {model.__name__}")
        raw_data: Dict = json.loads(response.content)
        data: List[Dict] = [p["node"] for p in raw_data['data'][field]['edges']]
        for d in data:  # Store graphql id for future references
            d['graphid'] = d.pop('id')
        instances, late_bindings = self.get_instances(model, data, self.target_data[model]['links'])
        ins_created: List[StarWarsModel] = model.objects.bulk_create(instances)

        with transaction.atomic():  # Update all instances in one transaction
            for ins in ins_created:  # Bind related objects
                late_binding: Dict = late_bindings.get(ins.graphid, {})
                for field, objs in late_binding.items():
                    getattr(ins, field).set(objs)
                ins.save()

    def get_instances(
        self,
        base_model: StarWarsModel,
        rows: List[Dict],
        links: Dict[str, Link]
    ) -> Tuple[List[StarWarsModel], Dict]:
        """
        Get instances from rows and bind related objects
        :param base_model: Model used to create instances
        :type base_model: StarWarsModel
        :param rows: Data to create instances
        :type rows: List[Dict]
        :param links: Links to other models data
        :type links:  Dict[str, Link]
        :return: Instances and related objects to bind later
        :rtype: Tuple[List[StarWarsModel], Dict]
        """
        late_binding = {}
        for field, link in links.items():
            ids: List[str] = self._get_ids(rows, field, link)
            related_instances: StarWarsModel = link.model.objects.filter(graphid__in=ids)
            # create id mapping to make search faster
            id_mapping: Dict[str, StarWarsModel] = {i.graphid: i for i in related_instances}

            for instance_data in rows:  # replace graphql id with db instance
                if link.reference_format == ReferenceFormat.SHORT:
                    graph_ref: Optional[Dict[str, str]] = instance_data.get(field)
                    if graph_ref is None:
                        continue
                    instance_data[field] = id_mapping.get(graph_ref.get('id'))
                elif link.reference_format == ReferenceFormat.EXTENDED:
                    edges: Dict = instance_data.get(field).get('edges')
                    referenced_objs: List[str] = [id_mapping.get(obj.get('node').get('id')) for obj in edges]
                    if instance_data['graphid'] not in late_binding:
                        late_binding[instance_data['graphid']] = {}
                    late_binding[instance_data['graphid']][field] = referenced_objs  # store for later binding
                    instance_data.pop(field)
        # instances.append(base_model(**instance_data))
        return [base_model(**instance_data) for instance_data in rows], late_binding

    @staticmethod
    def _get_ids(rows: List[Dict], field: str, link: Link) -> List[str]:
        """
        Get all non-duplicate ids from rows
        :param rows: Rows to get ids from
        :type rows: List[Dict]
        :param field: Field name in the response object where the ids are stored
        :type field: str
        :param link: Data about the link to the other model
        :type link: Link
        :return: All non-duplicate ids from rows
        :rtype: List[str]
        """
        result = set()
        if link.reference_format == ReferenceFormat.SHORT:
            result.update([r.get(field).get('id') for r in rows if r.get(field) is not None])
        elif link.reference_format == ReferenceFormat.EXTENDED:
            for r in rows:
                edges = r.get(field).get('edges')
                for obj in edges:
                    result.add(obj.get('node').get('id'))
        return list(result)
