from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('predict', views.predict, name='predict'),
    

    path('logout1/', views.logout1, name='logout1'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
]
