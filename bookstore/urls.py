

from django.urls import path
from . import views

#create your urls here

app_name='bookstore'

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/',views.BookListView.as_view(),name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    #path('author_list',views.AuthorListView.as_view(),name='author_list'),
    path('profile_detail/<int:pk>',views.ProfileDetail.as_view(),name='profile_detail')
]

