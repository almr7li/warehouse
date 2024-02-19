from django.shortcuts import render
from .forms import GoodsForm

# Create your views here.
def goods_list(request):
    return render(request, "warehouse_register/warehouse_list.html")


def goods_form(request):
        form = GoodsForm()
        return render(request, "warehouse_register/warehouse_form.html",{'form':form})


def goods_delete(request):
    return
