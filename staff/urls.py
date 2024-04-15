from django.urls import path
from staff import views

urlpatterns = [
    path('profile/<slug:slug>/', views.profile, name='profile'),
]