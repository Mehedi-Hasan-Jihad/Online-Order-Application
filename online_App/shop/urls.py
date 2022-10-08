from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('about/',views.about,name='about'),
    path('order/',views.order,name='order'),
    path('order_list/',views.order_list,name='order_list'),
    path('reg/', views.user_registration, name='reg'),
    path('show_category/<str:pk>',views.show_category,name='show_category'),
    path("order_details/<str:pk>", views.show_order, name='order_details'),
    path("update_order/<str:pk>", views.update_order, name='update_order'),
    path("delete_order/<str:pk>",views.delete_order,name='delete_order'),
    path('sign_in/',views.sign_in,name='sign_in'),


]
