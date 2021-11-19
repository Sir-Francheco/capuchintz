from django.shortcuts import render
from .models import News
from .models import Articles
import mimetypes
import os

news_list = News.objects.all().order_by('-date')
article_list = Articles.objects.all().order_by('-date')

def homepage(request):
    return render(request, 'homepage.html', {'news_list': news_list, 'article_list': article_list})

def news(request):
    return render(request, 'news.html', {'news_list': news_list})

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def details(request, slug):
    try:
        news_details = News.objects.get(slug=slug)
        return render(request, 'news_details.html', {'news_details': news_details})
    except News.DoesNotExist:
        article_details = Articles.objects.get(slug=slug)
        return render(request, 'article_details.html', {'article_details': article_details})

def articles(request):
    return render(request, 'articles.html', {'article_list': article_list})

def parishministry(request):
    return render(request, 'parishministry.html')

def educationmin(request):
    return render(request, 'educationmin.html')

def download_pdf_file(request, filename=''):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + 'media/files/' + filename
        path = open(filepath, 'rb')
        mime_type, _=mimetypes.guess_type(filepath)
        response = render(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return render(request, "documents.html")
