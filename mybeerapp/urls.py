from django.conf.urls import url
from mybeerapp import views

app_name='mybeerapp'

urlpatterns = [
    url(r'^new/$', views.createbeer, name='create'),
    url(r'^rate/$', views.createrating, name='rating'),
    url(r'^by/(?P<username>[-\w]+)/$', views.user_beerlist, name='user_beerlist'),
    url(r'^by/$', views.user_search, name='user_search'),
    url(r'^details/(?P<slug>[-\w]+)/$', views.beer_details, name='beer_details'),
    url(r'^details/(?P<slug>[-\w]+)/edit/$', views.BeerUpdateView.as_view(), name='beer_edit'),
    url(r'^details/(?P<slug>[-\w]+)/delete/$', views.BeerDeleteView.as_view(), name='beer_delete'),
    url(r'^ratedetails/(?P<slug>[-\w]+)/$', views.rating_details, name='rating_details'),
    url(r'^rating/(?P<pk>\d+)/edit/$', views.RatingUpdateView.as_view(), name='rating_edit'),
    url(r'^rating/(?P<pk>\d+)/delete/$', views.RatingDeleteView.as_view(), name='rating_delete'),
]
