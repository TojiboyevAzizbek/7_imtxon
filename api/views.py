from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from main import models
from . import serializers



@api_view(['POST'])
def staff_create(request):
    f_name = request.data.get('f_name')
    l_name = request.data.get('l_name')
    status = request.data.get('status')
    tel_num = request.data.get('tel_num')
    email = request.data.get('email')
    if f_name and l_name and status and tel_num and email:
        models.Staff.objects.create(
            f_name = f_name,
            l_name = l_name,
            status = status,
            tel_num = tel_num,
            email = email
        )
        return Response({'status':HTTP_200_OK})
    return Response({'status':HTTP_400_BAD_REQUEST})



@api_view(['GET'])
def staff_list(request):
    staff = models.Staff.objects.all()
    staffs = serializers.StaffSerializers(staff, many=True)
    return Response(staffs.data)


@api_view(['POST'])
def attendance_create(request, id):
    staff = models.Staff.objects.get(id = id)
    if staff:
        models.Attendance.objects.create(
            staff = staff
        )
        return Response({'status':HTTP_200_OK})