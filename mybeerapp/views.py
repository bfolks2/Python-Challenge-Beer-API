from django.shortcuts import render
from mybeerapp.models import Beer
from django.views import generic

from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')



class BeerList(generic.ListView):
    model = Beer
    template_name='mybeerapp/beer_list.html'
    context_object_name='beers'

def beerlist(request):
    beers = Beer.objects.all().order_by('name')
    return render(request, 'mybeerapp/beer_list.html', {'beers':beers})



def beerdetails(request):
    return render(request, 'mybeerapp/beer_details.html')
