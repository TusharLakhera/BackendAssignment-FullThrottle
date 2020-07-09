from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import User,ActivityPeriod
from . serializers import UserSerializer,ActivityPeriodSerializer
from rest_framework import generics

class UserApi(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ActivityPeriodApi(generics.ListCreateAPIView):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodSerializer

# Create your views here.
# class MemberList(APIView):

# 	def get(self,request):
# 		members1=members.objects.all()
# 		serializer=memberserializer(members1,many=True)
# 		return Response(serializer.data)

# 	def post(self,request):
# 		data=request.data
# 		serializer=memberserializer(data=data,many=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data,status=201)
# 		return Response(serializer.errors,status=400)
	
# 	def get_object(self,id):
# 		try:
# 			return members.objects.get(id=id)
# 		except members.DoesNotExist as e:
# 			return Response({"error: object not found"},status=404)

# 	def put(self,request,id=None):
# 		data=request.data
# 		instance=self.get_object(id)
# 		serializer=memberserializer(instance,data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data,status=200)
	
# 	def delete(self, request, id=None):
# 		instance=self.get_object(id)
# 		instance.delete()
# 		return Response(status=204)

		 