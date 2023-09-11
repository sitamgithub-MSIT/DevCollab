from django.contrib import admin
from .models import Forum, Messages, Category, User
# Register your models here.

admin.site.register(User)
admin.site.register(Forum)
admin.site.register(Messages)
admin.site.register(Category)
