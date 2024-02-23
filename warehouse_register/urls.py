from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(template_name='custom_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', views.goods_form, name='goods_add'),
    path('', views.goods_form, name='goods_insert'),  # For inserting new goods
    path('<int:id>/', views.goods_form, name='goods_update'),  # For updating existing goods
    path('list/', views.goods_list, name='goods_list'),  # For listing all goods
    path('delete/<int:id>/', views.goods_delete, name='goods_delete'),  # For deleting existing goods
]
