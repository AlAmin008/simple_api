from django.shortcuts import render
from .models import employeetable
from .serializers import employeeserializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import action

# Create your views here.
class employeeview(APIView):
    def get(self, request):
        employee = employeetable.objects.all()
        serializer = employeeserializer(employee, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        newemployee = employeeserializer(data=request.data)
        if newemployee.is_valid():
            try:
                newemployee.save()
                return Response(newemployee.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(newemployee.errors, status=status.HTTP_400_BAD_REQUEST)

    
        
class employeedetailview(APIView):
    def get(self, request, id):
        try:
            employee = employeetable.objects.get(id = id)
        except employeetable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = employeeserializer(employee)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            existingemployee = employeetable.objects.get(id=id)
        except employeetable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = employeeserializer(existingemployee, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            existingemployee = employeetable.objects.get(id=id)
            existingemployee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except employeetable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)