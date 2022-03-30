from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('<int:pk>/balanceSheet/', views.balanceSheet, name="balanceSheet"),
    path('addTransaction', views.addTransaction, name='addTransaction'),
]
