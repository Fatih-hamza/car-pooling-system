from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeCovoiturage),
    path('/addProposition/', views.addProposition),
    path('/wantProp/', views.wantProp),
    path('/aboutUs/', views.aboutUs),
    path('/FAQ/', views.FAQ)
]