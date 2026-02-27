from django.db import models

# Create your models here.
# class AssetDistribution(models.Model):
#     asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
#     department = models.ForeignKey("Department", on_delete=models.PROTECT)
#     distributed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     distributed_at = models.DateTimeField(auto_now_add=True)
#     note = models.TextField(blank=True)
# 	hashed = models.CharField(max_length=32, null=True, blank=True)
	
# 	def __str__(self):
# 		template = '{0.name}'
# 		return template.format(self)
	
# 	def soft_delete(self, user):
# 		self.deleted_at = str(timezone.now())
# 		self.deleted_by = user
# 		self.save()
	
# 	def undelete(self):
# 		self.deleted_at = None
# 		self.deleted_by = None
# 		self.save()
	
# 	def hard_delete(self):
# 		super().delete()
		
# 	objects = models.Manager()  
# 	active_objects = ActiveManager()

# 	class Meta:
# 		verbose_name_plural='09-Dadus_Distribuisaun'


# class AssetTransfer(models.Model):
#     asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
#     from_department = models.ForeignKey("Department", on_delete=models.PROTECT, related_name="transfer_from")
#     to_department = models.ForeignKey("Department", on_delete=models.PROTECT, related_name="transfer_to")
#     transferred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     transferred_at = models.DateTimeField(auto_now_add=True)
#     note = models.TextField(blank=True)