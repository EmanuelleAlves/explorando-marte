# coding: utf-8

from __future__ import absolute_import
from server.models.base_model_ import Model
from server import util


class Planalto(Model):
    def __init__(self, tamanho_x: int = None, tamanho_y: int = None):
        self._tamanho_x = tamanho_x
        self._tamanho_y = tamanho_y

    @classmethod
    def from_dict(cls, dikt) -> 'Planalto':
        """Retorna um modelo do dict

        :param dikt: Um dict.
        :type: dict
        :return: Um objeto do tipo Planalto.
        :rtype: Planalto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tamanho_x(self) -> int:
        """Retorna o tamanho_x do planalto

        :return: O tamanho_x do planalto.
        :rtype: int
        """
        return self._tamanho_x

    @tamanho_x.setter
    def tamanho_x(self, tamanho_x: int):
        """Adiciona o tamanho_x do planalto

        :param tamanho_x: O tamanho_x do planalto.
        :type tamanho_x: int
        """

        self._tamanho_x = tamanho_x

    @property
    def tamanho_y(self) -> int:
        """Retorna o tamanho_x do planalto

        :return: O tamanho_y do planalto.
        :rtype: int
        """
        return self._tamanho_y

    @tamanho_y.setter
    def tamanho_y(self, tamanho_y: int):
        """Adiciona o tamanho_y do planalto

        :param tamanho_y: O tamanho_y do planalto.
        :type tamanho_y: int
        """

        self._tamanho_y = tamanho_y
