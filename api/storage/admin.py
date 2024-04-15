from django.contrib import admin
from .models import Material, Product_Material, Products, Warehouse
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_name']   
    
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_material']    
   
   
class Product_MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'remainder'] 
         
admin.site.register(Products, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Product_Material, Product_MaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
