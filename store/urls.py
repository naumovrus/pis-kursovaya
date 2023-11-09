from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cash', views.cash, name='cash'),
    path('realcash', views.realcash, name='realcash'),
    path('credit', views.credit, name='credit'),
    path('barter', views.barter, name='barter'),
    path('netting', views.netting, name='netting'),
    path('addProduct', views.addProduct, name='addproduct'),
    path('addclient', views.addclient, name='addclient'),
    path('CustomerBase', views.CustomerBase, name='CustomerBase'),
    path('MakeDeal', views.MakeDeal, name='MakeDeal'),
    path('ProductInfo', views.ProductInfo, name='ProductInfo'),
    path('checkclient', views.CheckCustomer, name='CheckCustomer'),
    path('delete/customer/<id>', views.del_customer, name='delete_customer'),
    path('delete/product/<id>', views.del_product, name='delete_product'),
]
