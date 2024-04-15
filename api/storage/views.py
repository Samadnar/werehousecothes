from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Products, Product_Material, Warehouse
from rest_framework.response import Response
                        

class ProductView(APIView):
    def get(self, request):
        data_list = []
        dict_keys = list(request.data.keys())
        dict_values = list(request.data.values())
        for i in range(len(dict_keys)):
            
            if self.get_material(dict_keys[i], dict_values[i]) is False:
                continue
            data_list.append(self.get_material(dict_keys[i], dict_values[i]))
        base_data = self.check_warehouse(data_list, dict_keys, dict_values)
   
        data = {
            'result' : base_data
        }
        return Response(data)

    def get_material(self, product_id, number_of_product):
        product_material = Product_Material.objects.filter(product_id=product_id).values('material_id_id', 'remainder')
        if len(product_material) == 0:
            return False
        for i in product_material:
            i['remainder'] = float(number_of_product) * float(i['remainder'])
        return product_material

    def check_warehouse(self, data_list, dict_keys, dict_values):
        war_info = list(Warehouse.objects.all())
        base_data = []
        for i in range(len(data_list)):
            l=[]
            for j in range(len(data_list[i])):
                for k in range(len(war_info)):
                    if data_list[i][j]['material_id_id'] == war_info[k].material_id.id:    
                        if war_info[k].number_material == 0:
                            continue
                        number = float(data_list[i][j]['remainder']) - float(war_info[k].number_material)
                        if number > 0:
                            data = {
                                "warehouse_id" : war_info[k].id,
                                "material_name" : war_info[k].material_id.material_name,
                                "dict_keysty" : war_info[k].number_material,
                                "price" : war_info[k].price
                            }
                            war_info[k].number_material = 0
                            data_list[i][j]['remainder'] = number
                            
                        if number < 0:
                            data = {
                                "warehouse_id" : war_info[k].id,
                                "material_name" : war_info[k].material_id.material_name,
                                "qty" : data_list[i][j]['remainder'],
                                "price" : war_info[k].price
                            }
                            war_info[k].number_material = number * (-1)
                            
                        
                        l.append(data)
            
            
            new_data = {
                "product_name" : Products.objects.get(product_barcode=dict_keys[i]).product_name,
                "product_qty" : dict_values[i],
                "product_materials" : l
            }  
            base_data.append(new_data)
        return base_data
             