from rest_framework import serializers
from tours.models import Months, TourItem, Tourists


class TourItemSerializer(serializers.ModelSerializer):
    dateRange = serializers.CharField(source='date_range')
    spotsLeft = serializers.IntegerField(source='spots_left')
    spotsTotal = serializers.IntegerField(source='spots_total')

    class Meta:
        model = TourItem
        fields = ['id', 'dateRange', 'spotsTotal', 'price', 'spotsLeft', 'created_at']


class TourSerializer(serializers.ModelSerializer):
    items = TourItemSerializer(many=True, read_only=True)

    class Meta:
        model = Months
        fields = ['id', 'type', 'title', 'items']




class TouristsSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = Tourists
        fields = ['firstName', 'lastName', 'status']

class TourItemUserSerializer(serializers.ModelSerializer):
    dateRange = serializers.CharField(source='date_range')
    spotsLeft = serializers.IntegerField(source='spots_left')
    spotsTotal = serializers.IntegerField(source='spots_total')
    tourists = TouristsSerializer(many=True, read_only=True)

    class Meta:
        model = TourItem
        fields = ['id', 'dateRange', 'spotsTotal', 'price', 'spotsLeft', 'created_at', 'tourists']