import json

from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, OrderForm
from .models import ProductInOrder
from products.models import Product
# Create your views here.


def order_checkout(request):
    form = CustomerForm
    sub_form = OrderForm
    context = {
        'form': form,
        'sub_form': sub_form,
    }

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        sub_form = OrderForm(request.POST)
        data = json.loads(request.POST['Cart'])
        if form.is_valid() and sub_form.is_valid():
            order = sub_form.save(commit=False)
            order.customer = form.save()
            order.save()
            order.productinorder_set.bulk_create([ProductInOrder(
                order_id=order.id,
                product_id=pk,
                quantity=data[pk],
                price_per_item=Product.objects.get(id=pk).price,
                total_price=(Product.objects.get(id=pk).price * int(data[pk]))
            ) for pk in data])

            all_product_in_order = order.productinorder_set.all()
            order.total_price = sum([product.total_price for product in all_product_in_order])
            order.save()
        return HttpResponse('response :)', status=200)
    else:
        return render(request, 'orders/order_checkout.html', context)
