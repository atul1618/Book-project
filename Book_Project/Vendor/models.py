from django.db import models

# Create your models here.
""""Category model for storing book category"""
class Category(models.Model):
    category_name=models.CharField(max_length=120)

    def __str__(self):
        return self.category_name

""""Author model for  author registration"""

class Author(models.Model):
    author_name=models.CharField(max_length=120)

    def __str__(self):
        return self.author_name

"""Model for storing book details"""

class Book(models.Model):
    book_name=models.CharField(max_length=120)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    pages=models.IntegerField(default=60)
    price=models.IntegerField(default=100)
    pub_date=models.DateField()

    def __str__(self):
        return self.book_name
