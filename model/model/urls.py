
from django.contrib import admin
from django.urls import path,include
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user.views.index, name='list'),
    path('post/',include('post.urls')),

]
