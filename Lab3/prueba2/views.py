from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'title' : 'Título del index de la aplicación testing en el template ubicado en "templates/testing/index.html"'}

	return render (request, 'prueba2/index.html', context)