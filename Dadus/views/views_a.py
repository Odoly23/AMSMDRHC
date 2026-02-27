import csv, io, datetime
from django.shortcuts import render, get_object_or_404
from main.utils import getjustnewid
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dash(request):
	context = {
		'title': 'Sumario Distribuisaun Assets',
		'legend': 'Sumario Distribuisaun Assets'
	}
	return render(request, 'Dash/index.html', context)