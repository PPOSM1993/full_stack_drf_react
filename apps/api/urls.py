from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country', views.CountryViewSet, basename='country'),
router.register('league', views.LeagueViewSet, basename='league'),
router.register('characteristic', views.CharacteristicViewSet, basename='characteristic'),
router.register('football_club', views.FootballClubViewSet, basename='football_club')

urlpatterns = router.urls