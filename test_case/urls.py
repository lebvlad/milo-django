from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users-list'),
    path('create_user', views.user_create, name='user-create'),
    path('profile/<str:profile_name>', views.user_profile, name='user-profile'),
    path('edit/<str:profile_name>', views.user_edit, name='user-edit'),
    path('delete/<str:profile_name>', views.user_delete, name='user-delete'),
    path('export/', views.export_csv, name='export-csv'),
]
