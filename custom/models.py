from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

 
class Diresaun(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="diresauncreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="diresaunupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="diresaundeletedbys")
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
		verbose_name_plural='01-Dadus_Custom_Diresaun'
	
class Pozisaun(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="pozisauncreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="pozisaunupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="pozisaundeletedbys")
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
		verbose_name_plural='02-Dadus_Custom_Pozisaun'

class Kategoria(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="kategoriacreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="kategoriaupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="kategoriadeletedbys")
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
		verbose_name_plural='03-Dadus_Custom_Kategoria'


class Sub_Kategoria(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	kat = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="subkatcreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="subkatupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="subkatdeletedbys")
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
		verbose_name_plural='04-Dadus_Custom_Sub_Kategoria'


class Marka(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="markacreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="markaupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="markadeletedbys")
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
		verbose_name_plural='05-Dadus_Custom_marka'


class Tipu_Entrada(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tpentradacreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tpentradaupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tpentradadeletedbys")
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
		verbose_name_plural='06-Dadus_Custom_tipo_entrada'


class Rak(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="rakcreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="rakupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="rakdeletedbys")
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
		verbose_name_plural='07-Dadus_Custom_Rak'

class Supplier(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="suppliercreatedbys")
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="supplierupdatetedbys")
	updated_at = models.DateTimeField( null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="supplierdeletedbys")
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
		verbose_name_plural='08-Dadus_Custom_Supplier'