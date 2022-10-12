from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404
from querys import StandarQuerys
from .models import Users
from exceptions import GetException

class Create_All_View(APIView):

    def get(self, request):
        return Response(UserSerializer(Users.objects.all(), many=True).data,200)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response(UserSerializer(user).data,201)
        else:
            return Response(serializer.errors,400)

    def handle_exception(self, exc):
        return GetException(exc)

class Detail_Mod_Delete_View(APIView):

    def get(self, request, UUID):
        user = get_object_or_404(Users, UUID = UUID)
        return Response(UserSerializer(user).data,200)

    def patch(self, request, UUID):
        user = get_object_or_404(Users, UUID = UUID)
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(user,serializer.validated_data)
            return Response(UserSerializer(user).data,200)
        else:
            return Response(serializer.errors,400)

    def delete(self, request, UUID):
        user = get_object_or_404(Users, UUID = UUID)
        data = UserSerializer(user).data
        user.delete()
        return Response(data,200)

    def handle_exception(self, exc):
        return GetException(exc)
