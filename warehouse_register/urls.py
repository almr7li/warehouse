from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.goods_form),
    path('list/',views.goods_list),
]
