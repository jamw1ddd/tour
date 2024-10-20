from django.urls import path

from apps.tours.views import destinations, countries, country_view, tours,single_list

urlpatterns = [
    path('<int:pk>/', tours, name='tours'),
    path('destinations/', destinations, name='destinations'),
    path('countries/', countries, name='countries'),
    path('country/<int:pk>/', country_view, name='country'),
    path('tour-detail/<int:pk>/', single_list, name='singlelist'),
]