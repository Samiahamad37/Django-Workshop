from rest_framework import serializers
from.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'



class SubjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()