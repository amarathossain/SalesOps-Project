from django.urls import path
from . import views

urlpatterns = [
    path('divisions/', views.division_list, name='division_list'),
    path('divisions/add/', views.division_create, name='division_create'),
    path('divisions/edit/<int:pk>/', views.division_update, name='division_update'),
    path('divisions/delete/<int:pk>/', views.division_delete, name='division_delete'),
]