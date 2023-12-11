from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success_page, name='success_page'),
    path('match/<str:uid>/', views.view_match, name='view_match'),
]
