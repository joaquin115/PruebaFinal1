from django.test import TestCase
from .views import *
from .models import *
# Create your tests here.


class PublicacionesTest(TestCase):
    def setUp(self):
        Publicaciones.objects.create(titulo="Viajando por Uruguay", pais= "Uruguay", descripcion="Montevideo", fecha_viaje="2022-07-18")

    def test_publicacion_titulo(self):
        resultado = Publicaciones.objects.get(pais = "Uruguay")
        self.assertEqual(resultado.titulo, "Viajando por Uruguay")   

    def test_publicacion_creada(self):
        resultado = Publicaciones.objects.get(pais = "Uruguay")
        self.assertNotEquals(resultado, None)
    
    def test_publicacion_descripcion(self):
        resultado = Publicaciones.objects.get(pais = "Uruguay")
        self.assertEqual(resultado.descripcion, "Montevideo")