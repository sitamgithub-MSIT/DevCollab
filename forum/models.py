from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    Represents a user in the system.

    Attributes:
        name (str): The name of the user.
        username (str): The unique username of the user.
        email (str): The unique email address of the user.
        bio (str): The bio of the user.
        avatar (str): The path to the user's avatar image.
    """

    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(default="avatar.svg", null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Category(models.Model):
    """
    Represents a category in the forum.
    """

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Forum(models.Model):
    """
    Represents a forum in the application.

    Attributes:
        host (User): The user who created the forum.
        category (Category): The category to which the forum belongs.
        name (str): The name of the forum.
        participants (ManyToManyField): The users who are participating in the forum.
        description (str): The description of the forum.
        created_at (datetime): The date and time when the forum was created.
        updated_at (datetime): The date and time when the forum was last updated.
    """

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.name


class Messages(models.Model):
    """
    Represents a message in a forum room.

    Attributes:
        user (User): The user who posted the message.
        room (Forum): The forum room where the message is posted.
        message (str): The content of the message.
        created_at (datetime): The timestamp when the message was created.
        updated_at (datetime): The timestamp when the message was last updated.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Forum, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.message[:50]
