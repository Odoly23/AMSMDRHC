from django.db import models
import uuid
from django.contrib.auth.models import User
from custom.models import Diresaun, Pozisaun, Kategoria, Sub_Kategoria, Marka, Tipu_Entrada, Supplier

#Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)



class Assets(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200, null=True, verbose_name="Naran Sasan")
	serial = models.CharField(max_length=10, verbose_name="Serial Number")
	kat = models.ForeignKey(Sub_Kategoria, on_delete=models.CASCADE, null=True, verbose_name="Kategoria")
	mark = models.ForeignKey(Marka, on_delete=models.CASCADE, null=True, verbose_name="Marka/Merek")
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, verbose_name="Supplier")
	price = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Presu",null=True)
	total = models.IntegerField(blank=True, null=True,verbose_name="Total Tama")
	total_s = models.IntegerField(blank=True, null=True,verbose_name="Total")
	is_active = models.BooleanField(default=True, null=True)
	data_sosa = models.DateTimeField(null=True, blank=True, verbose_name="Data SOsa")
	data_prod = models.DateTimeField(null=True, blank=True, verbose_name="Data Produsaun")
	status = models.CharField(choices=[('Foun','Foun'),('Confirmed','Confirmed'),('Completed','Completed'),('maintenanced','maintenanced')], max_length=20, null=True, blank=True)
	kat = models.ForeignKey(Sub_Kategoria, on_delete=models.CASCADE, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="assetscreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="assetsupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="assetsdeletedbys")
	deleted_at = models.DateTimeField(null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	
	def __str__(self):
		template = '{0.name}'
		return template.format(self)
	
	def soft_delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()
	
	def undelete(self):
		self.deleted_at = None
		self.deleted_by = None
		self.save()
	
	def hard_delete(self):
		super().delete()
		
	objects = models.Manager()  # The default manager
	active_objects = ActiveManager()

	class Meta:
		verbose_name_plural='09-Dadus_Assets'