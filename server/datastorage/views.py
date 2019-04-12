# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datastorage.models import Personal_Info, House_Info_Keys, House_Info, Farm_Info_Keys, Farm_Info, Wells_Info, Crop_Info
from rest_framework import viewsets
from datastorage.serializers import Personal_InfoSerializer, House_Info_KeysSerializer, House_InfoSerializer, Farm_Info_KeysSerializer, Farm_InfoSerializer, Wells_InfoSerializer, Crop_InfoSerializer
# Create your views here.

class Personal_InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personal_Info.objects.all()
    serializer_class = Personal_InfoSerializer

class House_Info_KeysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = House_Info_Keys.objects.all()
    serializer_class = House_Info_KeysSerializer

class House_InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = House_Info.objects.all()
    serializer_class = House_InfoSerializer

class Farm_Info_KeysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Farm_Info_Keys.objects.all()
    serializer_class = Farm_Info_KeysSerializer

class Farm_InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Farm_Info.objects.all()
    serializer_class = Farm_InfoSerializer

class Wells_InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Wells_Info.objects.all()
    serializer_class = Wells_InfoSerializer

class Crop_InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Crop_Info.objects.all()
    serializer_class = Crop_InfoSerializer

