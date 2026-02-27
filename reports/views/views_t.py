from django.shortcuts import render
from custom.models import Diresaun, Pozisaun, Kategoria, Sub_Kategoria, Marka, Tipu_Entrada, Supplier

# Create your views here.
def tabs(request):
	objects = Diresaun.objects.all()
	context = {
		'title': "Sumario Distribuisaun",
		'legend': "Sumario Distribuisaun",
		'objects':objects,
	}
	return render(request, 'Tabs/lstab.html', context)