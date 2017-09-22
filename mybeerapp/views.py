from django.shortcuts import render, get_object_or_404
from mybeerapp.models import Beer, Rating
from mybeerapp.forms import BeerForm, RatingForm
from mybeerapp.serializers import BeerSerializer, RatingSerializer
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.functions import Lower

from django.http import HttpResponse
from rest_framework.response import Response
from django.template.loader import render_to_string

from django.http import HttpResponseRedirect
from django.utils import timezone

from django.views.generic import (ListView, UpdateView, DeleteView)
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    beers=Beer.objects.all().order_by('name')
    return render(request, 'index.html', {'beers':beers})


class BeerAPIView(APIView):
    def get(self,request):
        beers = Beer.objects.all().order_by('name')
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)

class RatingAPIView(APIView):
    def get(self,request):
        ratings = Rating.objects.all().order_by('beer')
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class BeerList(ListView):
    model = Beer
    template_name='mybeerapp/beer_list.html'
    context_object_name='beers'

@login_required
def createbeer(request):

    yesterday = timezone.now() - timezone.timedelta(days=1)
    dayflag=False
    nameflag=False

    beerform=BeerForm()

    if Beer.objects.filter(user=request.user, created_at__gt=yesterday).exists():
        dayflag=True
        return render (request,'mybeerapp/createbeer.html',{'form':beerform,'dayflag':dayflag})

    if request.method=='POST':
        beerform=BeerForm(request.POST)
        print(beerform.errors)
        if beerform.is_valid():
            beer=beerform.save(commit=False)
            for beerobj in Beer.objects.all():
                if beerobj.slug_name == slugify(beer.name):
                    nameflag=True
                    return render (request,'mybeerapp/createbeer.html',{'form':beerform,'nameflag':nameflag,'beer':beer})
            beer.user=request.user
            beer.save()
            return render(request, 'mybeerapp/beerdetails.html',{'beer':beer})

    return render (request,'mybeerapp/createbeer.html',{'form':beerform,'dayflag':dayflag})


class BeerUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mybeerapp/beerdetails.html'

    template_name = 'mybeerapp/createbeer.html'

    model = Beer
    fields=['calories','abv','style','location','glass']

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['update']='update'
        return context

class BeerDeleteView(LoginRequiredMixin,DeleteView):
    model=Beer
    template_name= 'mybeerapp/beer_confirm_delete.html'
    context_object_name='beerdelete'

    def get_success_url(self):
        current_user = self.object.user
        return reverse_lazy( 'mybeerapp:user_beerlist', kwargs={'username': current_user.username})


@login_required
def createrating(request, slug=''):

    beerflag=False

    if request.method=='POST':
        ratingform=RatingForm(request.POST)
        if ratingform.is_valid():
            rating=ratingform.save(commit=False)
            if Rating.objects.filter(user=request.user, beer=rating.beer).exists():
                beerflag=True
                return render (request,'mybeerapp/createrating.html',{'form':ratingform,'beerflag':beerflag, 'ratingbeer':rating.beer})
            rating.user=request.user
            rating.save()
            return render(request, 'mybeerapp/ratingdetails.html',{'beer':rating.beer})
    else:
        if slug=='':
            ratingform=RatingForm()
        else:
            beerslug=get_object_or_404(Beer, slug=slug)
            ratingform=RatingForm(initial={'beer': beerslug})

    return render (request,'mybeerapp/createrating.html',{'form':ratingform,'beerflag':beerflag})


class RatingUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mybeerapp/ratingdetails.html'

    template_name = 'mybeerapp/createrating.html'

    model = Rating
    fields=['aroma','appearance','taste']
    context_object_name='ratingupdate'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['rateupdate']='rateupdate'
        return context

class RatingDeleteView(LoginRequiredMixin,DeleteView):
    model=Rating
    template_name= 'mybeerapp/rating_confirm_delete.html'
    context_object_name='ratingdelete'

    def get_success_url(self):
        current_user = self.object.user
        return reverse_lazy( 'mybeerapp:user_beerlist', kwargs={'username': current_user.username})


def user_beerlist(request,username):
    try:
        beer_user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        raise Http404
    else:
        user_beers = beer_user.beers.all()
        user_ratings = beer_user.user_ratings.all()

    return render(request, 'mybeerapp/user_beerlist.html', {'beer_user':beer_user, 'user_beers':user_beers, 'user_ratings':user_ratings})

def user_search(request):
    notuser=False
    if request.method == 'POST':
        username=request.POST.get('usersearch')
        username=username.replace('@','')
        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect(reverse('mybeerapp:user_beerlist', kwargs={'username':username}))
        else:
            notuser=True
            users=User.objects.all().order_by(Lower('username'))
            return render (request,'mybeerapp/siteuserlist.html', {'users':users,'username':username})

def beer_details(request, slug):
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'mybeerapp/beerdetails.html',{'beer':beer})

def rating_details(request, slug):
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'mybeerapp/ratingdetails.html',{'beer':beer})


# def beerdetails(request):
#     return render(request, 'mybeerapp/beer_details.html')
