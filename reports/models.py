from django.db import models

# Create your models here.
# class AssetDisposal(models.Model):

#     class DisposalType(models.TextChoices):
#         DAMAGED = "damaged", "Damaged"
#         LOST = "lost", "Lost"
#         SOLD = "sold", "Sold"

#     asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
#     disposal_type = models.CharField(max_length=20, choices=DisposalType.choices)
#     disposal_date = models.DateField()
#     note = models.TextField(blank=True)


# class AssetDepreciation(models.Model):
#     asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
#     year = models.IntegerField()
#     depreciation_amount = models.DecimalField(max_digits=15, decimal_places=2)
#     book_value = models.DecimalField(max_digits=15, decimal_places=2)
#     calculated_at = models.DateTimeField(auto_now_add=True)