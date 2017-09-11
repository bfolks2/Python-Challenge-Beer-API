from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

app_name='accounts'

urlpatterns=[
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout,name='user_logout'),
]

# urlpatterns = [
#     url(r'^login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='user_login'),
#     url(r'^logout/$', auth_views.LogoutView.as_view(), name='user_logout'), #Default template built in
#     url(r'^signup/$', views.SignUp.as_view(), name='signup'),
# ]
