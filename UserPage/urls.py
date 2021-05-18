from django.urls import path
from . import views

app_name = 'Userpage'
urlpatterns = [
    path('', views.UserDashboard.as_view(), name='UserDashboard'),
    path('vote',views.processVote, name='vote')
   
]