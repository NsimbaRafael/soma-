from django.urls import path, include
from . import views

urlpatterns = [
   
    path('upload_material/', views.upload_material, name='upload_material'),
    path('lista_materiais/', views.lista_materiais, name='lista_materiais'),
]