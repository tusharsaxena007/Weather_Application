from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.homepage ,name ='index' ),
    path('add',views.add, name= 'add'),
    path('delete/<name>',views.delete, name= 'delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

