from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

# from ipware import get_client_ip
# from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.
@login_required
@login_required
def home(request):
    context = {
        "title": "Sistema Manajemnto Assets MDRHC",
    }
    return render(request, 'home/indexAdmin.html', context)

@login_required
def logout_view(request):
    logout(request)          
    request.session.flush() 
    return render(request, 'auth/logout.html') 


def error_404(request, exception):
        data = {}
        return render(request,'auth/404.html', data)

def error_500(request):
        data = {}
        return render(request,'auth/500.html', data)