# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Personal_Info(models.Model):
	house_head = models.CharField(max_length = 100, blank = True, default = '')
	village_name = models.CharField(max_length = 100, blank = True, default = '')
	mail_id = models.CharField(max_length = 100, blank = True, default = '')
	aadhar_number = models.IntegerField()
	phone_number = models.IntegerField()

class House_Info_Keys(models.Model):
	personal_id = models.ForeignKey(Personal_Info, on_delete=models.CASCADE)
	house_id = models.AutoField(primary_key = True)

class House_Info(models.Model):
	houseinfo_id = models.ForeignKey(House_Info_Keys, on_delete = models.CASCADE)
	house_capacity = models.IntegerField()
	house_area = models.IntegerField()
	house_income = models.IntegerField()
	house_position = models.PointField(default = '')
	house_image = models.CharField(max_length = 100, blank = True, default = '')

class Farm_Info_Keys(models.Model):
	personal_id = models.ForeignKey(Personal_Info, on_delete=models.CASCADE)
	farm_id = models.AutoField(primary_key = True)

class Farm_Info(models.Model):
	farminfo_id = models.ForeignKey(Farm_Info_Keys, on_delete = models.CASCADE)
	farm_area = models.IntegerField()
	farm_position = models.PolygonField(default = '')

class Wells_Info(models.Model):
	wellsinfo_id = models.AutoField(primary_key = True)
	wells_position = models.PointField(default = '')
	wells_depth = models.IntegerField()

class Crop_Info(models.Model):
        crop_name = models.CharField(max_length = 100, blank = True, default = '')
        crop_output = models.IntegerField()
	cropfarm_id = models.IntegerField()

class Temperature(models.Model):
	temp_id = models.IntegerField()
	temperature = models.IntegerField()
