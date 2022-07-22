from django.shortcuts import render, redirect
from .forms import PeopleForm
from .models import People


# Create your views here.


def people_list(request):
    context = {'people_list': People.objects.all()}
    return render(request, "people_register/people_list.html", context)


def people_form(request, ID=0):
    if request.method == "GET":
        if ID == 0:
            form = PeopleForm()
        else:
            people = People.objects.get(pk=ID)
            form = PeopleForm(instance=people)
        return render(request, "people_register/people_form.html", {'form': form})
    else:
        if ID == 0:
            form = PeopleForm(request.POST)
        else:
            people = People.objects.get(pk=ID)
            form = PeopleForm(request.POST, instance=people)
        if form.is_valid():
            form.save()
        return redirect('/people/list')


def people_delete(request, ID):
    people = People.objects.get(pk=ID)
    people.delete()
    return redirect('/people/list')
