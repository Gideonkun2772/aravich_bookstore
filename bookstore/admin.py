from django.contrib import admin
from .models import Book,Genre,Author,BookInstance,Language,Comment

# Register your models here.
class BookInstanceinline(admin.TabularInline):
    model=BookInstance
    extra=0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','language','display_genre']
    inlines=[BookInstanceinline]
    list_filter=['title','genre','author','pub_date']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=['book','id','status','due_back']
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields=['first_name','last_name',('date_of_birth','date_of_death')]
    list_display=['first_name','last_name','date_of_birth']

