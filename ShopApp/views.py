from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def home(request, c_slug=None):
    if c_slug is not None:
        c_page = get_object_or_404(category, c_slug=c_slug)
        p_obj = products.objects.filter(p_category=c_page, p_available=True)
    else:
        p_obj = products.objects.all().filter(p_available=True)
    c_obj = category.objects.all()

    paginator = Paginator(p_obj, 12)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pro = paginator.page(page.num_pages)

    return render(request, 'index.html', {'products': p_obj, 'category': c_obj, 'page': pro})


def details(request, c_slug, p_slug):
    try:
        p_obj = products.objects.get(p_slug=p_slug)
    except Exception as e:
        raise e
    return render(request, 'detail.html', {'products': p_obj})


def search_box(request):
    p_obj = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        p_obj = products.objects.all().filter(Q(p_name__contains=query) | Q(p_desc__contains=query))
    return render(request, 'search.html', {'query': query, 'products': p_obj})


def cart(request):
    return render(request, 'cart.html')
