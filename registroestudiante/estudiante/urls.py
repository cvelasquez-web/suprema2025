from django.urls import path
from estudiante.views import EstudianteApiView, EstudianteApiViewDetail

urlpatterns_estudiantes = [

    path('v1/estudiantes',EstudianteApiView.as_view()),
    path('v1/estudiantes/<int:id>',EstudianteApiViewDetail.as_view()), 
]