from django.shortcuts import render
from mybeerapp.models import Beer
from django.views import generic
from mybeerapp.forms import BeerForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
def user_beerlist(request,username):
    try:
        beer_user = request.user
    except User.DoesNotExist:
        raise Http404
    else:
        user_beers = beer_user.beers.all()

    print(beer_user.username)
    print(user_beers)

    return render(request, 'mybeerapp/user_beerlist.html', {'beer_user':beer_user, 'user_beers':user_beers})

# def beerdetails(request):
#     return render(request, 'mybeerapp/beer_details.html')
