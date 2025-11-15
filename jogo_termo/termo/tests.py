from django.test import TestCase
from django.urls import reverse

class TesteNivel1(TestCase):
    def test_template_usado_nivel1(self):
        """
        ESTE TESTE VAI FALHAR DE PROPÓSITO.
        Ele espera que o nível 1 use o template 'termo/home.html',
        mas sua view usa 'termo/nivel1.html'.
        Assim você aprende como localizar e resolver o erro.
        """

        url = reverse('nivel1')
        response = self.client.get(url)

        # teste propositalmente errado
        self.assertTemplateUsed(response, 'nao_existe_teste.html')