from rest_framework import serializers
from .models import Proj_details, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    people = PersonSerializer(many=True)

    class Meta:
        model = Proj_details
        fields = '__all__'
