# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib import admin
from datastorage.models import Personal_Info, House_Info_Keys, House_Info, Farm_Info_Keys, Farm_Info, Wells_Info, Crop_Info

# Register your models here.
admin.site.register(Personal_Info)
admin.site.register(House_Info_Keys)
admin.site.register(House_Info)
admin.site.register(Farm_Info_Keys)
admin.site.register(Farm_Info)
admin.site.register(Wells_Info)
admin.site.register(Crop_Info)
