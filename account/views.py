from account.models import Menu
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import MenuForm, PenjualanDetailForm,PenjualanForm
from .models import Menu,Penjualan, PenjualanDetail
from django.db.models import Sum

# Create your views here.


def home_view(request):
    daftar_menu = Menu.objects.all()
    daftar_penjualan = Penjualan.objects.all().order_by('lunas')
    return render(request, 'account/index.html', {'daftar_menu':daftar_menu,'daftar_penjualan':daftar_penjualan})


def create_menu(request):

    new_form = None
    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect("account:index")
    else:
        form = MenuForm()
    return render(request, 'account/add_menu.html', {'form_menu': form})

def create_penjualan(request):

    new_form = None
    if request.method == 'POST':
        form = PenjualanForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect("account:index")
    else:
        form = PenjualanForm()
    return render(request, 'account/add_penjualan.html', {'form_penjualan': form})

def penjualan_detail(request,id):
    datas = PenjualanDetail.objects.filter(penjualan=id)
    menus = Menu.objects.all()
    pembeli = Penjualan.objects.get(pk=id)
    total = 0
    for data in datas:
        x = Menu.objects.get(id=data.menu_id)
        total += x.harga
    new_form = None
    if request.method == 'POST':
        form = PenjualanDetailForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.penjualan = pembeli
            new_form.save()
            return redirect("account:detail",id)
    else:
        form = PenjualanDetailForm()
    return render(request,'account/add_penjualan_detail.html', {'datas':datas, 'menus':menus, 'total':total, 'pembeli':pembeli, 'form':form})

def delete_detail(request, id,slug):
    obj = PenjualanDetail.objects.get(pk=id)
    print(obj.pk)
    if request.method == "POST":
        obj.delete()
        return redirect("account:detail",slug)
    return render(request, "account/add_penjualan_detail.html")

def Pelunasan(request, id):
    datas = Penjualan.objects.get(pk=id)
    print(datas)
    obj = PenjualanDetail.objects.filter(penjualan=id)
    jumlah = 0
    for data in obj:
          x = Menu.objects.get(id=data.menu_id)
          jumlah += x.harga
    return render(request, 'account/pelunasan.html', {'datas':datas,'jumlah':jumlah})

def Pembayaran(request,id,jumlah_id):
    obj = get_object_or_404(Penjualan, pk=id)
    obj.total += jumlah_id
    obj.lunas += 1
    obj.save()
    return redirect("account:index")
