from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    genre=models.CharField(max_length=35)
    
    def __str__(self):
        return self.genre
    
class Book(models.Model):
    image=models.ImageField(upload_to="aravich_bookstore/")
    title=models.CharField(max_length=64)
    pub_date=models.DateField()
    author=models.ForeignKey('Author', on_delete=models.SET_NULL,null=True)
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
    book=models.ForeignKey(Book,on_delete=models.RESTRICT)
    
    due_back=models.DateField(null=True,blank=True)
    
    
    class Mete:
        ordering=('status')
    
    def __str__(self):
        return f'{self.book}'

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    date_of_birth=models.DateField()
    date_of_death=models.DateField()
    
    class Meta:
        ordering=('-first_name',)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
    def get_absolute_url(self):
        return reverse("auther_detail", kwargs={"pk": self.pk})
    
    
    
    
    
    
    
    
    
    
     
    
