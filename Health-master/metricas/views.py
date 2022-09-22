from tkinter import messagebox
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from metricas.forms import MetricsForm
from metricas.models import Metrics
# Create your views here.


def diary(request):
    if request.method == "POST":
        form = MetricsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = MetricsForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    metric = Metrics.objects.all()
    return render(request, "show.html", {'metric': metric})


def edit(request, id):
    metrics = Metrics.objects.get(id=id)
    stressLevels = Metrics.STRESS_LEVEL
    return render(request, 'edit.html', {'metrics': metrics, 'stressLevels': stressLevels})


def update(request, id):
    metrics = Metrics.objects.get(id=id)
    form = MetricsForm(request.POST, instance=metrics)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'metrics': metrics})


def destroy(request, id):
    metrics = Metrics.objects.get(id=id)
    resultado = messagebox.askquestion("Eliminar", 
    "Desea eliminar el objeto")
    if resultado == "yes":
        metrics.delete()
    return redirect("/show")
