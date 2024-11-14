from django.db import models

from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    publicado_en = models.DateField()

    def __str__(self):
        return self.titulo

    @classmethod
    def buscar_libro_local(cls, query):
        # Busca libros que contengan el texto 'query' en el título (insensible a mayúsculas/minúsculas)
        return cls.objects.filter(titulo__icontains=query)


class Meta:
    tabla_bd= "Libro"


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

    return render(request, 'detalle_libro_local.html', {'libro': libro})