

from rest_framework import serializers

from Boletin.models import Votaciones, Boletin


class VotacionesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Votaciones
        fields = '__all__'


class BoletinSerializer(serializers.ModelSerializer):

    class Meta:
        model= Boletin
        fields ='__all__'