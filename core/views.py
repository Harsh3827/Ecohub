from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from articles.models import Article
from tips.models import Tip
from django.contrib import messages

# Create your views here.

def home(request):
    # Track user visits using sessions
    if request.user.is_authenticated:
        visits = request.session.get('visits', 0)
        request.session['visits'] = visits + 1
    
    # Get recent articles and tips
    recent_articles = Article.objects.all().order_by('-created_at')[:3]
    recent_tips = Tip.objects.all().order_by('-created_at')[:3]
    
    context = {
        'recent_articles': recent_articles,
        'recent_tips': recent_tips,
        'visits': request.session.get('visits', 0),
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def search(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'all')
    
    results = []
    if query:
        if search_type == 'articles' or search_type == 'all':
            articles = Article.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            results.extend(articles)
        
        if search_type == 'tips' or search_type == 'all':
            tips = Tip.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            results.extend(tips)
    
    context = {
        'query': query,
        'search_type': search_type,
        'results': results,
    }
    return render(request, 'core/search.html', context)

@login_required
def user_history(request):
    visits = request.session.get('visits', 0)
    context = {
        'visits': visits,
    }
    return render(request, 'core/user_history.html', context)
