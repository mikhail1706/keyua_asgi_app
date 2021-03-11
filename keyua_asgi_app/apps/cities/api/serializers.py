from rest_framework import serializers


class UpdateCitySerializer(serializers.Serializer):
    city_id = serializers.IntegerField()
    temperature = serializers.CharField()
    users = serializers.ListSerializer(child=serializers.IntegerField())