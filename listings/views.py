from django.shortcuts import get_object_or_404, render
from .models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    data = {'listings': listings}
    return render(request, 'listings/listings.html', data)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    data = {'listing': listing}
    return render(request, 'listings/listing.html', data)

def search(request):
    listings = Listing.objects.order_by('-list_date').order_by('-list_date').filter(is_published=True)
    
    #keyword
    if 'keywords' in request.POST:
        keywords = request.POST['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    #city
    if 'city' in request.POST:
        city = request.POST['city']
        if city:
            listings = listings.filter(city__iexact=city)
    
    #state
    if 'state' in request.POST:
        state = request.POST['state']
        if state:
            listings = listings.filter(state__iexact=state)

    #bedrooms
    if 'bedrooms' in request.POST:
        bedrooms = request.POST['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.POST:
        price = request.POST['price']
        if price:
            listings = listings.filter(price__lte=price)

    data = {'listings': listings, 'bedroom_choices': bedroom_choices, 'price_choices': price_choices, 'state_choices': state_choices, 'values': request.POST}
    return render(request, 'listings/search.html', data)