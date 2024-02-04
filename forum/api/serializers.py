from rest_framework import serializers
from forum.models import Forum


class ForumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Forum model.
    """

    class Meta:
        model = Forum
        fields = "__all__"
