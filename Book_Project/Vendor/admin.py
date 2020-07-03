from django.contrib import admin
from Vendor.models import *
# Register your models here.
admin.site.register(Category),
admin.site.register(Author),
admin.site.register(Book)