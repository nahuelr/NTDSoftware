from django.db import models
from django_mysql.models import ListCharField


class BaseModel(models.Model):
    graphid = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Planet(BaseModel):
    climates = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100)
    diameter = models.IntegerField(null=True, blank=True)
    gravity = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    orbitalPeriod = models.IntegerField(null=True, blank=True)
    population = models.CharField(max_length=100, null=True, blank=True)
    rotationPeriod = models.IntegerField(null=True, blank=True)
    surfaceWater = models.FloatField(null=True, blank=True)
    terrains = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100, null=True, blank=True)

    def __str__(self):
        return self.name


class Specie(BaseModel):
    averageHeight = models.FloatField(null=True, blank=True)
    averageLifespan = models.IntegerField(null=True, blank=True)
    classification = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    eyeColors = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100, null=True, blank=True)
    # filmConnection = models.CharField(max_length=100)
    hairColors = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100, null=True, blank=True)
    homeworld = models.ForeignKey(Planet, on_delete=models.DO_NOTHING, null=True, blank=True)  # check ondelete
    language = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # personConnection = models.CharField(max_length=100)
    skinColors = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100, null=True, blank=True)

    def __str__(self):
        return self.name


class Person(BaseModel):
    birthYear = models.CharField(max_length=10, null=True, blank=True)
    eyeColor = models.CharField(max_length=100, null=True, blank=True)
    # filmConnection = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, blank=True)
    hairColor = models.CharField(max_length=100, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    homeworld = models.ForeignKey(Planet, on_delete=models.DO_NOTHING, null=True, blank=True)  # check ondelete
    mass = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    skinColor = models.CharField(max_length=100, null=True, blank=True)
    species = models.ForeignKey(Specie, on_delete=models.DO_NOTHING, null=True, blank=True)  # check ondelete
    # starshipConnection = models.CharField(max_length=100)
    # vehicleConnection = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(BaseModel):
    cargoCapacity = models.FloatField(null=True, blank=True)
    consumables = models.CharField(max_length=100, null=True, blank=True)
    costInCredits = models.FloatField(null=True, blank=True)
    crew = models.IntegerField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    manufacturers = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100)
    maxAtmospheringSpeed = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    passengers = models.CharField(max_length=100, null=True, blank=True)
    pilotConnection = models.ManyToManyField(Person)
    vehicleClass = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Starship(BaseModel):
    MGLT = models.IntegerField(null=True, blank=True)
    cargoCapacity = models.FloatField(null=True, blank=True)
    consumables = models.CharField(max_length=100, null=True, blank=True)
    costInCredits = models.FloatField(null=True, blank=True)
    crew = models.CharField(max_length=20, null=True, blank=True)
    # filmConnection = models.CharField(max_length=100)
    hyperdriveRating = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    manufacturers = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100)
    maxAtmospheringSpeed = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    passengers = models.CharField(max_length=100, null=True, blank=True)
    pilotConnection = models.ManyToManyField(Person)
    starshipClass = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Film(BaseModel):
    characterConnection = models.ManyToManyField(Person)
    director = models.CharField(max_length=100, null=True, blank=True)
    episodeID = models.IntegerField(null=True)
    openingCrawl = models.TextField(null=True, blank=True)
    planetConnection = models.ManyToManyField(Planet)
    producers = ListCharField(base_field=models.CharField(max_length=100), max_length=10*100)
    releaseDate = models.DateField(null=True, blank=True)
    speciesConnection = models.ManyToManyField(Specie)
    starshipConnection = models.ManyToManyField(Starship)
    title = models.CharField(max_length=100, null=True, blank=True)
    vehicleConnection = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.title
