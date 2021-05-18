from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.views.generic.list import ListView
from dashboard.models import Food, Vote
from django.http import Http404, JsonResponse
from django.db.models import F
from datetime import date
import calendar

class ViewallFood(generic.ListView):
    model = Food
    template_name = 'UserPage/ViewallFood.html'
    context_object_name = 'OfferedFood'

    def get_queryset(self):
        return Food.objects.all()[:10]

class UserDashboard(generic.ListView):
    model = Food
    template_name = 'UserPage/UserDashboard.html'
    context_object_name = 'OfferedFood'

    def get_queryset(self):
        my_date = date.today()
        today = calendar.day_name[my_date.weekday()] 
        print(today)
        return Food.objects.all().filter(foodAvailableDay = today )



def processVote( request):
    print("hello")
    print(request.POST)
    if request.is_ajax and request.method =="POST":
        type = request.POST.get('type', 0)
        if type and type=='upVote' or type=='downVote' :
            food= Food.objects.get(pk=request.POST['foodId'])
            if Vote.objects.filter(foodId=request.POST['foodId']).exists():
                if type=='upVote':
                    voteItem = Vote.objects.get(foodId=Food.objects.get(pk=request.POST['foodId']))
                    voteItem.upVote= F('upVote') + 1
                    voteItem.save()
                elif type=='downVote':
                    voteItem = Vote.objects.get(foodId=Food.objects.get(pk=request.POST['foodId']))
                    voteItem.downVote= F('downVote') + 1
                    voteItem.save() 
            else:
                if type=='upVote':
                    vote = Vote(foodId=food, upVote=1, downVote=0 )
                    vote.save()
                elif type=='downVote': 
                    vote = Vote(foodId=food, upVote=0, downVote=1 )
                    vote.save()

    return redirect('Userpage:UserDashboard')


                 
                    




        
