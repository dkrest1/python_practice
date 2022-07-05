from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def dynamic_lookup_view(request):
    queryset = Product.objects.all()
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    # if request.method ==  "POST":
    #     obj.delete()
    #     return redirect("../")
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "objects_list": queryset
    }
    
    return render(request, "myApp/product_list.html", context)