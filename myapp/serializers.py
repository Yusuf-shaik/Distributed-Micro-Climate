from rest_framework import serializers
from .models import Conditions

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = ('myId', 'location','temperature', 'humidity', 'windspeed', 'percipitation')
