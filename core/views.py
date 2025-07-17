from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from articles.models import Article
from tips.models import Tip
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            try:
                subject = f"Contact Form: {form.cleaned_data['subject']}"
                message = f"""
New contact form submission from EcoHub:

Name: {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}
Email: {form.cleaned_data['email']}
Phone: {form.cleaned_data['phone'] or 'Not provided'}
Subject: {form.cleaned_data['subject']}

Message:
{form.cleaned_data['message']}
                """
                
                # Send to admin (in production, this would be a real email)
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})

def search(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'all')
    category = request.GET.get('category', '')

    articles = []
    tips = []
    
    # Build filters for articles
    if search_type in ['articles', 'all']:
        article_filter = Q()
        if query:
            article_filter &= (Q(title__icontains=query) | Q(content__icontains=query))
        if category:
            article_filter &= Q(category=category)
        
        if article_filter:
            articles = list(Article.objects.filter(article_filter).order_by('-created_at'))
        elif not query and not category:
            # Show all articles if no filters applied
            articles = list(Article.objects.all().order_by('-created_at'))
    
    # Build filters for tips
    if search_type in ['tips', 'all']:
        tip_filter = Q()
        if query:
            tip_filter &= (Q(title__icontains=query) | Q(description__icontains=query))
        if category:
            tip_filter &= Q(category=category)
        
        if tip_filter:
            tips = list(Tip.objects.filter(tip_filter).order_by('-created_at'))
        elif not query and not category:
            # Show all tips if no filters applied
            tips = list(Tip.objects.all().order_by('-created_at'))

    context = {
        'query': query,
        'search_type': search_type,
        'category': category,
        'articles': articles,
        'tips': tips,
    }
    return render(request, 'core/search.html', context)

@login_required
def user_history(request):
    visits = request.session.get('visits', 0)
    context = {
        'visits': visits,
    }
    return render(request, 'core/user_history.html', context)
