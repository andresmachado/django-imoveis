from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse

from .forms import CreatePropertyForm

def property_list(request):
    return HttpResponse('<h1> It works </h1>')

def property_create(request):
	if request.method == "POST":
		form = CreatePropertyForm(request.POST, request.FILES)
		if form.is_valid():
			property = form.save(commit=False)
			property.owner = request.user
			property.image = request.FILES['image']
			property.save()
			messages.success(request, "Anuncio publicado com sucesso!")
			return redirect('show_property', pk=property.id)
	else:
		form = CreatePropertyForm()
	return render(request, 'properties/property_create.html', {'form': form})

def property_detail(request, pk):
    return HttpResponse('<h1> Detail page works! </h1>')

def property_edit(request, pk):
    return HttpResponse('<h1> Edit page works! </h1>')

def property_delete(request, pk):
    return HttpResponse('<h1> Delete page works! </h1>')