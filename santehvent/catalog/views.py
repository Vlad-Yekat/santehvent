from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader

from django.http import HttpResponse
from .models import Goods, Invoice
from celery.decorators import task
from django.views import View
from .forms import InvoiceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


class InvoiceCreate(LoginRequiredMixin, CreateView):
    model = Invoice
    # fields = ['goodID', 'goodcount', 'goodPrice']
    fields = "__all__"
    success_url = "/invoice/add"

    def form_valid(self, form):
        # model = form.save(commit=False)
        form.instance.user = self.request.user
        return super().form_valid(form)


def index(request):
    goods_list = []
    other_arr = []

    goods_list = Goods.objects.order_by("-goodName")[:12]

    q = request.GET.get("q")
    if q is not None:
        goods_list = Goods.objects.all()
        goods_list = goods_list.filter(goodName__icontains=q)
        other_arr.append("search_string:" + str(q))

    template = loader.get_template("catalog/index.html")
    context = {"goods_list": goods_list, "other": other_arr}
    return HttpResponse(template.render(context, request))


def reestr(request):
    goods_list = []
    other_arr = []

    goods_list = Goods.objects.order_by("-goodName")

    q = request.GET.get("q")
    if q is not None:
        goods_list = goods_list.filter(goodName__icontains=q)

    template = loader.get_template("catalog/reestr.html")
    context = {"goods_list": goods_list, "other": other_arr}
    return HttpResponse(template.render(context, request))


def detail(request, good_id):
    template = loader.get_template("catalog/details.html")
    good_obj = get_object_or_404(Goods, pk=good_id)
    context = {"good_obj": good_obj}
    return HttpResponse(template.render(context, request))


def reviews(request, good_id):
    template = loader.get_template("catalog/reviews.html")
    context = {"good_id": str(good_id)}
    return HttpResponse(template.render(context, request))


# all = Goods.objects.all()
# one = Goods.objects.get(pk=1)
# some = Goods.objects.filter(name='123')
# notsome = Goods.objects.exclude(name='123')
# andgood = Goods.objects(pole1='123',pole2='124')
# orand : from django.db.models import Q / orgood = Goods.objects.filter((Q(pole1='1'))|(Q(pole1='2'))&Q(pole2='aa'))
# step1,2  some = Goods.objects.filter(pole1='1') / some2 = some.filter(pole1='1')

# ingod = Goods.objects.filter(pole1__in=[1,2])
# contains(icontains) = like(ilike) '%ddd%'
# startwith = like 'ddd%'
# gt,gte,lt,lte >,>=, <,<=
# range=between , insull=is null
