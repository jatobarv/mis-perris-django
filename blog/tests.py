from django.test import TestCase
from .models import Post
# Create your tests here.


class PostTestCase(TestCase):
    def test_post_breed(self):
        # Arrange
        dog = Post.objects.create(name='Cholito', breed='Mestizo',
                                  description='Este es un post para realizar pruebas', condition='Disponible')
        expected = 'Mestizo'
        # Act
        result = dog.breed
        # Assert
        self.assertEqual(expected, result)
        print('Resultado esperado: ' + expected)
        print('Resultado final: ' + result)
