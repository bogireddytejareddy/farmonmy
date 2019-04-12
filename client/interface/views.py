# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.
def house(request):
	req = requests.get('http://127.0.0.1:1999/house/')
	conj = req.json()
	house_id = []
	house_capacity = []
	house_area = []
	house_income = []
	house_position_lat = []
	house_position_lon = []
	house_image = []
	houseinfo_id = []
	for i in xrange(len(conj)):
		house_id.append(conj[i]['id'])
		house_capacity.append(conj[i]['house_capacity'])
		house_area.append(conj[i]['house_area'])
		house_income.append(conj[i]['house_income'])
		house_position_lat.append(float(conj[i]['house_position'][17:23]))
		house_position_lon.append(float(conj[i]['house_position'][35:41]))
		house_image.append(conj[i]['house_image'])
		houseinfo_id.append(conj[i]['houseinfo_id'])
	context= {'house_id':house_id,'house_capacity':house_capacity,'house_income':house_income,'house_lat':house_position_lat,'house_lon':house_position_lon,'house_image':house_image,'houseinfo_id':houseinfo_id}
	return render(request, 'interface/house.html', context)

def wells(request):
	req = requests.get('http://127.0.0.1:1999/wells/')
	conj = req.json()
	wellsinfo_id = []
	wells_position_lat = []
	wells_position_lon = []
	wells_depth = []
	for i in xrange(len(conj)):
		wellsinfo_id.append(conj[i]['wellsinfo_id'])
		wells_position_lat.append(float(conj[i]['wells_position'][17:23]))
                wells_position_lon.append(float(conj[i]['wells_position'][35:41]))
		wells_depth.append(conj[i]['wells_depth'])
	context= {'wellsinfo_id':wellsinfo_id,'wells_lat':wells_position_lat,'wells_lon':wells_position_lon,'wells_depth':wells_depth}
        return render(request, 'interface/wells.html', context)

def crops(request):
	req = requests.get('http://127.0.0.1:1999/crops/')
	conj = req.json()
	crop_id = []
	crop_name = []
	crop_area = []
	cropfarm_id = []
	for i in xrange(len(conj)):
		crop_id.append(conj[i]['id'])
		crop_name.append(conj[i]['crop_name'])
		crop_area.append(conj[i]['crop_output'])
		cropfarm_id.append(conj[i]['cropfarm_id'])
	context= {'crop_id':crop_id,'crop_name':crop_name,'crop_area':crop_area,'cropfarm_id':cropfarm_id}
	return render(request, 'interface/farm.html', context)

def farm(request):
	req = requests.get('http://127.0.0.1:1999/farms/')
        conj = req.json()
	sreq = requests.get('http://127.0.0.1:1999/crops/')
	sconj = sreq.json()
	crop_id = []
	crop_name = []
	crop_area = []
	cropfarm_id = []
	for i in xrange(len(sconj)):
		crop_id.append(sconj[i]['id'])
		crop_name.append(sconj[i]['crop_name'])
		cropfarm_id.append(sconj[i]['cropfarm_id'])
	farm_id = []
	farminfo_id = []
	farm_lat = []
	farm_lon = []
	for i in xrange(len(conj)):
		listing_lat = []
		listing_lon = []
		print i
		farm_id.append(conj[i]['id'])
		farm_position_lat1 = (float(conj[i]['farm_position'][20:26]))
		farm_position_lat2 = (float(conj[i]['farm_position'][57:63]))
		farm_position_lat3 = (float(conj[i]['farm_position'][93:99]))
		farm_position_lat4 = (float(conj[i]['farm_position'][128:134]))
		farm_position_lon1 = (float(conj[i]['farm_position'][38:44]))
		farm_position_lon2 = (float(conj[i]['farm_position'][75:81]))
		farm_position_lon3 = (float(conj[i]['farm_position'][110:116]))
		farm_position_lon4 = (float(conj[i]['farm_position'][146:152]))
		farminfo_id.append(conj[i]['farminfo_id'])
		listing_lat = [farm_position_lat1, farm_position_lat2, farm_position_lat3, farm_position_lat4]
		farm_lat.append(listing_lat)
		listing_lon = [farm_position_lon1, farm_position_lon2, farm_position_lon3, farm_position_lon4]
        	farm_lon.append(listing_lon)
	print listing_lat
	for a in xrange(len(farm_id)):
		temp = []
		for j in xrange(len(sconj)):
			if a+1 == sconj[j]['cropfarm_id']:
				temp.append(sconj[j]['crop_output'])
		crop_area.append(temp)
	print crop_area
	#print farm_lat
	#print farm_lon
	crop_fpos = []
	for i in range(len(farm_lat)):
		temp_fpos = [(farm_lat[i][0]),(farm_lon[i][0])]
		crop_fpos.append(temp_fpos)
		temp_fpos = []
	print crop_fpos
	final = []
	for j in xrange(len(crop_fpos)):
		final.append(crop_fpos[j]+crop_area[j])
	print final
	context = {'farm_id':farm_id,'farm_lat':farm_lat,'farm_lon':farm_lon,'farminfo_id':farminfo_id,'final': final}
        return render(request, 'interface/farm.html', context)

def graph(request):
	req = requests.get('http://127.0.0.1:1999/crops/')
        conj = req.json()
	wheat = 0
	paddy = 0
	mazie = 0
	groundnut = 0
	for i in xrange(len(conj)):
		if (conj[i]['crop_name'] == "wheat" or conj[i]['crop_name'] == "Wheat"):
			wheat = wheat + conj[i]['crop_output']
		elif (conj[i]['crop_name'] == "Paddy"):
                        paddy = paddy + conj[i]['crop_output']
		elif (conj[i]['crop_name'] == "Maize"):
                        mazie = mazie + conj[i]['crop_output']
		elif (conj[i]['crop_name'] == "GroundNut"):
                        groundnut = groundnut + conj[i]['crop_output']
	print groundnut,mazie,paddy,wheat
	context = {'groundnut':groundnut, 'mazie':mazie, 'paddy':paddy, 'wheat':wheat}
	return render(request, 'interface/graph.html', context)

def analytics(request):
	req = requests.get('http://127.0.0.1:1999/crops/')
        conj = req.json()
	w1 = 0
	w2 = 0
	m1 = 0
	m2 = 0
	p1 = 0
	p2 = 0
	gn1 = 0
	gn2 = 0
	for i in xrange(len(conj)):
		if (conj[i]['cropfarm_id'] == 1):
			if (conj[i]['crop_name'] == "wheat" or conj[i]['crop_name'] == "Wheat"):
				w1  = w1 + conj[i]['crop_output']
		if (conj[i]['cropfarm_id'] == 1):
                        if (conj[i]['crop_name'] == "Maize"):
                                m1  = m1 + conj[i]['crop_output']
		if (conj[i]['cropfarm_id'] == 1):
                        if (conj[i]['crop_name'] == "Paddy"):
                                p1  = p1 + conj[i]['crop_output']
		if (conj[i]['cropfarm_id'] == 1):
                        if (conj[i]['crop_name'] == "GroundNut"):
                                gn1  = gn1 + conj[i]['crop_output']
		if (conj[i]['cropfarm_id'] == 2):
                        if (conj[i]['crop_name'] == "wheat" or conj[i]['crop_name'] == "Wheat"):
                                w2  = w2 + conj[i]['crop_output']
                if (conj[i]['cropfarm_id'] == 2):
                        if (conj[i]['crop_name'] == "Maize"):
                                m2  = m2 + conj[i]['crop_output']
                if (conj[i]['cropfarm_id'] == 2):
                        if (conj[i]['crop_name'] == "Paddy"):
                                p2  = p2 + conj[i]['crop_output']
                if (conj[i]['cropfarm_id'] == 2):
                        if (conj[i]['crop_name'] == "GroundNut"):
                                gn2  = gn2 + conj[i]['crop_output']
	context = {'gn1':gn1, 'm1':m1, 'p1':p1, 'w1':w1,'gn2':gn2, 'm2':m2, 'p2':p2, 'w2':w2}
        return render(request, 'interface/analytics.html', context)

def threed(request):
	return render(request,'interface/3d.html')

def piechart(request):
	return render(request, 'interface/pie.html')

def homepage(request):
	return render(request, 'interface/home.html')
