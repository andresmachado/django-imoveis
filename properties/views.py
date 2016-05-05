from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse

def property_list(request):
    return HttpResponse('<h1> It works </h1>')

def property_detail(request, pk):
    return HttpResponse('<h1> Detail page works! </h1>')

def property_create(request):
    return HttpResponse('<h1> Create page works </h1>')

def property_edit(request, pk):
    return HttpResponse('<h1> Edit page works! </h1>')

def property_delete(request, pk):
    return HttpResponse('<h1> Delete page works! </h1>')