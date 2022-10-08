from django.contrib import admin
from .models import Category,Customer,Product,Order

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):

    list_display= ['name','email','phone','adress']
    search_fields = ['name','adress']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category_id','product_quantity']
    search_fields = ['product_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id','product_id','delivery']
    search_fields = ['delivery']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)

