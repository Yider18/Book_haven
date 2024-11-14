"""
URL configuration for Book_haven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Book_haven/urls.py
from django.contrib import admin
from django.urls import path
from main import views as main_views  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),  
    path('buscar_libros/', main_views.buscar_libros, name='buscar_libros'),  
    path('detalles/<str:google_books_id>/', main_views.detalles_libro, name='detalles_libro'), 
    path('buscar_libros_locales/', main_views.buscar_libros_locales, name='buscar_libros_locales'),
    path('detalle_libro_local/<int:libro_id>/', main_views.detalle_libro_local, name='detalle_libro_local'),

] 