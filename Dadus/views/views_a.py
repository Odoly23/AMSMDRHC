import csv, io, datetime
from django.shortcuts import render, get_object_or_404
from main.utils import getjustnewid
from django.contrib.auth.decorators import login_required
from custom.models import Pozisaun, Diresaun, Kategoria, Sub_Kategoria,\
						  Supplier, Rak, Marka

# Create your views here.
@login_required
def dash(request):
	user = request.user
	object1, object2, object3 = [],[],[]
	objects = Diresaun.objects.all()
	context = {
		'link_antes': [{'link_name':"d-dash",'link_text':"Dados Distribuisaun"}],
		'title': 'Sumario Distribuisaun Assets',
		'legend': 'Sumario Distribuisaun Assets',
		'dashActive':"active",
	}
	return render(request, 'Dash/index.html', context)