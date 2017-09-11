from django.conf.urls import url
from mybeerapp import views

app_name='mybeerapp'

urlpatterns = [
    url(r'^new/$', views.createbeer, name='create'),
    url(r'^by/(?P<username>[-\w]+)/$', views.user_beerlist, name='user_beerlist'),
    # url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='beer_details'),
]