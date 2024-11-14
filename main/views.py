
from django.shortcuts import render
from catalogo.services.google_books_service import GoogleBooksService 
from django.shortcuts import render, get_object_or_404
from catalogo.models import Libro

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

##### Buscar libros locales ####
@classmethod
def buscar_libro_local(cls, query):
        return cls.objects.filter(titulo__icontains=query)  # Filtra libros que contengan 'query' en el título
    
def buscar_libros_locales(request):
    query = request.GET.get('q', '')  # Obtiene el parámetro 'q' de la URL
    if query:
        # Llama al método buscar_libro_local de la clase Libro
        libros = Libro.buscar_libro_local(query)
    else:
        # Si no hay consulta, la lista de libros queda vacía
        libros = []
    
    return render(request, 'buscar_libros_locales.html', {'libros': libros})

##### detalles libros locales #####

def detalle_libro_local(request, libro_id):
    try:
        libro = Libro.objects.get(id=libro_id)  # Recupera el libro por su ID.
    except Libro.DoesNotExist:
        return render(request, '404.html')  # Si el libro no se encuentra, puedes mostrar un error.

    return render(request, 'detalles_libros_locales.html', {'libro': libro})