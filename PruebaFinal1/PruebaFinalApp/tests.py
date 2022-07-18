from django.test import TestCase
from .views import *
from .models import Publicaciones
# Create your tests here.


class PublicacionesTest(TestCase):
    def setUp(self):
        Publicaciones.objects.create(titulo="Publicacion de viaje a Brasil", pais= 2,)

    def test_publicacion_nombre(self):
        Publicacion = Publicacion.objects.get(pais = 2)
        self.assertEqual(self.publicacion.nombre, "Publicacion de viaje a Brasil")

    def test_publicacion_creada(self):
        Publicacion = Publicacion.objects.get(pais = 2)
        self.assertNotEquals(publicaciones, None)