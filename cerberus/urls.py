from django.urls import path


from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('activate/', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('getNotStaffUsers/', views.getNotStaffUsers, name='getNotStaffUsers')

]