from rest_framework.decorators import api_view
from rest_framework.response import Response
from forum.models import Forum
from .serializers import ForumSerializer


@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/<str:pk>',
    ]
    return Response(routes)


@api_view(['GET'])
def getrooms(request):
    forums = Forum.objects.all()
    serializer = ForumSerializer(forums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getroom(request, pk):
    forum = Forum.objects.get(id=pk)
    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)

