# myapp/views.py
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_persons')  # Redirect ke halaman daftar orang
    else:
        form = PersonForm()
    return render(request, 'members/add_person.html', {'form': form})

def list_persons(request):
    persons = Person.objects.all()
    return render(request, 'members/list_persons.html', {'persons': persons})


def update_person(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('list_persons')
    else:
        form = PersonForm(instance=person)
    return render(request, 'members/update_person.html', {'form': form})


def delete_person(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect('list_persons')
    return render(request, 'members/delete_person.html', {'person': person})
