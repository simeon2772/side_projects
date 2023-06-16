from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from Car_Collection_App.web.forms import ProfileCreateForm, CarCreateForm
from Car_Collection_App.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    return render(request, 'index.html')


def catalogue(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'cars': Car.objects.all()
    }
    return render(request, 'catalogue.html', context=context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            return ValidationError

    context = {
        'form': form
    }
    return render(request, 'profile/profile-create.html', context=context)


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


def car_create(request):
    if request.method == "GET":
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            return ValidationError

    context = {
        'form': form
    }
    return render(request, 'car/car-create.html', context=context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    return render(request, 'car/car-details.html')


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request, pk):
    return render(request, 'car/car-delete.html')
