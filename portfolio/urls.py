from django.contrib import admin
from django.urls import path
import content.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',content.views.main,name="main"),
    path('pfedit/',content.views.pfedit,name="pfedit"),
]
