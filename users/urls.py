from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name='registerView' ),
    path('sigin/', views.login_view, name='sigin'),
     path('logout/', views.logout_views, name='logout_views'),
     path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile')
]