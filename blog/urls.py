from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('view/', views.viewPost, name='view'),
    path('delete/<int:id>/', views.deletePost, name='delete'),
    path('edit/<int:id>/', views.editPost, name='edit'),
]