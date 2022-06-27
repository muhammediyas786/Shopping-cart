from .views import *



def count(request):
    item_count = 0
    if 'admin' in request.path:
        return ()
    else:
        try:
            c_obj = cart.objects.filter(cart_id=cart_id(request))
            c_items = ct_items.objects.all().filter(items = c_obj[:1])
            for c in c_items:
                item_count += c.quantity
        except cart.DoesNotExist:
            item_count=0
        return dict(item_count=item_count)