from django.shortcuts import render, redirect
from .forms import Loginform, Rigesterform
from django.contrib.auth import authenticate, login, get_user_model
# from django.http import HttpResponse,Http404

def home_page(request):
    print(request.user.is_authenticated)
    context={
        'message' : 'welcome to home page'
    }
    return render(request, 'index.html',context)