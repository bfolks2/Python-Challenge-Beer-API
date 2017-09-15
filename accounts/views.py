from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.forms import UserCreateForm

def signup(request):
    registered=False
    error=False
    if request.method=='POST':
        usercreateform=UserCreateForm(data=request.POST)
        if usercreateform.is_valid():
            user=usercreateform.save()
            user.set_password(user.password)
            user.save()
            registered=True
            # return HttpResponseRedirect(reverse('index'))
        else:
            error=True
            print(usercreateform.errors)
    else:
        usercreateform=UserCreateForm()

    context_dict={'usercreateform':usercreateform,'registered':registered, 'error':error}

    return render(request,'accounts/signup.html',context_dict)

class SignUp(CreateView):
    form_class=UserCreateForm
    success_url=reverse_lazy('accounts:user_login')
    template_name='accounts/signup.html'


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        username=username.replace('@','')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('User is not active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} Password: {}'.format(username,password))
            return render(request,'accounts/login.html',{'invalid':True})
    else:
        return render(request,'accounts/login.html',{'invalid':False})
