from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:good_id>/', views.detail, name='detail'),
    # ex: /catalog/5/reviews/
    path('<int:good_id>/reviews/', views.reviews, name='reviews'),
]