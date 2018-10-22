from django.urls import path

from . import views

urlpatterns = [
    path('catalog/', views.reestr, name='reestr'),
    path('<int:good_id>/', views.detail, name='detail'),
    # ex: /catalog/5/reviews/
    path('<int:good_id>/reviews/', views.reviews, name='reviews'),
    path('index/', views.index, name='index'),
    path('invoice/', views.FormInvoiceView.as_view()),
    path('', views.index, name='index'),
]