from django.shortcuts import render, get_object_or_404
from mybeerapp.models import Beer
from django.views import generic
from mybeerapp.forms import BeerForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.template.loader import render_to_string

from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    beers=Beer.objects.all().order_by('-name')
    return render(request, 'index.html', {'beers':beers})


class BeerList(generic.ListView):
    model = Beer
    template_name='mybeerapp/beer_list.html'
    context_object_name='beers'

@login_required
def createbeer(request):

    if request.method=='POST':
        beerform=BeerForm(request.POST)
        if beerform.is_valid():
            beer=beerform.save(commit=False)
            beer.user=request.user
            beer.save()
            # return HttpResponseRedirect(reverse('mybeerapp:beer_details', kwargs={'username':self.user.username, 'pk':self.pk}))
            # return HttpResponseRedirect(reverse('mybeerapp:beer_list', kwargs={'username':self.user.username}))
            return HttpResponseRedirect(reverse('index'))
    else:
        beerform=BeerForm()

    return render (request,'mybeerapp/createbeer.html',{'beerform':beerform})


@login_required
def createrating(request):
    if request.method=='POST':
        ratingform=RatingForm(request.POST)
        if ratingform.is_valid():
            rating=ratingform.save(commit=False)
            rating.user=request.user
            rating.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        ratingform=RatingForm()

    return render(request, 'mybeerapp/createrating.html',{'ratingform':ratingform})


@login_required
def user_beerlist(request,username):
    try:
        beer_user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        raise Http404
    else:
        user_beers = beer_user.beers.all()
        user_ratings = beer_user.user_ratings.all()

    return render(request, 'mybeerapp/user_beerlist.html', {'beer_user':beer_user, 'user_beers':user_beers, 'user_ratings':user_ratings})

def beer_details(request, slug):
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'mybeerapp/beerdetails.html',{'beer':beer})

def rating_details(request, slug):
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'mybeerapp/ratingdetails.html',{'beer':beer})


# def beerdetails(request):
#     return render(request, 'mybeerapp/beer_details.html')
