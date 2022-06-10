from django.shortcuts import render

from smart.models import Services


def index(request):
    context = {
        'title': 'СМАРТ ФОТО',
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
    }
    return render(request, 'smart/index.html', context=context)
