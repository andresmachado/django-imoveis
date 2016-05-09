from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CreatePropertyForm
from .models import Property

def property_list(request, template_name='properties/property_list.html'):
	properties = Property.objects.all()
	return render(request, template_name, {'properties': properties})


@login_required
def property_create(request, template_name = 'properties/property_create.html'):
	form = CreatePropertyForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		property = form.save(commit=False)
		property.owner = request.user
		property.image = request.FILES['image']
		property.save()
		messages.success(request, "Anuncio publicado com sucesso!")
		return redirect('show_property', pk=property.id)
	return render(request, template_name, {'form': form})


@login_required
def property_edit(request, pk, template_name='properties/property_create.html'):
    property = get_object_or_404(Property, pk=pk, owner=request.user.id)
    form = CreatePropertyForm(request.POST or None, request.FILES or None, instance=property)
    if form.is_valid():
    	property = form.save()
    	if property.image in form.changed_data:
    		property.image = request.FILES['image']
    	property.save()
    	messages.success(request, "Post editado com successo!")
    	return redirect('show_property', pk=pk)
    return render(request, template_name, {'form': form, 'property':property})


def property_detail(request, pk, template_name='properties/property_detail.html'):
	property = get_object_or_404(Property, pk=pk)
	recommended = Property.objects.filter(city__icontains=property.city).exclude(pk=pk)
	context = {
		'property': property,
		'recommended': recommended
	}
	return render(request, template_name, context)


def property_delete(request, pk):
    return HttpResponse('<h1> Delete page works! </h1>')