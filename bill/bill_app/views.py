from django.shortcuts import render
from .form import data
from .models import Store_add
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import UpdateView

def adding_store(request):
    form = data
    context = {'form': form}
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product')

    return render(request, 'storeadd.html', context=context)


def product(request):
    form = Store_add.objects.all()
    context = {'form': form}
    return render(request, 'storeproduct.html', context=context)


def delete(request, id):
    form = Store_add.objects.get(id=id)
    form.delete()
    return redirect('/product')


def update(request, id):
    context = {}
    obj = get_object_or_404(Store_add, id=id)
    form = data(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, 'update.html', context=context)





