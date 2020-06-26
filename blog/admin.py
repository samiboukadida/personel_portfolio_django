from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_published']

    def make_published(self, request, queryset):
        updated = queryset.update(status=1)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "Mark selected blogs as published"


admin.site.register(Blog, BlogAdmin)