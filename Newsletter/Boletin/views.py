from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, viewsets
from Boletin.models import Boletin, Votaciones
from Boletin.serializers import BoletinSerializer,VotacionesSerializer
from rest_framework.decorators import api_view, action
from django.core.mail import send_mail
from Boletin.task import boletin_email


class VotacionesViewSet(viewsets.ModelViewSet):

    queryset = Votaciones.objects.all()
    serializer_class = VotacionesSerializer

    def list(self, request):
        serializer_class = VotacionesSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    @action(methods=['GET'], detail=False)
    def countVotaciones(self, request):
        queryset = Votaciones.objects.all().count('votaciones')
        serializer = self.get_serializer_class()
        if queryset > 20:
            print('Este boletín se lanzará por ser el ma votado')
            serialized = serializer(queryset, many=True)
            return Response(data=serialized.data)



class BoletinViewSet(viewsets.ModelViewSet):

    queryset = Boletin.objects.all()
    serializer_class = BoletinSerializer

    def list(self,request):
        serializer_class = BoletinSerializer(self.queryset,many=True)
        return Response(serializer_class.data)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        fecha_envio_correo = datetime.now() + timedelta(seconds=10)
        boletin_email.apply_async(
            args=[request.user.email],
            eta=fecha_envio_correo
        )
        serializer = self.get_serializer_class()
        serialized = serializer(data=request.data)
        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)

        serialized.save()
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)

    @action(methods=['GET'], detail=False)
    def categories(self, request):
        queryset = Boletin.objects.all().order_by('categorias')
        serializer = self.get_serializer_class()
        serialized = serializer(queryset, many=True)
        return Response(data=serialized.data)