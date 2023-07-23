from django.urls import path
from .views import blog_list, edit_post, create_post


urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:pk>', edit_post, name='edit_post'),
]