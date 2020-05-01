from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',
         views.show_posts,
         name='posts'),

    path('posts/new/',
         views.create_post,
         name='create_post'),

    path('init_data/',
         views.initialize_data,
         name='init_data'),
]
