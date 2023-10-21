from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your models here.
fs=FileSystemStorage(location="/aravich_bookstore/")
class Genre(models.Model):
    genre=models.CharField(max_length=35)
    
    def __str__(self):
        return self.genre
    
class Book(models.Model):
    image=models.ImageField(storage=fs)
    title=models.CharField(max_length=64)
    pub_date=models.DateField()
    author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    isbn=models.CharField(max_length=64,unique=True)
    summery=models.TextField(max_length=200)
    language=models.ForeignKey('Language', on_delete=models.SET_NULL,null=True)
    genre=models.ManyToManyField(Genre, )
    
    
    class Meta:
        ordering=('pub_date',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.genre for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
    
class Comment(models.Model):
    book=models.ForeignKey(Book, related_name='comments' ,on_delete=models.CASCADE)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class meta:
        ordering=('-pub_date')
        
    def __str__(self):
        return ' %s - %s' %(self.book.title, self.body)
    
    
class Language(models.Model):
    language=models.CharField(max_length=40)
    
    def __str__(self):
        return self.language
    


import uuid
class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    loan_status=(
        ('a','Available'),
        ('m','Maintainance'),
        ('b','Borrowed'),
        ('r','reserved')
    )
    status=models.CharField(max_length=10,choices=loan_status,default='a')
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    
    due_back=models.DateField(null=True,blank=True)
    
    
    class Mete:
        ordering=('status')
    
    def __str__(self):
        return f'{self.book}'

class Profile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio=models.TextField()
    date_of_birth=models.DateField()
    date_of_death=models.DateField()
    
    class Meta:
        ordering=('-name',)
    
    def __str__(self):
        return self.name.username
    
    '''def get_absolute_url(self):
        return reverse("auther_detail", kwargs={"pk": self.pk})'''
    
    
    
    
    
    
    
    
    
    
     
    
