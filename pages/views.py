from django.shortcuts import render
from .models import *
from cars.models import Car
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars=Car.objects.order_by('-created_date')
    #The values() method returns a QuerySet containing dictionaries:
    #<QuerySet [{'comment_id': 1}, {'comment_id': 2}]>
    # search_fields=Car.objects.values('model','city','year','body_style')
    #he values_list() method returns a QuerySet containing tuples:
    #<QuerySet [(1,), (2,)]>
    #If you are using values_list() with a single field,
    # you can use flat=True to return a QuerySet of single values instead of 1-tuples:
    #<QuerySet [1, 2]>

    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'teams':teams,
        'featured_cars':featured_cars,
        'latest_cars':latest_cars,
        # 'search_fields':search_fields,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    teams=Team.objects.all()
    data={
        'teams':teams
    }
    return render(request,'pages/services.html',data)

def contact(request):
    return render(request,'pages/contact.html')

