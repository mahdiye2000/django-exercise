from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles),
    path('<str:slug>/', views.article),

]