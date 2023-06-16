"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from My_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("auth/", views.auth),
    path("reg/", views.reg),
    path("manual/", views.manual),
    path("manual/<cmd_name>", views.manual),
    path("tasks/", views.task),
    path("tasks/<task_id>", views.task),
    path("theory/", views.theory),
    path("theory/<theme_id>", views.theory),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
