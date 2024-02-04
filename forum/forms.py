from django.forms import ModelForm
from .models import Forum, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    """
    A custom user creation form that extends the UserCreationForm class.

    This form is used for creating new user accounts with additional fields such as name, username, email, and passwords.

    Attributes:
        model (User): The user model to be used for creating new user accounts.
        fields (list): The fields to be included in the form for user input.

    """

    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]


class ForumForm(ModelForm):
    """
    A form for creating or updating a forum.

    Inherits from ModelForm and is used to generate HTML forms
    for the Forum model. It includes all fields of the Forum model
    except for 'host' and 'participants'.

    Attributes:
        model (class): The model class associated with the form.
        fields (list): The fields to include in the form.
        exclude (list): The fields to exclude from the form.
    """

    class Meta:
        model = Forum
        fields = "__all__"
        exclude = ["host", "participants"]


class UserForm(ModelForm):
    """
    Form for creating or updating a user.

    Attributes:
        model (Model): The model class associated with the form.
        fields (list): The fields to include in the form.

    """

    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
        # exclude = ['is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions', 'first_name', 'last_name']
