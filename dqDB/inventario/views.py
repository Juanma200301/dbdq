from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from .models import IceCream
from .serializers import IceSerializer


# Create your views here.
class IceViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceSerializer
    