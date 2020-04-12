from django.contrib import admin
from django.urls import path
import exchangeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',exchangeapp.views.home, name='home'),
    path('result/',exchangeapp.views.result,name='result'),
    path('about/',exchangeapp.views.about,name='about')
]
