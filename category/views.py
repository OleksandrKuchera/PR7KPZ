from django.shortcuts import render
from .models import Article

def news_view(request):
    articles = Article.objects.all()
    return render(request, 'news.html', {'articles': articles})
