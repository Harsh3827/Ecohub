from django.urls import path
from . import views

urlpatterns = [
    path('', views.TipListView.as_view(), name='tip-list'),
    path('tip/<int:pk>/', views.TipDetailView.as_view(), name='tip-detail'),
    path('tip/new/', views.TipCreateView.as_view(), name='tip-create'),
    path('tip/<int:pk>/edit/', views.TipUpdateView.as_view(), name='tip-update'),
    path('tip/<int:pk>/delete/', views.TipDeleteView.as_view(), name='tip-delete'),
] 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TipListView.as_view(), name='tip-list'),
    path('<int:pk>/', views.TipDetailView.as_view(), name='tip-detail'),
    path('create/', views.TipCreateView.as_view(), name='tip-create'),
    path('<int:pk>/update/', views.TipUpdateView.as_view(), name='tip-update'),
    path('<int:pk>/delete/', views.TipDeleteView.as_view(), name='tip-delete'),
]
