from django.forms import ModelForm
from Vendor.models import *

"""To create book"""
class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=['book_name','category','author','pages','price','pub_date']

    def clean(self):
        print("inside clean")
        cleaned_data=super().clean()
        book=cleaned_data.get('book_name')
        ob=Book.objects.filter(book_name=book)
        if(ob):
            msg="Book name exists"
            self.add_error('book_name',msg)



"""To create category"""

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=['category_name']

    def clean(self):
        print("inside clean")
        cleaned_data=super().clean()
        category=cleaned_data.get("category_name")
        obj=Category.objects.filter(category_name=category)
        if(obj):
            msg="Category already exists"
            self.add_error("category_name",msg)

"""To create author"""

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=['author_name']

    def clean(self):
        print("inside clean")
        cleaned_data=super().clean()
        name=cleaned_data.get("author_name")
        ob=Author.objects.filter(author_name=name)
        print("query executed")
        if(ob):
            msg="Author name exists"
            self.add_error("author_name",msg)
            print("Error")

"""To update book"""

class UpdateBook(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
    def clean(self):
        pass

"""To update author"""

class UpdateAuthor(ModelForm):
    class Meta:
        model=Author
        fields="__all__"
        def clean(self):
            pass

class UpdateCategory(ModelForm):
    class Meta:
        model=Category
        fields=['category_name']
        def clean(self):
            pass

class SearchBook(ModelForm):
    class Meta:
        model=Book
        fields=['book_name']

    def clean(self):
            pass
