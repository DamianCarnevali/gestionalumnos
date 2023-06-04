from rest_framework import serializers
from .models import Materias, Carreras


class MateriasSerializer(serializers.ModelSerializer):
    correlativas = serializers.SlugRelatedField(
        many=True,
        queryset=Materias.objects.all(),
        slug_field='nombre',
        required=False
    )

    class Meta:
        model = Materias
        fields = '__all__'


class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'
