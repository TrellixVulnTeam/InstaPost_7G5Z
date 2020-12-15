from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    exclude = ('slug',)
    summernote_fields = ('content',)
    # list_display_links=('id','title',) #if needed turn this into a class. Refer stack overflow
    search_fields=('title',)
    list_per_page = 25
    summernote_fields = ('content',)



admin.site.register(BlogPost, BlogPostAdmin)
