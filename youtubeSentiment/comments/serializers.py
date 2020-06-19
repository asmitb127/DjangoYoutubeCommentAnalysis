from rest_framework import serializers


class WordsSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
