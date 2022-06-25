from rest_framework import serializers
from resaneh.models import Resaneh
from .models import *

class ResanehSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resaneh
        # fields = "__all__"
        fields = ("id","name", "owner", "category")

class AdVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdVideo
        fields = "__all__"
        # fields = ("name", "owner", "category")

class AdBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBox
        fields = "__all__"


class AdEventSerializer(serializers.ModelSerializer):
    # def get_media(self,obj):
    #     return obj.media.name
    #
    # def get_resanehs(self,obj):
    #     dicts = {}
    #     resaneh = obj.resaneh.all()
    #     for i in resaneh:
    #         dicts[i.id] = i.name
    #
    #     return dicts
    #
    #
    # media = serializers.SerializerMethodField('get_media',read_only=True)
    # resaneh = serializers.SerializerMethodField('get_resanehs',read_only=True)

    class Meta:
        model = AdEvent
        fields = "__all__"

class AdConnectionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdConnectionLog
        fields = "__all__"


class AdApplicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdApplicationLog
        fields = "__all__"


class AdVideoLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdVideoLog
        fields = "__all__"


class AdVideoCounterLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdVideoCounterLog
        fields = "__all__"
