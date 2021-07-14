from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, viewsets
from Boletin.models import Boletin, Votaciones
from Boletin.serializers import BoletinSerializer,VotacionesSerializer


class VotacionesViewSet(viewsets.ModelViewSet):

    queryset = Votaciones.objects.all()
    serializer_class = VotacionesSerializer

    def list(self, request):
        serializer_class = VotacionesSerializer(self.queryset, many=True)
        return Response(serializer_class.data)



class BoletinViewSet(viewsets.ModelViewSet):

    queryset = Boletin.objects.all()
    serializer_class = BoletinSerializer

    def list(self,request):
        serializer_class = BoletinSerializer(self.queryset,many=True)
        return Response(serializer_class.data)