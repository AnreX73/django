from django.shortcuts import render, get_object_or_404

from smart.models import *


def index(request):
    context = {
        'title': 'СМАРТ ФОТО',
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
        'services_title':'фотоуслуги',
        'souvenirs_title':'фотосувениры',
    }
    return render(request, 'smart/index.html', context=context)


def services(request):
    context = {
        'title': 'ФОТОУСЛУГИ',
        'services': Services.objects.filter(cat_id=1),
    }
    return render(request, 'smart/services.html', context=context)


def souvenirs(request):
    context = {
        'title': 'ФОТОСУВЕНИРЫ',
        'services': Services.objects.filter(cat_id=2),
    }
    return render(request, 'smart/souvenirs.html', context=context)


def show_service(request, service_slug):
    service = get_object_or_404(Services, slug=service_slug)
    context = {
        'show_service': service,
        'title': service.title,
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
        'prices': Prices.objects.all(),
        'extracontent': Extra.objects.all(),
    }
    return render(request, 'smart/service_item.html', context=context)
