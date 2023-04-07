
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Coords, Level, Pereval, Images


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'
        verbose_name = 'Координаты'


class LevelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='patronymic')
    email = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'fam', 'name', 'otc', 'phone',)
        verbose_name = 'Пользователь'


class ImagesSerializer(serializers.ModelSerializer):
    #data = serializers.ImageField(max_length=None, use_url=True)
    data = serializers.CharField()

    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Фото'




class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerialize()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        exclude = ('id', 'status')







