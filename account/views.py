from django.shortcuts import render, redirect, get_object_or_404
from .forms import MenuForm, PenjualanDetailForm,PenjualanForm
from .models import Menu,Penjualan, PenjualanDetail
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm



# Create your views here.
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("account:login")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as {username}.")
				return redirect("account:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("account:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html",context={"register_form":form})

@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def home_view(request):
    daftar_menu = Menu.objects.all()
    daftar_penjualan = Penjualan.objects.all().order_by('lunas')
    return render(request, 'account/index.html', {'daftar_menu':daftar_menu,'daftar_penjualan':daftar_penjualan})

@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def create_menu(request):
    new_form = None
    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Add new menu success.")
            return redirect("account:index")
    else:
        form = MenuForm()
    return render(request, 'account/add_menu.html', {'form_menu': form,})
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def create_penjualan(request):
    new_form = None
    if request.method == 'POST':
        form = PenjualanForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Add order success.")
            return redirect("account:index")
    else:
        form = PenjualanForm()
    return render(request, 'account/add_penjualan.html', {'form_penjualan': form,})
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
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
            messages.success(request, "Add item success.")
            return redirect("account:detail",id)
    else:
        form = PenjualanDetailForm()
    return render(request,'account/add_penjualan_detail.html', {'datas':datas, 'menus':menus, 'total':total, 'pembeli':pembeli, 'form':form})
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def delete_detail(request, id,slug):
    obj = PenjualanDetail.objects.get(pk=id)
    print(obj.pk)
    if request.method == "POST":
        obj.delete()
        messages.warning(request, "Delete success.")
        return redirect("account:detail",slug)
    return render(request, "account/add_penjualan_detail.html")
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def Pelunasan(request, id):
    datas = Penjualan.objects.get(pk=id)
    print(datas)
    obj = PenjualanDetail.objects.filter(penjualan=id)
    jumlah = 0
    for data in obj:
          x = Menu.objects.get(id=data.menu_id)
          jumlah += x.harga
    return render(request, 'account/pelunasan.html', {'datas':datas,'jumlah':jumlah})
@user_passes_test(lambda u: u.is_authenticated, login_url='account:login')
def Pembayaran(request,id,jumlah_id):
    obj = get_object_or_404(Penjualan, pk=id)
    obj.total += jumlah_id
    obj.lunas += 1
    obj.save()
    messages.success(request, "Payment success.")
    return redirect("account:index")
