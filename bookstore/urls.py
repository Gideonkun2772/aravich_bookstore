from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#create your urls here
app_name='bookstore'

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/',views.BookListView.as_view(),name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list',views.AuthorListView.as_view(),name='auther_list'),
    path('author_detail/<int:pk>',views.AuthorDetail.as_view(),name='author_detail')
]

