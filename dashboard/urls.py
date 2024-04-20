from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #Staff's urs
    path('staff-create/', views.staff_create, name='staff_create'),
    path('staff-list/', views.staff_list, name='staff_list'),
    path('staff-detail/<int:id>/', views.staff_detail, name='staff_detail'),
    path('staff-edit/<int:id>/', views.staff_edit, name='staff_edit'),
    path('staff-delete/<int:id>/', views.staff_delete, name='staff_delete'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),

    path('log-in/', views.log_in, name='login'),
    path('log-out/', views.log_out, name='logout'),
    # path('query/', views.query, name='query'),


]