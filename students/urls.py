from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:student_id>/', views.edit, name='edit'),
    path('delete/<int:student_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:student_id>/', views.update, name='update'),
]