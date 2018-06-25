from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import good


def index(request):
    goods_list = []
    other_arr = []

    goods_list = good.objects.order_by('-qoodName')[:5]

    template = loader.get_template('catalog/index.html')
    context = {
        'goods_list': goods_list, 'other': other_arr,
    }
    return HttpResponse(template.render(context, request))
