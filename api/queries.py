"""
This file contains the configuration for the GraphQL server and the queries to fetch the data from the SWAPI GraphQL
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Union

from django.db import models

from api.models import Planet, Specie, Person, Vehicle, Starship, Film


@dataclass
class GraphQLConfig:
    """
    Configuration for the GraphQL server
    """
    url: str = 'https://swapi-graphql.netlify.app/.netlify/functions/index'


class ReferenceFormat(Enum):
    """
    Reference path for the link
    SHORT: The id of the referenced model is stored in field->id path
    EXTENDED: The id of the referenced model is stored in field->edges->node->id path
    """
    SHORT = auto()
    EXTENDED = auto()


@dataclass
class Link:
    """
    Link to another model.

    model type(models.Model): The Referenced model
    reference_format ReferenceFormat: The format of the reference. Default: ReferenceFormat.SHORT
    """
    model: type(models.Model)
    reference_format: ReferenceFormat = ReferenceFormat.SHORT


planet_query: str = """
{
  allPlanets {
    edges {
      node {
        climates
        created
        diameter
        edited
        gravity
        id
        name
        orbitalPeriod
        population
        rotationPeriod
        surfaceWater
        terrains
      }
    }
  }
}
"""
specie_query: str = """
{
  allSpecies {
    edges {
      node {
        averageHeight
        averageLifespan
        classification
        created
        designation
        edited
        eyeColors
        hairColors
        id
        language
        name
        skinColors
        homeworld {
          id
        }
      }
    }
  }
}
"""

person_query: str = """
{
  allPeople {
    edges {
      node {
        birthYear
        created
        edited
        eyeColor
        gender
        hairColor
        height
        id
        mass
        name
        skinColor
        homeworld {
          id
        }
        species {
          id
        }
      }
    }
  }
}
"""

vehicle_query: str = """
{
  allVehicles {
    edges {
      node {
        cargoCapacity
        consumables
        costInCredits
        created
        crew
        edited
        id
        length
        manufacturers
        maxAtmospheringSpeed
        model
        name
        passengers
        vehicleClass
        pilotConnection {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
}
"""

starship_query: str = """
 {
  allStarships {
    edges {
      node {
        MGLT
        cargoCapacity
        consumables
        costInCredits
        created
        crew
        edited
        hyperdriveRating
        id
        length
        manufacturers
        maxAtmospheringSpeed
        model
        name
        passengers
        starshipClass
        pilotConnection {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
}
"""

film_query: str = """
{
  allFilms {
    edges {
      node {
        created
        director
        edited
        episodeID
        id
        openingCrawl
        producers
        releaseDate
        title
        planetConnection {
          edges {
            node {
              id
            }
          }
        }
        speciesConnection {
          edges {
            node {
              id
            }
          }
        }
        starshipConnection {
          edges {
            node {
              id
            }
          }
        }
        vehicleConnection {
          edges {
            node {
              id
            }
          }
        }
        characterConnection {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
}
"""

StarWarsModel = type(models.Model)
SchemaData = Dict[str, Union[str, Dict[str, Link]]]
SwapiData = Dict[StarWarsModel, SchemaData]
star_war_schema_data: SwapiData = {
    Planet: {'query': planet_query, 'field': 'allPlanets', 'links': {}},
    Specie: {'query': specie_query, 'field': 'allSpecies', 'links': {'homeworld': Link(Planet)}},
    Person: {
        'query': person_query,
        'field': 'allPeople',
        'links': {'homeworld': Link(Planet), 'species': Link(Specie)}
    },
    Vehicle: {
        'query': vehicle_query,
        'field': 'allVehicles',
        'links': {'pilotConnection': Link(Person, ReferenceFormat.EXTENDED)}
    },
    Starship: {
        'query': starship_query,
        'field': 'allStarships',
        'links': {'pilotConnection': Link(Person, ReferenceFormat.EXTENDED)}
    },
    Film: {
        'query': film_query,
        'field': 'allFilms',
        'links': {
            'characterConnection': Link(Person, ReferenceFormat.EXTENDED),
            'planetConnection': Link(Planet, ReferenceFormat.EXTENDED),
            'speciesConnection': Link(Specie, ReferenceFormat.EXTENDED),
            'starshipConnection': Link(Starship, ReferenceFormat.EXTENDED),
            'vehicleConnection': Link(Vehicle, ReferenceFormat.EXTENDED),
        },
    }
}
