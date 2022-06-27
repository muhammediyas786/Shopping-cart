from django.urls import path
from . import views



urlpatterns = [
    path('cart/',views.cart_details,name='cart'),
    path('add/<int:pro_id>/',views.add_to_cart,name='add'),
    path('dec/<int:product_id>/',views.Dec_quant,name='dec'),
    path('remove/<int:id>/',views.remove,name='remove')
]