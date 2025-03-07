from django.urls import path
from .views import post_list, post_create, post_update, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('update/<int:id>/', post_update, name='post_update'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
]