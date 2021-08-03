from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Barang, Menu, Pengeluaran, Penjualan, PenjualanDetail


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        #fields = '__all__'
        #exclude = ['title']
        fields = ('nama', 'deskripsi', 'harga',)
        #widgets = {'pertanyaan_text': Input(attrs={'cols': 100, 'rows': 1}),}
        labels = {
            'nama': _(''),
            'deskripsi': _(''),
            'harga': _(''),
        }
        error_messages = {
            'nama': {
                'max_length': _("Menu name are too long."),
            },
            'deskripsi': {
                'max_length': _("Description name are too long."),
            },
        }
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'autocomplete': 'off',
                    'placeholder': 'Name',
                }
            ),
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm',
                    'rows': '6',
                    'autocomplete': 'off',
                    'placeholder': 'Description',
                    
                }
            ),
            'harga': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Price'
                }
            ),
        }


class PenjualanForm(ModelForm):

    class Meta:
        model = Penjualan
        fields = ('pembeli',)
        labels = {
            'pembeli': _(''),
        }
        error_messages = {
            'pembeli': {
                'max_length': _("Customer name are too long."),
            },
        }
        widgets = {
            'pembeli': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'autocomplete': 'off',
                    'placeholder': 'Customer Name'
                }
            ),
        }


class PenjualanDetailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu'].widget.attrs.update(
            {'class': 'custom-select mr-sm-2','autocomplete': 'off','placeholder': 'Menu'})

    class Meta:
        model = PenjualanDetail
        #fields = '__all__'
        #exclude = ['title']
        fields = ('menu',)
        #widgets = {'pertanyaan_text': Input(attrs={'cols': 100, 'rows': 1}),}
        labels = {
            'menu': _('Menu'),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BarangForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_barang'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'autocomplete': 'off',
            'placeholder': 'Items Name',
            })
        self.fields['harga'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'autocomplete': 'off',
            'placeholder': 'Price',
            })

    class Meta:
        model = Barang
        fields = ('nama_barang','harga',)
        labels = {
            'nama_barang': _(''),
            'harga': _(''),
        }

class PengeluaranForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['keterangan'].queryset = Penjualan.objects.filter(lunas='0')
        self.fields['barang'].widget.attrs.update({
            'class': 'custom-select mr-sm-2',
            'autocomplete': 'off',
            'placeholder': 'Items Name',
            })
        self.fields['keterangan'].widget.attrs.update({
            'class': 'custom-select mr-sm-2',
            'autocomplete': 'off',
            'placeholder': 'Descriptions',
            })

    class Meta:
        model = Pengeluaran
        fields = ('barang','keterangan',)
        labels = {
            'barang': _(''),
            'keterangan': _(''),
        }