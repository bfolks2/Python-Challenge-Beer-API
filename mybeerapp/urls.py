from django.conf.urls import url
from mybeerapp import views

app_name='mybeerapp'

urlpatterns = [
    url(r'^$',views.beerlist, name='beer_list'),
]
