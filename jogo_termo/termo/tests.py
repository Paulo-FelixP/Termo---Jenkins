from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

class TesteBasicoTermo(TestCase):
    def test_pagina_inicial_carrega(self):
        """
        Testa se a página inicial do projeto responde com status 200.
        Caso sua view principal tenha outro nome, basta ajustar a URL.
        """

        url = reverse('index')  # <- ajuste aqui caso sua URL tenha outro nome
        response = self.client.get(url)

        # 1) A página deve existir
        self.assertEqual(response.status_code, 200)

        # 2) A página deve conter algum texto esperado
        self.assertIn(b"Termo", response.content)
