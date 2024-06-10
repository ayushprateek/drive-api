from rest_framework import serializers


class TravelAssistantSerializer(serializers.Serializer):
    query = serializers.CharField(required=True)


