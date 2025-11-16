from django.test import TestCase
from django.urls import reverse

class TesteNivel1(TestCase):
    def test_template_usado_nivel1(self):

        url = reverse('nivel1')
        response = self.client.get(url)

        # teste propositalmente errado
        self.assertTemplateUsed(response, 'termo/nivel1.html')