
from django.shortcuts import render
from catalogo.services.google_books_service import GoogleBooksService 

##### inicio de la pagina #######

def index(request):
    return render(request, 'index.html')

##### Detalles de los libros #######

def detalles_libro(request, google_books_id):
    libro_detalles = GoogleBooksService.obtener_detalles_libro(google_books_id)
    
    if libro_detalles:
        return render(request, 'detalles_libro.html', {'libro': libro_detalles})
    else:
        return render(request, 'detalles_libro.html', {'error': 'No se pudo obtener los detalles del libro.'})
    
####   Buscar libros #######

def buscar_libros(request):
    query = request.GET.get('q', '') 
    resultados = []
    if query:
        resultados = GoogleBooksService.buscar_libro(query)  

    return render(request, 'buscar_libros.html', {'query': query, 'resultados': resultados})
