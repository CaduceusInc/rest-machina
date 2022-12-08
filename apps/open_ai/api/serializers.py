from abc import ABC

from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    n = serializers.IntegerField()
    size = serializers.IntegerField()
    response_format = serializers.CharField()

    def create(self, validated_data):
        return validated_data

    class Meta:
        fields = ('image', 'n', 'size', 'response_format')
        ordering = ('image',)


class ImageFromPromptSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    n = serializers.IntegerField()
    size = serializers.CharField()
    response_format = serializers.CharField()

    def create(self, validated_data):
        return validated_data

    class Meta:
        fields = ('prompt', 'n', 'size', 'response_format')
