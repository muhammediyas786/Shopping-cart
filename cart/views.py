from django.shortcuts import render, redirect, get_object_or_404
from ShopApp.views import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def cart_details(request, total=0, count=0):
    c_item = None
    c_obj = None
    try:
        c_obj = cart.objects.get(cart_id=cart_id(request))
        c_item = ct_items.objects.filter(items=c_obj, active=True)
        for i in c_item:
            total += (i.product.p_price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'cart_items': c_item, 'total': total, 'count': count})


def cart_id(request):
    key = request.session.session_key
    if not key:
        key = request.session.create()
    return key


def add_to_cart(request, pro_id):
    p_obj = products.objects.get(id=pro_id)
    try:
        c_obj = cart.objects.get(cart_id=cart_id(request))
    except cart.DoesNotExist:
        c_obj = cart.objects.create(cart_id=cart_id(request))
        c_obj.save()
    try:
        c_item = ct_items.objects.get(product=p_obj, items=c_obj)
        if c_item.quantity < c_item.product.p_stock:
            c_item.quantity += 1
        c_item.save()
    except ct_items.DoesNotExist:
        c_item = ct_items.objects.create(product=p_obj, quantity=1, items=c_obj)
        c_item.save()
    return redirect('cart')


def Dec_quant(request, product_id):
    c_obj = cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(products, id=product_id)
    c_item = ct_items.objects.get(product=product)
    if c_item.quantity > 1:
        c_item.quantity -= 1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cart')


def remove(request, id):
    c_obj = cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(products, id=id)
    c_item = ct_items.objects.get(product=product, items=c_obj)
    c_item.delete()
    return redirect('cart')
