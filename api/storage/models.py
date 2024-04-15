from django.db import models
from api.base.models import BaseModel
# Create your models here.
class Products(BaseModel):
    product_name = models.CharField(max_length=50)
    product_barcode = models.CharField(max_length=50)
  
    def __str__(self) :
        return str(self.product_name)
        
class Material(BaseModel):
    material_name = models.CharField(max_length=50)

    def __str__(self) :
        return str(self.material_name)
        
class Warehouse(BaseModel):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='material_rn1')
    number_material = models.FloatField()
    price = models.FloatField()

    def __str__(self) :
        return str(self.material_id)
        
class Product_Material(BaseModel):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_rn')
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='material_rn2')
    remainder = models.FloatField()

    def __str__(self) :
        return str(self.product_id)