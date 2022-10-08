from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProfessorAPIView.as_view()),
    path('<int:id>/aulas/', views.CadastrarAulaAPIView.as_view()),
    path('aulas/', views.AulaSerializerAPIView.as_view()),
]
