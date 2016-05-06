from django import forms

from .models import Property

class CreatePropertyForm(forms.ModelForm):

	class Meta:
		model = Property
		fields = ( 'cep', 'address', 'state', 'city', 'district',
				  'property_type', 'category', 'rooms', 'util_area', 'total_area', 'title', 'image', 'description',
				  'rent_price'
		)