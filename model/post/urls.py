from django.urls import path
import post.views

urlpatterns=[
    path('',post.views.list, name='list'),
]