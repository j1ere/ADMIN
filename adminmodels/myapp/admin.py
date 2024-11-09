from django.contrib import admin
from .models import Book

#register models here
#using ModelAdmin class
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'publish_date') #columns to show in admin 
    search_fields=('title', 'author') #add search functionality
    list_filter=('publish_date',) #filter by , as a tuple

admin.site.register(Book,BookAdmin)