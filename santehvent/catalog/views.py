from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader

from django.http import HttpResponse
from .models import Goods


def index(request):
    goods_list = []
    other_arr = []

    goods_list = Goods.objects.order_by('-goodName')[:12]

    template = loader.get_template('catalog/index.html')
    context = {
        'goods_list': goods_list, 'other': other_arr,
    }
    return HttpResponse(template.render(context, request))

def detail(request, good_id):
    template = loader.get_template('catalog/details.html')
    good_obj = get_object_or_404(Goods, pk=good_id)
    context = {
        'good_obj': good_obj,
    }
    return HttpResponse(template.render(context, request))

def reviews(request, good_id):
    template = loader.get_template('catalog/reviews.html')
    context = {
        'good_id': str(good_id),
    }
    return HttpResponse(template.render(context, request))
