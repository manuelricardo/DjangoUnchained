from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	context = {
		'title' : 'Mis Películas',
		'description' : 'Esta es mi página de películas',
		'movie' : 'Inception',
		'director' : 'Christopher Nolan',
		'genre' : 'Ciencia Ficción'
	}

	return render (request, 'prueba1/index.html', context)