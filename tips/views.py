from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Tip
from .forms import TipForm

# Create your views here.

class TipListView(ListView):
    model = Tip
    template_name = 'tips/tip_list.html'
    context_object_name = 'tips'
    ordering = ['-created_at']

class TipDetailView(DetailView):
    model = Tip
    template_name = 'tips/tip_detail.html'
    context_object_name = 'tip'

class TipCreateView(LoginRequiredMixin, CreateView):
    model = Tip
    form_class = TipForm
    template_name = 'tips/tip_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Your tip has been shared successfully!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class TipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tip
    form_class = TipForm
    template_name = 'tips/tip_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Your tip has been updated successfully!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def test_func(self):
        tip = self.get_object()
        return self.request.user == tip.user

class TipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tip
    template_name = 'tips/tip_confirm_delete.html'
    success_url = reverse_lazy('tip-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Tip deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        tip = self.get_object()
        return self.request.user == tip.user
