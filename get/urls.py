from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns =[
        path('', views.gtech),
        path('next/', views.login),
        path('login/', views.next),
        path('data/', views.data),
        ]




urlpatterns += staticfiles_urlpatterns()
