from django.contrib import admin
from .models import (Publisher, Book, Store)

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
