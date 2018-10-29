from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def test_users_name(self):
        # Arrange
        user = User.objects.create_user(
            username='Pepe Grillo', password='duoc.2018')
        expected = 'Pepe Grillo'
        # Act
        result = user.username
        # Assert
        self.assertEqual(expected, result)
        print('Resultado esperado: ' + expected)
        print('Resultado final: ' + result)
