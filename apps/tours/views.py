from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tours.models import Country, Destination, Tour
from apps.tours.serializers import TourSerializer


def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'tours/destinations.html', {'destinations': destinations})


def countries(request):
    countries = Country.objects.all()
    return render(request, 'tours/countries.html', {'countries': countries})

def country_view(request, pk):
    country = Country.objects.get(id=pk)
    destinations = country.destination_set.all()

    return render(request, 'tours/tours.html', {'country': country, 'destinations': destinations})

def single_list(request,pk):
    tur = Tour.objects.get(id=pk)
    return render(request, 'tours/single-listing.html', {'tur': tur})


@api_view(['GET'])
def tours(request, pk):
    
    destination = Destination.objects.get(id=pk)
    tours = destination.tours.all()
    data = TourSerializer(tours, many=True).data

    return Response({'tours': data})
