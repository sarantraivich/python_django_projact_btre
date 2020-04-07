from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtor.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    data = {'listings': listings, 'bedroom_choices': bedroom_choices, 'price_choices': price_choices, 'state_choices': state_choices}
    return render(request, 'pages/index.html', data)


def about(request):
    #Get all realtor 
    realtors = Realtor.objects.all
    #Get MVP realtor 
    mvp_realtors = Realtor.objects.filter(is_mvp=True)[:1]
    data = {'realtors': realtors, 'mvp_realtors': mvp_realtors}
    return render(request, 'pages/about.html', data)
