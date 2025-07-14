from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Article, Comment, Favorite
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Your article has been published successfully!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Your article has been updated successfully!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Article deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('article-detail', pk=article.pk)
        else:
            messages.error(request, 'Please correct the errors in your comment.')
    else:
        form = CommentForm()
    return render(request, 'articles/add_comment.html', {'form': form, 'article': article})

@login_required
def toggle_favorite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        article=article
    )
    
    if not created:
        favorite.delete()
        is_favorited = False
        messages.success(request, 'Article removed from favorites.')
    else:
        is_favorited = True
        messages.success(request, 'Article added to favorites!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'is_favorited': is_favorited,
            'favorites_count': article.favorite_set.count()
        })
    
    return redirect('article-detail', pk=article.pk)
