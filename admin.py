from django.contrib import admin
from .models import Article,Category,Tags
admin.site.register(Tags)
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','category','title','user','views','top','created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    fk_fields = ['category']
    list_display_links = ['id','title']
    search_fields = ['title']
    list_filter = ['user']
    admin.site.site_header = '知识内容管理后台'
    admin.site.site_title = '测试知识内容平台'

admin.site.register(Category)