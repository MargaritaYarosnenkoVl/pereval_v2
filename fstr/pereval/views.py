from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pereval, Images
from .serializers import PerevalSerializer, ImagesSerializer, PerevalAddSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddSerializer

    def create(self, request):
        img = ImagesSerializer(data=request.data)
        if img.is_valid():
            img.save()
            return Response(status=201)
        else:
            print("ошибка")
            return Response({"error": "validation error"}, status=400)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer




