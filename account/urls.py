from django.conf import settings
from django.conf.urls.static import static
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
    path('register/', register_request , name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name= 'logout'),
    path('barang/', create_barang, name= 'barang'),
    path('pengeluaran/', create_pengeluaran, name= 'pengeluaran'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)