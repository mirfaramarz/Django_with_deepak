from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    #path('signin/', views.signin, name='signin'),
    #path('signout/', views.signout, name='signout'),
]

