from django.conf.urls import url
from mybeerapp import views

app_name='mybeerapp'

urlpatterns = [
    url(r'^new/$', views.createbeer, name='create'),
    url(r'^rate/$', views.createrating, name='rating'),
    url(r'^by/(?P<username>[-\w]+)/$', views.user_beerlist, name='user_beerlist'),
    url(r'^details/(?P<slug>[-\w]+)/$', views.beer_details, name='beer_details'),
    url(r'^ratedetails/(?P<slug>[-\w]+)/$', views.rating_details, name='rating_details'),
]
