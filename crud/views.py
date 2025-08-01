from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from app.models import studentModel
from app.forms import ContactForm
from django.contrib import messages


def home(request):
    form = StudentForm()
    data = studentModel.objects.all()
    total = studentModel.objects.all().count()
    pas = studentModel.objects.filter(result = "Pass").count()
    Fail = studentModel.objects.filter(result__icontains = "f").count( )

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')
        

    return render(request, 'index.html', {'form': form, 'data': data, "total": total, "pass":pas, "fail":Fail})


def delete(request, id):
    record = get_object_or_404(studentModel, id=id)
    record.delete()
    return redirect('home')

def update(request, id):
    record = get_object_or_404(studentModel, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=record)

    return render(request, 'update.html', {'form': form})

def add(request):
    form = StudentForm()
    data = studentModel.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')

    return render(request, 'add.html', {'form': form, 'data': data})


def search(request):
    query=""
    if request.method == "GET":
        query = request.GET.get("q")

    
    data = studentModel.objects.filter(name__icontains=query)
    return render(request, "search.html",{"data":data})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thanks for contacting us Well reply soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
