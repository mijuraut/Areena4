# game/serializers.py
from rest_framework import serializers
from .models import Gladiator


class GladiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gladiator
        fields = '__all__'
