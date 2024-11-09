from django import forms
from subscribe.models import Customer

class DaftarPelanggan(forms.ModelForm):
    class Meta():
        model = Customer
        fields ='__all__'