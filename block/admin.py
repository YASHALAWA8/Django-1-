from django.contrib import admin
from .models import Article

from django.contrib import admin

admin.site.site_title = "<your_title>"
admin.site.site_header = "<your_header>"
admin.site.index_title = "<your_index_title>"


@admin.register(Article)
class ArticalAdmin(admin.ModelAdmin):
    pass
