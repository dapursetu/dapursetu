from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Menu,Penjualan, PenjualanDetail

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        #fields = '__all__'
        #exclude = ['title']
        fields = ('nama', 'deskripsi','harga',)
        #widgets = {'pertanyaan_text': Input(attrs={'cols': 100, 'rows': 1}),}
        labels = {
            'nama': _('Name'),
            'deskripsi': _('Description'),
            'harga': _('Price'),
        }
        help_texts = {
            'nama': _('Name.'),
            'deskripsi': _('Description.'),
            'harga': _('Price.'),
        }
        error_messages = {
            'nama': {
                'max_length': _("Menu name are too long."),
            },
            'deskripsi': {
                'max_length': _("Description name are too long."),
            },
        }

class PenjualanForm(ModelForm):
    class Meta:
        model = Penjualan
        #fields = '__all__'
        #exclude = ['title']
        fields = ('pembeli',)
        #widgets = {'pertanyaan_text': Input(attrs={'cols': 100, 'rows': 1}),}
        labels = {
            'pembeli': _('Customer Name'),
        }
        help_texts = {
            'pembeli': _('Customer Name'),
        }
        error_messages = {
            'pembeli': {
                'max_length': _("Customer name are too long."),
            },
        }

class PenjualanDetailForm(ModelForm):
    class Meta:
        model = PenjualanDetail
        #fields = '__all__'
        #exclude = ['title']
        fields = ('menu',)
        #widgets = {'pertanyaan_text': Input(attrs={'cols': 100, 'rows': 1}),}
        labels = {
            'menu': _('Menu'),
        }
        help_texts = {
            'menu': _('Menu'),
        }