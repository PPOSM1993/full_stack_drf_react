from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country', views.CountryView, basename='country'),
router.register('league', views.LeagueView, basename='league'),
router.register('characteristic', views.CharacteristicView, basename='characteristic'),
router.register('football_club', views.FootballClubView, basename='football_club')

urlpatterns = router.urls