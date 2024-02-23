# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Goods
from .forms import GoodsForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def goods_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = GoodsForm()
        else:
            goods = Goods.objects.get(pk=id)
            form = GoodsForm(instance=goods)
        return render(request, "warehouse_register/goods_form.html", {'form': form})
    else:
        if id == 0:
            form = GoodsForm(request.POST)
        else:
            goods = Goods.objects.get(pk=id)
            form = GoodsForm(request.POST, instance=goods)
        if form.is_valid():
            form.save()
            return redirect('goods_list')  # Redirect to the goods list page after adding or updating goods

def goods_list(request):
    goods_list = Goods.objects.all()
    return render(request, "warehouse_register/goods_list.html", {'goods_list': goods_list})

def goods_delete(request, id):
    # Retrieve the Goods object
    goods = get_object_or_404(Goods, id=id)
    
    # Delete the goods object
    goods.delete()
    
    # Redirect to the goods list page
    return redirect('goods_list')

class CustomLoginView(LoginView):
    template_name = 'custom_login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('goods_list')

# views.py

from django.shortcuts import render
from .models import Goods

def goods_list(request):
    search_query = request.GET.get('search', '')
    goods_list = Goods.objects.all()
    if search_query:
        goods_list = goods_list.filter(name__icontains=search_query) | \
                     goods_list.filter(price__icontains=search_query) | \
                     goods_list.filter(quantity__icontains=search_query)
    return render(request, "warehouse_register/goods_list.html", {'goods_list': goods_list, 'search_query': search_query})
