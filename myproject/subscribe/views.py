from django.shortcuts import render
from subscribe.models import Customer
from subscribe.form import DaftarPelanggan

# Create your views here.
def index(request):
    return render (request, 'subscribe/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers':customer_list}
    return render (request, 'subscribe/customers.html', context=customer_dict)

def layanan(request):
    form = DaftarPelanggan()

    if request.method == 'POST':
        form = DaftarPelanggan(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("error : form invalid")

    return render (request, 'subscribe/langganan.html', {'form':form})
    
    