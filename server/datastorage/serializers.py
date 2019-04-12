from rest_framework import serializers
from datastorage.models import Personal_Info, House_Info_Keys, House_Info, Farm_Info_Keys, Farm_Info, Wells_Info, Crop_Info

class Personal_InfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personal_Info
		fields = '__all__'		
		#field = ('house_head', 'village_name', 'mail_id', 'aadhar_number', 'phone_number')

class House_Info_KeysSerializer(serializers.ModelSerializer):
	class Meta:
		model = House_Info_Keys
		fields = '__all__'
		#field = ('personal_id', 'house_id')

class House_InfoSerializer(serializers.ModelSerializer):
        class Meta:
                model = House_Info
		fields = '__all__'
                #field = ('houseinfo_id', 'house_capacity', 'house_area', 'house_income', 'house_position', 'house_image')

class Farm_Info_KeysSerializer(serializers.ModelSerializer):
        class Meta:
                model = Farm_Info_Keys
		fields = '__all__'
                #field = ('personal_id', 'farm_id')

class Farm_InfoSerializer(serializers.ModelSerializer):
        class Meta:
                model = Farm_Info
		fields = '__all__'
                #field = ('farminfo_id', 'farm_area', 'farm_position')

class Wells_InfoSerializer(serializers.ModelSerializer):
        class Meta:
                model = Wells_Info
		fields = '__all__'
                #field = ('wellsinfo_id', 'wells_position', 'wells_depth')

class Crop_InfoSerializer(serializers.ModelSerializer):
        class Meta:
                model = Crop_Info
		fields = '__all__'
                #field = ('crop_name', 'cropfarm_id', 'crop_output')
