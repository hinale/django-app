from django.test import TestCase
from dados.models import Cliente


class ClienteTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(nome="leticia", idade="20")
        Cliente.objects.create(nome="hina", idade="19")

    def test_idade_true(self):
        leticia = Cliente.objects.get(nome="leticia")
        hina = Cliente.objects.get(nome="hina")
        self.assertEqual(leticia.idade, 20)
        self.assertEquals(hina.idade, 20)
