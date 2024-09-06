from django.db import models
from .validators import *
# Create your models here.


class ItemInfo(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255, validators=[validate_item_name])
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='item_images')
    item_resume=models.FileField(upload_to="file",validators=[validate_file])