from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.contrib.auth.forms import UserCreationForm

from .filters import ContentFilter

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth

from .models import Content
from django.contrib import messages

from .forms import CreateUserForm




# Create your views here.
def index(request):
    content = Content.objects.all()
    myFilter = ContentFilter(request.GET, queryset=content)
    content = myFilter.qs        

    context= {'content':content, 'myfilter':myFilter}


    return render(request, 'index.html', context)

def register(request):
    form = CreateUserForm
    if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)

                    return redirect('login')

                else:
                    return render(request, 'register.html', {'form':form})

        
       
    else:
        form = CreateUserForm()
        return render(request, 'register.html', {'form':form})    


def login1(request):
    if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')
   

def about(request):
    return render(request, 'aboutus.html')    


def info(request, pk):
    content = Content.objects.filter(id=pk)
            

    context= {'content':content}


    return render(request, 'info.html', context) 
