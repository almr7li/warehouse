from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
 openapi. Info(
 title="warehouse",
 default_version="v1",
 description="Test description",
 terms_of_service="https://www.google.com/policies/terms/",
 contact=openapi. Contact(email="contact@snippets.local"),
 license=openapi. License(name="BSD License"),
 ),
 public=True,
 permission_classes=(permissions. AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(template_name='custom_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', views.goods_form, name='goods_add'),
    path('', views.goods_form, name='goods_insert'),  # For inserting new goods
    path('<int:id>/', views.goods_form, name='goods_update'),  # For updating existing goods
    path('list/', views.goods_list, name='goods_list'),  # For listing all goods
    path('delete/<int:id>/', views.goods_delete, name='goods_delete'),  # For deleting existing goods
]
