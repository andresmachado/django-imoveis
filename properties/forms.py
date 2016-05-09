from django import forms

from .models import Property

class CreatePropertyForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CreatePropertyForm, self).__init__(*args, **kwargs)
		self.fields['category'].label = "Categoria"
		self.fields['property_type'].label = "Tipo do imóvel"

	class Meta:
		model = Property
		fields = ( 'cep', 'address', 'state', 'city', 'district',
				  'property_type', 'category', 'rooms', 'util_area', 'total_area', 'title', 'image', 'description',
				  'rent_price'
		)
		widgets = {
			'district': forms.TextInput(attrs={'readonly': 'readonly'}),
			'city': forms.TextInput(attrs={'readonly': 'readonly'}),
		}