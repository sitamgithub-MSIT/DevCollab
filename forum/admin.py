from django.contrib import admin
from .models import Forum, Messages, Category, User


class MessagesInline(admin.TabularInline):
    """
    Inline admin class for displaying and editing Messages model in the admin interface.

    This class defines the behavior and appearance of the Messages model when displayed as an inline
    in the admin interface. It inherits from the `admin.TabularInline` class provided by Django.

    Attributes:
        model (Model): The Messages model to be displayed and edited inline.
        raw_id_fields (list): A list of fields that should be displayed as raw id fields in the admin interface.
                              Raw id fields are displayed as a text input instead of a select box, which can be
                              useful for models with a large number of instances.
    """

    model = Messages
    raw_id_fields = ["room"]


class ForumAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Forum model.

    This class defines the behavior and appearance of the Forum model in the Django admin interface.

    Attributes:
        list_display (list): A list of field names to display in the admin list view.
        list_filter (list): A list of field names to use for filtering in the admin list view.
        search_fields (list): A list of field names to use for searching in the admin list view.
        date_hierarchy (str): The name of the field to use for date-based drilldown navigation in the admin list view.
        ordering (list): A list of field names to use for ordering the objects in the admin list view.
        inlines (list): A list of inline classes to display in the admin detail view.

    """

    list_display = ["name", "host", "category", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "host__username", "category__name"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
    inlines = [MessagesInline]


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing Category model in the Django admin interface.
    """

    list_display = ["name"]
    search_fields = ["name"]


class MessagesAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Messages model.

    This class defines the display, filtering, search, and ordering options for the Messages model in the admin interface.

    Attributes:
        list_display (list): The fields to display in the admin list view.
        list_filter (list): The fields to use for filtering in the admin list view.
        search_fields (list): The fields to use for searching in the admin list view.
        date_hierarchy (str): The field to use for date-based navigation in the admin list view.
        ordering (list): The fields to use for ordering the records in the admin list view.
    """

    list_display = ["user", "room", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["user__username", "room__name"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]


class UserAdmin(admin.ModelAdmin):
    """
    Admin model for managing user data.

    Attributes:
        list_display (list): List of fields to display in the admin list view.
        search_fields (list): List of fields to enable search functionality in the admin list view.
        list_filter (list): List of fields to enable filtering in the admin list view.
        date_hierarchy (str): Field to enable date-based hierarchical navigation in the admin list view.
        ordering (list): List of fields to specify the default ordering of records in the admin list view.
    """

    list_display = ["username", "email", "is_staff", "is_active"]
    search_fields = ["username", "email"]
    list_filter = ["is_staff", "is_active"]
    date_hierarchy = "date_joined"
    ordering = ["-date_joined"]


"""
This module is responsible for registering the models in the Django admin site.

The models being registered are:
- User
- Forum
- Messages
- Category
"""

admin.site.register(User, UserAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Category, CategoryAdmin)
