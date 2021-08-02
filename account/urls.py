from django.urls import path
from .views import *

app_name='account'

urlpatterns = [
    path('', home_view,name='index'),
    path('menu/', create_menu,name='menu'),
    path('penjualan/', create_penjualan,name='penjualan'),
    path('<int:id>/detail/', penjualan_detail,name='detail'),
    path('<int:id>/<int:slug>/delete/', delete_detail,name='delete'),
    path('<int:id>/pelunasan', Pelunasan,name='pelunasan'),
    path('<int:id>/<int:jumlah_id>/pembayaran', Pembayaran,name='pembayaran'),
]
