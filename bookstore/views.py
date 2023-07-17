from django.shortcuts import render
from .models import Book,Author,BookInstance
from django.views import generic
from django.views.generic import ListView,DetailView
from django.http import Http404

#create your views here

def index(request):
    num_books=Book.objects.all().count()
    bookinstances=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.all().count()
    context={
        'num_books':num_books,
        'bookinstances':bookinstances,
        'num_authors':num_authors
        
    }
    return render(request,'bookstore/index.html',context=context)
class BookListView(generic.ListView):
    model=Book
    context_object_name='Books'
    template_name='bookstore/book_list.html'
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model=Book
    template_name='bookstore/book_detail.html'
    def book_detail(request,pk):
        try:
            book=Book.objects.get(pk=pk)
        except Book.doesnotexist:
            raise Http404('book does not exist')
        return render(request,'bookstore/book_detail.html',{'book':book})
    
class AuthorListView(generic.ListView):
    model=Author
    context_object_name='Author_list'
    template_name='bookstore/author_list.html'
    def get_queryset(self):
        return Author.objects.all()

class AuthorDetail(generic.DetailView):
    model=Author
    template_name='bookstore/author_detail.html'
    def auther_detail(request,pk):
        try:
            auther=Author.objects.get(pk=pk)
        except Author.doesnotexist:
            raise Http404('Author does not exist')
        return render(request,'bookstore/author_detail.html',{'author':author})

    
