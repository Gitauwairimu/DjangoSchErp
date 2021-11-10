from django.urls import path
from . import views


urlpatterns = [
    path('', views.payment, name='payment'),
    path('paylist/', views.paylist, name='paylist'),
    path('paylist/<int:id>/', views.payaccount, name='personalpay'),
    path('paylist/<int:id>/', views.lastpay, name='lastpay'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
    path('addexpense/', views.addexpense, name='addexpense'),
    path('addaccount/', views.addaccount, name='addaccount'),
]
