import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.contrib import messages



@login_required
def ListaUtilizadores(request):
	objects = User.objects.all()#.exclude(is_staff=True)
	print('objects:',objects)
	context = {
		'userlist_active':"active",
		'objects': objects, 
		'title': 'Lista Utilizador', 'legend': 'Lista Utilizador',
	}
	return render(request,'users/userlist.html',context)