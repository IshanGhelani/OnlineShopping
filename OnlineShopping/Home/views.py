from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ProductDescription


def redirect(request):
    return HttpResponseRedirect('/Home/')


def search(request):
    item = request.POST.get('q')
    if item == 'tv':
        item = 'television'
    if item == 'all':
        product = ProductDescription.objects.all()
    else:
        product = ProductDescription.objects.filter(item=item)
    return render(request, 'index2.html', {'product': product})


def show(request):
    product = ProductDescription.objects.all()
    return render(request, 'index2.html', {'product': product})


#def temp(request):
 #   return render(request, 'home.html')


def showt(request):
    item = request.POST.get('item')
    if item == 'all':
        product = ProductDescription.objects.all()
    else:
        product = ProductDescription.objects.filter(item=item)
    return render(request, 'index2.html', {'product': product})


def detail(request):
    product = request.GET.get('product')
    p = ProductDescription.objects.get(p_id=product)
    return render(request, 'detail.html', {'p': p})
