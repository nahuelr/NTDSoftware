from django.shortcuts import redirect
from rest_framework import viewsets

from api.models import Planet, Specie, Person, Vehicle, Starship, Film
from api.queries import star_war_schema_data
from api.scraper import ScraperData
from api.serializers import (
    PlanetSerializer, SpecieSerializer, PersonSerializer, VehicleSerializer, StarshipSerializer, FilmSerializer
)


def reset_data(_request):
    """
    Clear all data and re-scrap data from SWAPI

    :param _request: Not used, but required by Django
    :type _request: django.http.HttpRequest
    :return: Redirect to admin:index
    :rtype: django.http.HttpResponseRedirect
    """
    scrap_data = ScraperData(target_data=star_war_schema_data)
    scrap_data.reset_data()
    return redirect('admin:index')


class PlanetViewSet(viewsets.ModelViewSet):
    """ CRUD for Planet"""
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    """ CRUD for Specie """
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """ CRUD for Person """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """ CRUD for Vehicle """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class StarshipViewSet(viewsets.ModelViewSet):
    """ CRUD for Starship """
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class FilmViewSet(viewsets.ModelViewSet):
    """ CRUD for Film """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
