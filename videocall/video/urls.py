from django.urls import path
from video import views

urlpatterns = [
    path("",views.register,name='register'),
    path('login/',views.login_us,name='login'),
    path('home/', views.home,name='home'),
    path('meeting/', views.videocall,name='meeting'),
    path('logout/', views.logout_vu,name='logout'),
    path('join/', views.join_room,name='join_room')
    ]
