from rest_framework import serializers
from api.models.Log import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"