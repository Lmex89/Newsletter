# Create your views here.
from re import A
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from Boletin.models import Boletin, Votaciones
from Boletin.serializers import BoletinSerializer, VotacionesSerializer
from rest_framework.decorators import api_view, action
from django.core.mail import send_mail
from Boletin.task import boletin_email
from rest_framework import generics


class BoletinViewsDetail(APIView):
    model = Boletin

    def get(self, request, pk):
        try:
            item_boletines = Boletin.objects.get(pk=pk)
            serializers = BoletinSerializer(item_boletines)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(dict(success=False, data=['Boletin id  Invalido']))

    def put(self, request, pk):
        request.POST._mutable = True
        request.data['owner'] = request.user.pk
        try:
            item_boletines = Boletin.objects.get(pk=pk)
            serializers = BoletinSerializer(data=item_boletines, partial=True)
            if serializers.is_valid():
                return Response(data=serializers.data,
                                status=status.HTTP_200_OK)
            return Response(dict(success=False,
                                 data=[serializers.errors[error][0] for error in serializers.errors]),
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(dict(success=False,
                                 data=['Boletin id  Invalido', str(error)]),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            item_boletin = Boletin.objects.get(pk=pk)
            item_boletin.delete()
            return Response(dict(succes=True,
                                 data=['id eliminado correctamente']),
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(dict(success=False,
                                 data=['Boletin id  Invalido', str(error)]),
                            status=status.HTTP_400_BAD_REQUEST)


class BoletinListView(APIView):
    model = Boletin

    def get(self, request):
        item_boletines = Boletin.objects.all()
        if item_boletines:
            serializers = BoletinSerializer(item_boletines, many=True)
            return Response(dict(succes=True, data=serializers.data),
                            status=status.HTTP_200_OK)
        return Response(dict(succes=False, data=['No existen boletines']),
                        status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        request.POST._mutable = True
        serializers = BoletinSerializer(data=request.data, partial=True)
        if serializers.is_valid():
            return Response(dict(succes=True, data=serializers.data),
                            status=status.HTTP_201_CREATED)
        return Response(dict(succes=False,
                             data=[serializers.errors]),
                        status=status.HTTP_400_BAD_REQUEST)


class VotacionViewsDetail(APIView):
    model = Votaciones

    def get(self, request, pk):
        try:
            item_ = Votaciones.objects.get(pk=pk)
            serializers = VotacionesSerializer(item_)
            return Response(
                dict(
                    sucess=True,
                    data=serializers.data,
                ),
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                dict(
                    success=False,
                    data=['Boletin id  Invalido']
                )
            )

    def put(self, request, pk):
        try:
            item_ = Votaciones.objects.get(pk=pk)
            serializers = VotacionesSerializer(
                data=item_, partial=True)
            if serializers.is_valid():
                return Response(
                    dict(
                        sucess=True,
                        data=serializers.data
                    ),
                    status=status.HTTP_200_OK
                )
            return Response(
                dict(
                    success=False,
                    data=[serializers.errors]
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as error:
            return Response(
                dict(
                    success=False,
                    data=['Votacion id  Invalido', str(error)]
                    ),
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            item_ = Votaciones.objects.get(pk=pk)
            item_.delete()
            return Response(dict(succes=True,
                                 data=['id eliminado correctamente']),
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(dict(success=False,
                                 data=['Votacion id  Invalido', str(error)]),
                            status=status.HTTP_400_BAD_REQUEST)


class VotacionListView(APIView):
    model = Votaciones

    def get(self, request):
        item_ = Boletin.objects.all()
        if item_:
            serializers = VotacionesSerializer(
                item_,
                many=True
            )
            return Response(
                dict(
                    succes=True,
                    data=serializers.data
                ),
                status=status.HTTP_200_OK
            )
        return Response(
            dict(
                succes=False,
                data=['No existen boletines']
            ),
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        request.POST._mutable = True
        serializers = VotacionesSerializer(
            data=request.data,
            partial=True
        )
        if serializers.is_valid():
            return Response(
                dict(
                    sucess=True,
                    data=serializers.data
                ),
                status=status.HTTP_200_OK
            )
        return Response(
            dict(
                succes=False,
                data=[serializers.errors]
            ),
            status=status.HTTP_400_BAD_REQUEST
        )
