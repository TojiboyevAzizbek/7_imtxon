from django.urls import path
from . import views

urlpatterns = [
    path('staff-list', views.staff_list),
    path('staff-create', views.staff_create),
    path('attendance-create/<int:id>', views.attendance_create), 
]