from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='c_slug'),
    path('search',views.search_box,name='search'),
    path('<slug:c_slug>/<slug:p_slug>/',views.details,name='details')
]