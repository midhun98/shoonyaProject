from rest_framework import serializers
from .models import Retreat, Booking


class RetreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retreat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
