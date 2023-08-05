from django.shortcuts import render
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

from rest_framework import generics


class StudentListCreateView(generics.ListCreateAPIView):#get,post
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializers


class StudentDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentData.objects.all()
    serializer_class = serializers.StudentSerializers
# class StudentView(APIView):
#     def get(self, request, format=None):
#         studentData = models.StudentData.objects.all()
#         serializer = serializers.StudentSerializers(studentData, many=True)
#         # serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serializers.StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class StudentDetailView(APIView):
#     def get(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         serializer = serializers.StudentSerializers(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = models.StudentData.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
