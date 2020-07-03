from django.shortcuts import render, redirect
from Vendor.forms import *
# Create your views here.
""" To get Home page"""

def getHome(request):
    return render(request,"vendor/home/index.html")

"""To create category"""

def createcategory(request):
    categoryfrm=CategoryForm()
    template_name="vendor/category/category_create.html"
    context={}
    context['form']=categoryfrm
    if request.method=="POST":
        categorypost=CategoryForm(request.POST)
        if categorypost.is_valid():
            categorypost.save()
            return redirect("createbook")
        else:
            categorypost = CategoryForm(request.POST)
            template_name="vendor/category/category_create.html"
            context={}
            context['form']=categorypost
            return render(request, template_name, context)

    return render(request,template_name,context)

""""To list category"""

def listCategory(request):
    template_name="vendor/category/listcategory.html"
    obj=Category.objects.all()
    context={}
    context['viewcategory']=obj
    return render(request,template_name,context)

"""To view category"""

def viewCategory(request,pk):
    qs=Category.objects.get(id=pk)
    template_name="vendor/category/viewcategory.html"
    context={}
    context['category']=qs
    return render(request,template_name,context)

"""To delete category"""

def delCategory(request,pk):
    qs=Category.objects.get(id=pk).delete()
    context={}
    context['delcategory']=qs
    return redirect('listcategory')

"""To create author"""

def createauthor(request):
    authorfrm=AuthorForm()
    template_name="vendor/author/author_create.html"
    context={}
    context['form']=authorfrm
    if request.method=="POST":
        authorfrmpost=AuthorForm(request.POST)
        print("data posted")
        if authorfrmpost.is_valid():
            print("Posted")
            authorfrmpost.save()
            return redirect("createbook")
        else:
            authorfrmpost = AuthorForm(request.POST)
            template_name="vendor/author/author_create.html"
            context={}
            context['form']=authorfrmpost
            return render(request, template_name, context)

    return render(request, template_name, context)

"""To list authors"""

def listAuthor(request):
    template_name="vendor/author/list_author.html"
    data=Author.objects.all()
    context={}
    context['listauthor']=data
    return render(request,template_name,context)

"""To view author details"""

def viewAuthor(request,pk):
    qs=Author.objects.get(id=pk)
    template_name="vendor/author/viewauthor.html"
    context={}
    context['view']=qs
    return render(request,template_name,context)

"""To delete authors"""

def deleteauthor(request,pk):
    qs=Author.objects.get(id=pk).delete()
    context={}
    context['delauthor']=qs
    return redirect('listauthor')

"""To create book"""

def createBook(request):
    bookcreate=BookForm()
    template_name="vendor/books/book_create.html"
    context={}
    context['user']=bookcreate
    if request.method=="POST":
        bookcreatepost=BookForm(request.POST)
        if bookcreatepost.is_valid():
            bookcreatepost.save()
            return redirect("listbooks")
        else:
            bookcreatepost = BookForm(request.POST)
            template_name = "vendor/books/book_create.html"
            context = {}
            context['user'] = bookcreatepost
            return render(request, template_name, context)

    return render(request,template_name,context)

"""To list books"""

def listBooks(request):
    template_name="vendor/books/listbook.html"
    ob=Book.objects.all()
    context={}
    context['item']=ob
    return render(request,template_name,context)

"""To view books"""
def bookView(request,pk):
    # pk=primary key
    qs=Book.objects.get(id=pk)
    template_name="vendor/books/bookview.html"
    context={}
    context['book']=qs
    return render(request,template_name,context)


"""To delete books"""
def delBook(request,pk):
    qs=Book.objects.get(id=pk).delete()
    context={}
    context['delbook']=qs
    return redirect('listbooks')

"""To update books"""
def updateBook(request,pk):
    qs=Book.objects.get(id=pk)
    form=UpdateBook(instance=qs)
    # instance means which objects details we need is passed
    template_name="vendor/books/update.html"
    context={}
    context['bookupdate']=form
    if request.method=="POST":
        updatefrm=UpdateBook(request.POST)
        if updatefrm.is_valid():
            bookname=updatefrm.cleaned_data["book_name"]
            category=updatefrm.cleaned_data["category"]
            author=updatefrm.cleaned_data["author"]
            page=updatefrm.cleaned_data["pages"]
            price=updatefrm.cleaned_data["price"]
            date=updatefrm.cleaned_data["pub_date"]
            qs.book_name=bookname
            qs.category=category
            qs.author=author
            qs.pages=page
            qs.price=price
            qs.date=date
            qs.save()
            return redirect('listbooks')
    return render(request,template_name,context)

"""To update author"""
def updateAuthor(request,pk):
    qs=Author.objects.get(id=pk)
    form=UpdateAuthor(instance=qs)
    template_name="vendor/author/updateauthor.html"
    context={}
    context['authorupdate']=form
    if request.method=="POST":
        updateauth=UpdateAuthor(request.POST)
        if updateauth.is_valid():
            authname=updateauth.cleaned_data["author_name"]
            qs.author_name=authname
            qs.save()
            return redirect('listauthor')

    return render(request,template_name,context)


""""To update category"""

def updateCategory(request,pk):
    qs=Category.objects.get(id=pk)
    form=UpdateCategory(instance=qs)
    template_name="vendor/category/updatecategory.html"
    context={}
    context['category']=form
    if request.method=="POST":
        categoryfrm=UpdateCategory(request.POST)
        if categoryfrm.is_valid():
            ctgry=categoryfrm.cleaned_data['category_name']
            qs.category_name=ctgry
            qs.save()
            return redirect('listcategory')
    return render(request,template_name,context)

def searchBooks(request):
    booksearch=SearchBook()
    context={}
    context['search']=booksearch
    template_name="vendor/books/searchbooks.html"
    if request.method=="POST":
        search=SearchBook(request.POST)
        if search.is_valid():
            bookname=search.cleaned_data['book_name']
            qs=Book.objects.get(book_name=bookname)
            if(qs):
                print("Found")
                template_name = "vendor/books/bookview.html"
                context = {}
                context['book'] = qs
                return render(request,template_name,context)



    return render(request,template_name,context)