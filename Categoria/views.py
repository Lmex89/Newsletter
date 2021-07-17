from functools import partial
from re import S
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView

# Create your views here
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Categoria.models import Categoria
from Categoria.serializers import CategoriaSerializer


class CategoriaViewDetail(APIView):
    model = Categoria

    def get(self, request, pk):

        try:
            item_categoria = Categoria.objects.get(pk=pk)
            serializers = CategoriaSerializer(item_categoria)
            return Response(
                dict(
                    success=True,
                    data=serializers.data,
                ),
                status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                dict(
                    sucesss=False,
                    data=['Categoria id invalido']
                )
            )

    def put(self, request, pk):

        try:
            item_categoria = Categoria.objects.get(pk=pk)
            serializers = CategoriaSerializer(data=request.data, partial=True)
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
                    sucess=False,
                    data=[serializers.errors]
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as error:
            return Response(
                dict(
                    sucesss=False,
                    data=['Categoria id invalido', str(error)]
                )
            )

    def delete(self, request, pk):
        try:
            item_categoria = Categoria.objects.get(pk=pk)
            item_categoria.delete()
            return Response(
                dict(
                    sucess=True,
                    data=['categoria eliminada']
                ),
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                dict(
                    sucesss=False,
                    data=['Categoria id invalido', str(error)]
                )
            )


class CategoriaListView(APIView):
    model = Categoria

    def get(self, request):
        items_categoria = Categoria.objects.all()
        if items_categoria:
            serializers = CategoriaSerializer(
                items_categoria,
                many=True
            )
            return Response(
                dict(
                    success=True,
                    data=serializers.data
                ),
                status=status.HTTP_200_OK
            )

    def post(self, request):
        serializers = CategoriaSerializer(
            data=request.data,
            partial=True
        )
        if serializers.is_valid():
            return Response(
                dict(
                    success=True,
                    data=serializers.data
                ),
                status=status.HTTP_201_CREATED
            )
        return Response(
            dict(
                success=False,
                data=serializers.errors
            ),
            status=status.HTTP_400_BAD_REQUEST
        )
