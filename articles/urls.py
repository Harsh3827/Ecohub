from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('article/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('favorites/', views.my_favorites, name='my-favorites'),
    path('<int:pk>/favorite/', views.toggle_favorite, name='toggle-favorite'),
]