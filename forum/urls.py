from django.urls import path
from forum import views

"""
URL patterns for the forum application.

This list defines the mapping between URL patterns and corresponding view functions.
"""

# Set the urlpatterns variable to a list of paths.
urlpatterns = [
    path("", views.homepageview, name="homepageview"),
    path("topic/<str:pk>/", views.topicpageview, name="topicpageview"),
    path("profile/<str:pk>/", views.profilepageview, name="profilepageview"),
    path("create-topic/", views.createtopicview, name="createtopicview"),
    path("update-topic/<str:pk>/", views.updatetopicview, name="updatetopicview"),
    path("delete-topic/<str:pk>/", views.deletetopicview, name="deletetopicview"),
    path("delete-message/<str:pk>/", views.deletemessageview, name="deletemessageview"),
    path("update-user/", views.updateuserview, name="updateuserview"),
    path("category/", views.categorypageview, name="categorypageview"),
    path("activity/", views.activitypageview, name="activitypageview"),
    path("login/", views.loginpageview, name="loginpageview"),
    path("logout/", views.logoutpageview, name="logoutpageview"),
    path("register/", views.registerpageview, name="registerpageview"),
]
