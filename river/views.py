from django.shortcuts import render, redirect
from .forms import RiverForm
from .models import River



def add_river(request):
    template_name = 'river/add.html'
    form = RiverForm()
    if request.method == 'POST':
        form = RiverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_river(request):
    template_name = 'river/show.html'
    rivers = River.objects.all()
    context = {'rivers': rivers}
    return render(request, template_name, context)


def update_river(request, pk):
    template_name = 'river/add.html'
    obj = River.objects.get(id=pk)
    form = RiverForm(instance=obj)
    if request.method == 'POST':
        form = RiverForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_river(request, pk):
    obj = River.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'river/confirm.html')