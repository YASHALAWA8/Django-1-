from django.contrib import admin
from .models import OtherText, Comment

from django.contrib import admin

admin.site.site_title = "<your_title>"
admin.site.site_header = "<your_header>"
admin.site.index_title = "<your_index_title>"


@admin.register(OtherText)
class OtherTextAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active = True)