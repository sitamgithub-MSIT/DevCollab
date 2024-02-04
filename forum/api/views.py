from rest_framework.decorators import api_view
from rest_framework.response import Response
from forum.models import Forum
from .serializers import ForumSerializer


@api_view(["GET"])
def getroutes(request):
    """
    Returns a list of available routes in the API.

    Returns:
        Response: A response containing a list of available routes.
    """
    routes = [
        "GET /api",
        "GET /api/rooms",
        "GET /api/rooms/<str:pk>",
    ]
    return Response(routes)


@api_view(["GET"])
def getrooms(request):
    """
    Retrieve all rooms from the database and serialize them using ForumSerializer.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The serialized data of all rooms.
    """
    forums = Forum.objects.all()
    serializer = ForumSerializer(forums, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getroom(request, pk):
    """
    Retrieve a specific forum room by its ID.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The ID of the forum room to retrieve.

    Returns:
        Response: The serialized data of the retrieved forum room.
    """
    forum = Forum.objects.get(id=pk)
    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)
