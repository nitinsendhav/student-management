from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('search/',views.search, name="search"),
    path('contact/', views.contact, name='contact'),
]
