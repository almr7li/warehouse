from django.shortcuts import render, redirect
from .forms import GoodsForm
from .models import Goods

def goods_list(request):
    context = {'goods_list': Goods.objects.all()}
    return render(request, "warehouse_register/goods_list.html", context)

def goods_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = GoodsForm()
        else:
            goods = Goods.objects.get(pk=id)
            form = GoodsForm(instance=goods)
        return render(request, "warehouse_register/goods_form.html", {'form': form})
    elif request.method == "POST":
        if id == 0:
            form = GoodsForm(request.POST)
        else:
            goods = Goods.objects.get(pk=id)
            form = GoodsForm(request.POST, instance=goods)
        if form.is_valid():
            form.save()
            return redirect('/goods/list')
    else:
        
        pass

def goods_delete(request):
    return
