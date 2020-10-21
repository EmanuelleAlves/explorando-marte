# coding: utf-8

from __future__ import absolute_import

from flask import json
from server.models.planalto import Planalto
from server.models.sonda import Sonda
from server.test import BaseTestCase


class TestComandosController(BaseTestCase):

    def test_enviar_somente_comandos_validos(self):
        """
        Testar o retorno quando enviar somente comandos válidos
        """
        body = {
            "planalto": {
                "tamanho_x": 5,
                "tamanho_y": 5
            },
            "sondas": [
                {
                    "movimentos": [
                        "M", "M", "R", "M", "M", "R", "M", "R", "R", "M"
                    ],
                    "sonda_inicial": {
                        "direcao_cardinal": "E",
                        "posicao_x": 3,
                        "posicao_y": 3
                    }
                }
            ]
        }

        response_esperado = [{
            "avisos": ["Não houve nenhum problema, conseguimos realizar todos movimentos!"],
            "sonda": "Status da sonda: Posicao X = 5. Posicao Y = 1. Direção Cardinal = E"
        }]

        response = self.client.open(
            '/v1/enviar-comando',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.json, response_esperado)

    def test_enviar_criacao_da_sonda_fora_do_planalto(self):
        """
        Testar o retorno quando enviar somente comandos válidos
        """
        body = {
            "planalto": {
                "tamanho_x": 5,
                "tamanho_y": 5
            },
            "sondas": [
                {
                    "movimentos": [
                        "M", "M", "R", "M", "M", "R", "M", "R", "R", "M"
                    ],
                    "sonda_inicial": {
                        "direcao_cardinal": "E",
                        "posicao_x": 8,
                        "posicao_y": 3
                    }
                }
            ]
        }

        response_esperado = [{
            "avisos": ["Você tentou aterrisar a sonda fora do planalto. Vamos fingir que nada aconteceu..."],
            "sonda": '''{"direcao_cardinal": "E", "posicao_x": 8, "posicao_y": 3}'''
        }]

        response = self.client.open(
            '/v1/enviar-comando',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.json, response_esperado)

    def test_enviar_movimento_invalido_eixo_y(self):
        """
        Testar o retorno quando enviar movimento inválido no eixo_y
        """
        body = {
            "planalto": {
                "tamanho_x": 5,
                "tamanho_y": 5
            },
            "sondas": [
                {
                    "movimentos": [
                        "L", "M", "L", "M", "L", "M", "L", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"
                    ],
                    "sonda_inicial": {
                        "direcao_cardinal": "N",
                        "posicao_x": 1,
                        "posicao_y": 2
                    }
                }
            ]
        }

        response_esperado = [{
            "avisos": [
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível.",
                "Essa posição Y não está disponível."
            ],
            "sonda": "Status da sonda: Posicao X = 1. Posicao Y = 5. Direção Cardinal = N"
        }]

        response = self.client.open(
            '/v1/enviar-comando',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.json, response_esperado)

    def test_enviar_movimento_invalido_eixo_x(self):
        """
        Testar o retorno quando enviar movimento inválido no eixo_x
        """
        body = {
            "planalto": {
                "tamanho_x": 5,
                "tamanho_y": 5
            },
            "sondas": [
                {
                    "movimentos": [
                        "L", "M", "L", "M", "L", "M", "L", "L", "M", "M"
                    ],
                    "sonda_inicial": {
                        "direcao_cardinal": "N",
                        "posicao_x": 1,
                        "posicao_y": 2
                    }
                }
            ]
        }

        response_esperado = [{
            "avisos": [
                "Essa posição X não está disponível."
            ],
            "sonda": "Status da sonda: Posicao X = 0. Posicao Y = 1. Direção Cardinal = W"
        }]

        response = self.client.open(
            '/v1/enviar-comando',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.json, response_esperado)

    def test_unitario(self):
        planalto = Planalto(5, 5)
        sonda = Sonda(planalto, 1, 2, "N")

        sonda.movimentar_sonda("L")
        sonda.movimentar_sonda("M")
        sonda.movimentar_sonda("L")
        sonda.movimentar_sonda("M")
        sonda.movimentar_sonda("L")
        sonda.movimentar_sonda("M")
        sonda.movimentar_sonda("L")
        sonda.movimentar_sonda("M")
        sonda.movimentar_sonda("M")

        self.assertEqual(sonda.posicao_x, 1)
        self.assertEqual(sonda.posicao_y, 3)
        self.assertEqual(sonda.direcao_cardinal, "N")


if __name__ == '__main__':
    import unittest
    unittest.main()
