from lib2to3.pgen2.token import NUMBER
from rest_framework import serializers
from numbers_api.models import Number

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['id', 'number']