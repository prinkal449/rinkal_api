from rest_framework import serializers
from .models import *

class DataConverter(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
        field = ('first_name', 'email', 'password')
