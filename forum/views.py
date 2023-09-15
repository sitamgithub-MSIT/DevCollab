from django.shortcuts import redirect, render
from .models import Forum, Category, Messages, User
from .forms import ForumForm, UserForm, MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginpageview(request):
    page = "loginpageview"

    if request.user.is_authenticated:
        return redirect("homepageview")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

        except Exception:
            messages.info(request, "User does not exist!")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepageview")
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {"page": page}
    return render(request, "forum/user_authentication.html", context)


def logoutpageview(request):
    logout(request)
    return redirect("homepageview")


def registerpageview(request):
    form = MyUserCreationForm()

    # if request.user.is_authenticated:
    #     return redirect("homepageview")

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect("loginpageview")
        else:
            messages.error(request, "An error occured during registration")

    context = {"form": form}
    return render(request, "forum/user_authentication.html", context)


def homepageview(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    topics = Forum.objects.filter(
        Q(category__name__contains=q)
        | Q(name__contains=q)
        | Q(description__contains=q)
        | Q(host__username__contains=q)
    )

    categories = Category.objects.all()[:5]
    topic_count = topics.count()
    room_messages = Messages.objects.filter(
        Q(room__category__name__contains=q) | Q(message__contains=q)
    )[:5]

    context = {
        "topics": topics,
        "categories": categories,
        "topic_count": topic_count,
        "room_messages": room_messages,
    }

    return render(request, "forum/home.html", context)


def profilepageview(request, pk):
    user = User.objects.get(id=pk)
    topics = user.forum_set.all()
    room_messages = user.messages_set.all()
    categories = Category.objects.all()
    topics_count = topics.count()

    context = {
        "user": user,
        "topics": topics,
        "topics_count": topics_count,
        "room_messages": room_messages,
        "categories": categories,
    }

    return render(request, "forum/user_profile.html", context)

#@login_required(login_url="loginpageview")
def topicpageview(request, pk):
    topic = Forum.objects.get(id=pk)
    room_messages = topic.messages_set.all()
    participants = topic.participants.all()
        
    if request.method == "POST":
        message = Messages.objects.create(
            user=request.user, room=topic, message=request.POST.get("body")
        )
        topic.participants.add(request.user)

        return redirect("topicpageview", pk=topic.id)

    context = {
        "topic": topic,
        "room_messages": room_messages,
        "participants": participants,
    }

    return render(request, "forum/topic.html", context)


@login_required(login_url="loginpageview")
def createtopicview(request):
    form = ForumForm()
    categories = Category.objects.all()

    if request.method == "POST":
        category_name = request.POST.get("topic")
        category, created = Category.objects.get_or_create(name=category_name)

        Forum.objects.create(
            host=request.user,
            category=category,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        return redirect("homepageview")

    context = {"form": form, "categories": categories}

    return render(request, "forum/create_topic.html", context)


@login_required(login_url="loginpageview")
def updatetopicview(request, pk):
    topic = Forum.objects.get(id=pk)
    form = ForumForm(instance=topic)
    categories = Category.objects.all()

    if request.user != topic.host:
        return redirect("homepageview")

    if request.method == "POST":
        category_name = request.POST.get("topic")
        category, created = Category.objects.get_or_create(name=category_name)

        topic.name = request.POST.get("name")
        topic.category = category
        topic.description = request.POST.get("description")
        topic.save()
        return redirect("homepageview")

    context = {"form": form, "topic": topic, "categories": categories}

    return render(request, "forum/create_topic.html", context)


@login_required(login_url="loginpageview")
def deletetopicview(request, pk):
    topic = Forum.objects.get(id=pk)

    if request.user != topic.host:
        return redirect("homepageview")

    if request.method == "POST":
        topic.delete()
        return redirect("homepageview")

    return render(request, "forum/delete_topic.html", {"obj": topic})


@login_required(login_url="loginpageview")
def deletemessageview(request, pk):
    message = Messages.objects.get(id=pk)

    if request.user != message.user:
        return redirect("homepageview")

    if request.method == "POST":
        message.delete()
        return redirect("homepageview")

    return render(request, "forum/delete_topic.html", {"obj": message})


@login_required(login_url="loginpageview")
def updateuserview(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect("profilepageview", pk=user.id)

    context = {"form": form}
    return render(request, "forum/edit_user_profile.html", context)


def categorypageview(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    categories = Category.objects.filter(Q(name__contains=q))

    context = {"categories": categories}

    return render(request, "forum/categorypageview.html", context)

def activitypageview(request):


    room_messages = Messages.objects.all()
    context = {"room_messages": room_messages}

    return render(request, "forum/activitypageview.html", context)
