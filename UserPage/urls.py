from django.urls import path
from . import views

app_name = 'Userpage'
urlpatterns = [
    path('', views.TodayMenu.as_view(), name='TodayMenu'),
    path('Food-List', views.ViewallFood.as_view(), name='ViewallFood'),

    path('vote',views.processVote, name='vote')
   
]