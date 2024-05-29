"""
URL configuration for proyectefl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import home, seg, exit, create, tabla, form_user_view, acerca

urlpatterns = [
    path('', home, name='home'),
    path('prod/', create, name='prod'),
    path('seg/', seg, name='seg'),
    path('logout/', exit, name='exit'),
    path('formulario/', form_user_view, name='form_user'),
    path('acerca/', acerca, name='acerca'),
    path('tabla/', tabla, name='tabla')   
]
