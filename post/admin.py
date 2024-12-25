from django.contrib import admin
from .models import Post

from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'images']

    def images(self, obj):
        return format_html(
            f'''<a href="{obj.photo.url}" target="_blank">
                        <img src="{obj.photo.url}" alt="image" width="150" height="100" 
                             style="object-fit: cover;"/>
                    </a>'''
        )

    def img(self, obj):
        return format_html(
            f'''<a href="{obj.photo.url}" target="_blank">
                          <img src="{obj.photo.url}" alt="image" width="150" height="100"
                               style="object-fit: cover;"/>
                      </a>'''
        )

