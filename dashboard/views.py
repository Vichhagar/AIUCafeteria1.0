from django.shortcuts import render
from django.views import generic
from .models import Food, Vote
from .forms import addFood

class Dashboard(generic.ListView):
    model = Food
    template_name = 'dashboard/index.html'
    context_object_name = 'foods'

    def get_queryset(self):
        return Food.objects.all()[:10]

class ViewAllFood(generic.ListView):
    model = Food
    template_name = 'dashboard/allFood.html'
    context_object_name = 'foods'

    def get_queryset(self):
        return Food.objects.all().order_by('-foodManufactureDate')

class FoodDetail():
    pass

class AddFood(generic.CreateView):
    model = Food
    template_name = 'dashboard/index.html'
    form_class = addFood
    success_url = '/dashboard/'
    print("Running")

class EditFood(generic.UpdateView):
    model = Food
    fields = ['foodImage', 'foodName', 'foodPrice', 'foodAvailableDay']
    template_name = 'dashboard/editFood.html'
    success_url = '/dashboard/'


class DeleteFood(generic.DeleteView):
    model = Food
    success_url = '/dashboard/'



