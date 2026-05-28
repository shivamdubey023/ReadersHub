from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Album(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    book_number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to='books/covers/')
    pdf_file = models.FileField(upload_to='books/pdfs/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.FloatField(default=0.0)


    def __str__(self):
        return self.title