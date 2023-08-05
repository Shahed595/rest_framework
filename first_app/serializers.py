from rest_framework import serializers
from . import models

        
class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
        
class StudentSerializers(serializers.ModelSerializer):
    course = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.StudentData
        fields = '__all__'