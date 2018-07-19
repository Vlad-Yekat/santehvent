from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .models import Goods


def index(request):
    goods_list = []
    other_arr = []

    goods_list = Goods.objects.order_by('-goodName')[:5]

    template = loader.get_template('catalog/index.html')
    context = {
        'goods_list': goods_list, 'other': other_arr,
    }
    return HttpResponse(template.render(context, request))
