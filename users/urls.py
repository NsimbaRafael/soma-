from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name='registerView' ),
    path('sigin/', views.login_view, name='sigin'),
    path('homepage/', views.homepage, name='homepage')
]