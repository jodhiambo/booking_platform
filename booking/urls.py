from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('single-room/', views.single_room, name='single_room'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single_blog'),
]
