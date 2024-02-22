from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_form, name='goods_insert'),  # For inserting new goods
    path('<int:id>/', views.goods_form, name='goods_update'),  # For updating existing goods
    path('list/', views.goods_list, name='goods_list'),  # For listing all goods
]
