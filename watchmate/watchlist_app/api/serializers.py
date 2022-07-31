from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from watchmate.watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_name(self, object):
        return len(object.name) 

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        