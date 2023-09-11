from django.forms import ModelForm
from .models import Forum, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
        #exclude = ['is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions', 'first_name', 'last_name']

