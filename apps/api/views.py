from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.response import Response

# Create your views here.

class CountryViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=204)

class LeagueViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    
    def list(self, request):
        queryset = League.objects.all()
        serializer = LeagueSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        queryset = League.objects.all()
        league = get_object_or_404(queryset, pk=pk)
        serializer = LeagueSerializer(league)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        league = League.objects.get(pk=pk)
        serializer = LeagueSerializer(league, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        league = League.objects.get(pk=pk)
        league.delete()
        return Response(status=204)
    
class CharacteristicViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    
    def list(self, request):
        queryset = Characteristic.objects.all()
        serializer = CharacteristicSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CharacteristicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        queryset = Characteristic.objects.all()
        characteristic = get_object_or_404(queryset, pk=pk)
        serializer = CharacteristicSerializer(characteristic)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        characteristic = Characteristic.objects.get(pk=pk)
        serializer = CharacteristicSerializer(characteristic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        characteristic = Characteristic.objects.get(pk=pk)
        characteristic.delete()
        return Response(status=204)

class FootballClubViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = FootballClub.objects.all()
    serializer_class = FootballClubSerializer
    
    def list(self, request):
        queryset = FootballClub.objects.all()
        serializer = FootballClubSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FootballClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        #return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        queryset = FootballClub.objects.all()
        football_club = get_object_or_404(queryset, pk=pk)
        serializer = FootballClubSerializer(football_club)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        football_club = FootballClub.objects.get(pk=pk)
        serializer = FootballClubSerializer(football_club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        football_club = FootballClub.objects.get(pk=pk)
        football_club.delete()
        return Response(status=204)

