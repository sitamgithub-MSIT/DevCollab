from django.shortcuts import redirect, render
from .models import Forum, Category, Messages, User
from .forms import ForumForm, UserForm, MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginpageview(request):
    """
    View function for rendering the login page and handling user authentication.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    page = "loginpageview"

    # Redirect to the homepage if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("homepageview")

    # If the request method is POST, authenticate the user
    if request.method == "POST":

        # Get the username and password from the request
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        # Check if the user exists else display an error message
        try:
            user = User.objects.get(email=email)

        except Exception:
            messages.info(request, "User does not exist!")

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        # If the user is not None, log in the user and redirect to the homepage
        if user is not None:
            login(request, user)
            return redirect("homepageview")
        
        # Else display an error message
        else:
            messages.info(request, "Username or Password is incorrect")

    # Render the login page with the context
    context = {"page": page}
    return render(request, "forum/user_authentication.html", context)


def logoutpageview(request):
    """
    Logs out the user and redirects to the homepage view.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect response to the homepage view.
    """

    # Log out the user and redirect to the homepage
    logout(request)
    return redirect("homepageview")


def registerpageview(request):
    """
    View function for registering a new user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = MyUserCreationForm()

    # if request.user.is_authenticated:
    #     return redirect("homepageview")

    # If the request method is POST, register the user
    if request.method == "POST":
        
        form = MyUserCreationForm(request.POST)

        # If the form is valid, save the user and log in the user
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # Log in the user and redirect to the login page
            login(request, user)
            return redirect("homepageview")
        
        # Else display an error message
        else:
            messages.error(request, "An error occured during registration")

    # Render the register page with the context
    context = {"form": form}
    return render(request, "forum/user_authentication.html", context)


def homepageview(request):
    """
    View function for rendering the homepage of the forum.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered home.html template.
    """

    # Get the query parameter from the URL if it exists
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    # Filter topics based on the query parameter
    topics = Forum.objects.filter(
        Q(category__name__contains=q)
        | Q(name__contains=q)
        | Q(description__contains=q)
        | Q(host__username__contains=q)
    )

    # Get the first 5 categories from the database and the count of topics in the forum
    categories = Category.objects.all()[:5]
    topic_count = topics.count()
    room_messages = Messages.objects.filter(
        Q(room__category__name__contains=q) | Q(message__contains=q)
    )[:5]

    # Context for rendering the homepage
    context = {
        "topics": topics,
        "categories": categories,
        "topic_count": topic_count,
        "room_messages": room_messages,
    }

    # Render the homepage with the context
    return render(request, "forum/home.html", context)


def profilepageview(request, pk):
    """
    View function to render the user profile page.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the user.

    Returns:
        HttpResponse: The HTTP response object containing the rendered user profile page.
    """

    # Get the user object from the database
    user = User.objects.get(id=pk)
    topics = user.forum_set.all()
    room_messages = user.messages_set.all()
    categories = Category.objects.all()
    topics_count = topics.count()

    # Context for rendering the user profile page
    context = {
        "user": user,
        "topics": topics,
        "topics_count": topics_count,
        "room_messages": room_messages,
        "categories": categories,
    }

    # Render the user profile page with the context
    return render(request, "forum/user_profile.html", context)


# @login_required(login_url="loginpageview")
def topicpageview(request, pk):
    """
    View function for displaying a topic page.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the topic.

    Returns:
        HttpResponse: The HTTP response object containing the rendered topic page.
    """

    # Get the topic object from the database
    topic = Forum.objects.get(id=pk)
    room_messages = topic.messages_set.all()
    participants = topic.participants.all()

    # If the request method is POST, create a new message object and add the user to the participants list
    if request.method == "POST":
        message = Messages.objects.create(
            user=request.user, room=topic, message=request.POST.get("body")
        )
        topic.participants.add(request.user)

        # Redirect to the topic page
        return redirect("topicpageview", pk=topic.id)

    # Context for rendering the topic page
    context = {
        "topic": topic,
        "room_messages": room_messages,
        "participants": participants,
    }

    # Render the topic page with the context
    return render(request, "forum/topic.html", context)


@login_required(login_url="loginpageview")
def createtopicview(request):
    """
    View function for creating a new topic in the forum.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Create a new form object
    form = ForumForm()
    categories = Category.objects.all()

    # If the request method is POST, process the form data
    if request.method == "POST":

        # Get the category object
        category_name = request.POST.get("topic")
        category, created = Category.objects.get_or_create(name=category_name)

        # Create a new topic object with the form data
        Forum.objects.create(
            host=request.user,
            category=category,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )

        # Redirect to the homepage
        return redirect("homepageview")

    # Context for rendering the create topic template
    context = {"form": form, "categories": categories}

    # Render the create topic template with the form object
    return render(request, "forum/create_topic.html", context)


@login_required(login_url="loginpageview")
def updatetopicview(request, pk):
    """
    View function to update a topic in the forum.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the topic to be updated.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Get the topic object from the database
    topic = Forum.objects.get(id=pk)
    form = ForumForm(instance=topic)
    categories = Category.objects.all()

    # Check if the user is the owner of the topic
    if request.user != topic.host:
        return redirect("homepageview")

    # If the request method is POST, process the form data
    if request.method == "POST":

        # Get the category name from the request and create a new category object if it does not exist
        category_name = request.POST.get("topic")
        category, created = Category.objects.get_or_create(name=category_name)

        # Update the topic object with the new data
        topic.name = request.POST.get("name")
        topic.category = category
        topic.description = request.POST.get("description")
        topic.save()

        # Redirect to the homepage
        return redirect("homepageview")

    # Context for rendering the update topic template
    context = {"form": form, "topic": topic, "categories": categories}

    # Render the update topic template with context
    return render(request, "forum/create_topic.html", context)


@login_required(login_url="loginpageview")
def deletetopicview(request, pk):
    """
    View function to delete a topic.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the topic to be deleted.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Get the topic object from the database
    topic = Forum.objects.get(id=pk)

    # Check if the user is the owner of the topic
    if request.user != topic.host:
        return redirect("homepageview")

    # If the request method is POST, delete the topic and redirect to the homepage
    if request.method == "POST":
        topic.delete()
        return redirect("homepageview")

    # Render the delete topic template with the topic object
    return render(request, "forum/delete_topic.html", {"obj": topic})


@login_required(login_url="loginpageview")
def deletemessageview(request, pk):
    """
    View function to delete a message.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the message to be deleted.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Get the message object from the database
    message = Messages.objects.get(id=pk)

    # Check if the user is the owner of the message
    if request.user != message.user:
        return redirect("homepageview")

    # If the request method is POST, delete the message and redirect to the homepage
    if request.method == "POST":
        message.delete()
        return redirect("homepageview")

    # Render the delete message template with the message object
    return render(request, "forum/delete_topic.html", {"obj": message})


@login_required(login_url="loginpageview")
def updateuserview(request):
    """
    View function to update the user profile.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Get the user object from the request
    user = request.user
    form = UserForm(instance=user)

    # If the request method is POST, process the form data
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)

        # If the form is valid, save the data and redirect to the user profile page
        if form.is_valid():
            form.save()
            return redirect("profilepageview", pk=user.id)

    # Render the form with the user's data
    context = {"form": form}
    return render(request, "forum/edit_user_profile.html", context)


def categorypageview(request):
    """
    View function for rendering the category page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered category page.
    """

    # Get the query parameter from the URL if it exists
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    # Filter categories based on the query parameter
    categories = Category.objects.filter(Q(name__contains=q))

    # Return the rendered template with the context
    context = {"categories": categories}
    return render(request, "forum/categorypageview.html", context)


def activitypageview(request):
    """
    View function for the activity page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """

    # Get all messages from the database
    room_messages = Messages.objects.all()

    # Return the rendered template with the context
    context = {"room_messages": room_messages}
    return render(request, "forum/activitypageview.html", context)
