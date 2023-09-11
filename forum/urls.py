from django.urls import path
from forum import views


urlpatterns = [
    path('' , views.homepageview, name='homepageview'),
    path('topic/<str:pk>/', views.topicpageview, name='topicpageview'),
    path('profile/<str:pk>/', views.profilepageview, name='profilepageview'),

    path('create-topic/', views.createtopicview, name='createtopicview'),
    path('update-topic/<str:pk>/', views.updatetopicview, name='updatetopicview'),
    path('delete-topic/<str:pk>/', views.deletetopicview, name='deletetopicview'),   
    path('delete-message/<str:pk>/', views.deletemessageview, name='deletemessageview'),
    path('update-user/', views.updateuserview, name='updateuserview'),
    path('category/', views.categorypageview, name='categorypageview'),
    path('activity/', views.activitypageview, name='activitypageview'),


    path('login/', views.loginpageview, name='loginpageview'),
    path('logout/', views.logoutpageview, name='logoutpageview'),
    path('register/', views.registerpageview, name='registerpageview'),
]