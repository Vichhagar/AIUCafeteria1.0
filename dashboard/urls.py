from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='index'),
    path('addFood/', views.AddFood.as_view(), name='addFood'),
    path('viewallfood/', views.ViewAllFood.as_view(), name='viewallfood'),
    path('editfood/<str:pk>', views.EditFood.as_view(), name='editfood'),
    path('delete/<str:pk>', views.DeleteFood.as_view(), name='delete'),
]