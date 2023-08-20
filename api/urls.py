from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
from api.views import PlanetViewSet, SpecieViewSet, PersonViewSet, VehicleViewSet, StarshipViewSet, FilmViewSet
router = DefaultRouter()
router.register(r'planet', PlanetViewSet)
router.register(r'specie', SpecieViewSet)
router.register(r'person', PersonViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'starship', StarshipViewSet)
router.register(r'film', FilmViewSet)

urlpatterns = [
    path('reset_data/', views.reset_data, name="api-reset-data"),
    path('', include(router.urls)),
]

