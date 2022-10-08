from django.urls import path

from . import views
from shop.models import*
from .views import catList, cus_List


urlpatterns = [
    path('categories/',views.categorylistapi),
    path('customers/',views.customerlistapi),
    path('products/',views.productlistapi),
    path('', catList.as_view(),name='country-list'),
    path('customerList/',views.cus_List.as_view(), name='customer-list'),
    path('OrderList/',views.OrderList.as_view(), name='Order-list'),
]
