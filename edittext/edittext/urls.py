
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('title',views.title,name='title'),
    path('lower',views.lower,name='lower'),
    path('analize',views.analize,name='analize')
]
