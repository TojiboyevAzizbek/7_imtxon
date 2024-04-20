
from rest_framework import serializers
from main import models


class StaffSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Staff
        fields = '__all__'
        
        
class AttendanceSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Attendance
        fields = '__all__'
