from django.contrib import admin
from .models import Forum, Messages, Category, User

"""
This module is responsible for registering the models in the Django admin site.

The models being registered are:
- User
- Forum
- Messages
- Category
"""

admin.site.register(User)
admin.site.register(Forum)
admin.site.register(Messages)
admin.site.register(Category)
