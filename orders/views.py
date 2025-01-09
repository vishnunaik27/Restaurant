from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import OrderForm


# Create your views here.
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'orders/product_list.html', {'products' : products})

def create_order(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'orders/order_success.html', {'product': product})
        else:
            form = OrderForm()
        return render(request, 'orders/create_order.html', {'form': form, 'product': product})

