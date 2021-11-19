"""capuchintz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from base import views as base_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.homepage, name = "home"),
    path('news/', base_views.news, name = "news"),
    path('gallery/', base_views.gallery, name = "gallery"),
    path('about/', base_views.about, name = "about"),
    path('articles/', base_views.articles, name = "articles"),
    path('(?P<slug>.*)$', base_views.details, name="details"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('parishministry/', base_views.parishministry, name="parishministry"),
    path('educationmin/', base_views.educationmin, name="eduactionmin"),
    path('downloadpdf/', base_views.download_pdf_file, name = "download_pdf_file"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
