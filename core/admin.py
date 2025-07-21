from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'stars', 'location', 'date')
    list_filter = ('section', 'stars', 'date')
    search_fields = ('name', 'review_content', 'location', 'badge_text')