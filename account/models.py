from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
# Create your models here.
x = 0
class Penjualan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='penjualans')
    pembeli = models.CharField(max_length=255)
    lunas = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'penjualan'

    def __str__(self):
        return self.pembeli

    def get_harga(self):
        obj = PenjualanDetail.objects.filter(penjualan=self)
        jumlah = 0
        x = globals
        for data in obj:
            x = Menu.objects.get(id=data.menu_id)
            jumlah += x.harga
        return jumlah
        
class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pakets')
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=1000)
    harga = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'menu'
    
    def __str__(self):
        ret = self.nama + ' - ' + self.deskripsi
        return ret


class PenjualanDetail(models.Model):
    penjualan = models.ForeignKey(Penjualan, on_delete=models.CASCADE, related_name='penjualandetails')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='penjualandetails')
    qty = models.IntegerField(default=1,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'penjualandetail'
'''
    def __str__(self):
        return self.qty
'''
    