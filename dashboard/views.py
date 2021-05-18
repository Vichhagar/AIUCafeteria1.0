from django.core.checks import messages
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Food, Vote
from .forms import addFood
import os
from django.contrib import messages

class Dashboard(generic.ListView):
    model = Food
    template_name = 'dashboard/index.html'
    # context_object_name = 'foods'

    def get(self, request, *args, **kwargs):
        vote = Vote.objects.all()
        # print(vote.upVote)
        foods = Food.objects.all().order_by('-foodAddDate')[:10]
        count = Food.objects.all().count()

        context = {
            'foods':foods,
            'count':count,
            'vote':vote
        }
        return render(request, self.template_name, context)

class ViewAllFood(generic.ListView):
    model = Food
    template_name = 'dashboard/allFood.html'
    context_object_name = 'foods'

    def get_queryset(self):
        return Food.objects.all().order_by('-foodAddDate')

class AllFoodList(generic.View):
    def get(self, request):
        allFood = Food.objects.all()
        context = {
            'foods':allFood
        }

        return render(request, 'dashboard/allFoodList.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            food_id = request.POST.getlist('id[]')
            for id in food_id:
                print(id)
                food = Food.objects.get(pk=id)
                food.delete()
            return redirect('dashboard:delete_multi')



# class AddFood(generic.CreateView):
#     model = Food
#     template_name = 'dashboard/index.html'
#     form_class = addFood
#     success_url = '/dashboard/'

class CreatePostView(generic.CreateView):
    model = Food
    form_class = addFood
    template_name = 'dashboard/post.html'
    success_url = reverse_lazy('dashboard:viewallfood')

    # def post(self, request, *args, **kwargs):
    #     messages.success(request, "Congraadulation, New Food Added into Menu")
    #     return redirect('/dashboard/')


class EditFood(generic.UpdateView):
    model = Food
    fields = ['foodImage', 'foodName', 'foodPrice', 'foodAvailableDay']
    template_name = 'dashboard/editFood.html'
    success_url = reverse_lazy('dashboard:viewallfood')

    # def post(self, request, *args, **kwargs):
    #     form = addFood(request.POST)
    #     if form.is_valid():
    #         super()

    #     messages.success(request, "Yayyy!!")
    #     return super().get(request, *args, **kwargs)

class DeleteFood(generic.DeleteView):
    model = Food
    success_url = reverse_lazy('dashboard:viewallfood')



