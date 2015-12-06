from django.shortcuts import render
from models import Toilet
from serializers import ToiletSerializer
from rest_framework import generics, viewsets, permissions

# Create your views here.
class ToiletViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ToiletList(generics.ListCreateAPIView):
    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer

class ToiletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer
