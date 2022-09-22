"""salud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from metricas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show),
    path('', RedirectView.as_view(url='show', permanent=True)),
    path('diary', views.diary),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)