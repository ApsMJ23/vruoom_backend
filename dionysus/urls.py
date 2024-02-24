from django.urls import path
from . import views


urlpatterns=[
    path('client/list',view=views.getClientList,name='getClientList'),
    path('client/add',view=views.addClient,name='addClient'),
    
]