from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeApiView.as_view(), name='home')
]
