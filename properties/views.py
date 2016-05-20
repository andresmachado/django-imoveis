import json

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict

from .forms import CreatePropertyForm
from .models import Property


def property_list(request, template_name='properties/property_list.html'):
    """List all properties."""
    properties = Property.objects.all()
    search = request.GET.get('search')
    if search:
        properties = properties.filter(
            Q(district__unaccent__icontains=search) |
            Q(city__unaccent__icontains=search) |
            Q(state__unaccent__icontains=search) |
            Q(address__unaccent__icontains=search)
        )
    return render(request, template_name, {'properties': properties})


@login_required
def property_create(request, template_name='properties/property_create.html'):
    """Property create view."""
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
    """Property edit view."""
    property = get_object_or_404(Property, pk=pk, owner=request.user.id)
    form = CreatePropertyForm(request.POST or None,
                              request.FILES or None,
                              instance=property)
    if form.is_valid():
        property = form.save()
        if property.image in form.changed_data:
            property.image = request.FILES['image']
        property.save()
        messages.success(request, "Post editado com successo!")
        return redirect('show_property', pk=pk)
    return render(request, template_name, {'form': form, 'property': property})


def property_detail(request, pk, template_name='properties/property_detail.html'):
    """Property detail view."""
    property = get_object_or_404(Property, pk=pk)
    recommended = Property.objects.filter(city__icontains=property.city).exclude(pk=pk)
    context = {
        'property': property,
        'recommended': recommended
    }
    return render(request, template_name, context)


@login_required
def property_delete(request):
    """Delete property view."""
    if request.method == "DELETE":
        property = get_object_or_404(
            Property,
            pk=int(QueryDict(request.body).get('property_id')), owner=request.user.id
        )
        property_title = property.title
        property.delete()

        response_data = {}
        response_data['msg'] = "Anúncio {} excluído com sucesso.".format(property_title)
        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json'
        )
    else:
        return HttpResponse(status=404)
