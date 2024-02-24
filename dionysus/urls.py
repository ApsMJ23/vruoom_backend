from django.urls import path
from . import views


urlpatterns=[
    path('client/list',view=views.getClientList,name='getClientList')
]