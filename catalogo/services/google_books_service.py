
import requests
import logging

logger = logging.getLogger(__name__)

class GoogleBooksService:
    BASE_URL = "https://www.googleapis.com/books/v1/volumes"

    @staticmethod
    def buscar_libro(query):
        try:
            params = {
                'q': query,
                'maxResults': 40,
                'langRestrict': 'es'
            }
            response = requests.get(GoogleBooksService.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error al buscar en Google Books: {str(e)}")
            return None

    @staticmethod
    def obtener_detalles_libro(google_books_id):
        try:
            response = requests.get(f"{GoogleBooksService.BASE_URL}/{google_books_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error al obtener detalles del libro: {str(e)}")
            return None
