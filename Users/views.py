from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Users.models import User
from Users.serializers import UserSerializer
from Users.task import users_email


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer_class = UserSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        fecha_envio_correo = datetime.now() + timedelta(seconds=10)
        users_email.apply_async(
            args=[request.user.email],
            eta=fecha_envio_correo
        )
        serializer = self.get_serializer_class()
        serialized = serializer(data=request.data)
        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)

        serialized.save()
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)