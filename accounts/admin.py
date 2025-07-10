from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'visits', 'last_visit')
    list_filter = ('last_visit',)
    search_fields = ('user__username', 'user__email')
