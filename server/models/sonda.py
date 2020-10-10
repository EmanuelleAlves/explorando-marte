from __future__ import absolute_import
from server.models.base_model_ import Model
from server import util


class Sonda(Model):
    def __init__(self, posicao_x: int = None, posicao_y: int = None, direcao_cardinal: str = None):
        self._posicao_x = posicao_x
        self._posicao_y = posicao_y
        self._direcao_cardinal = direcao_cardinal

    @classmethod
    def from_dict(cls, dikt) -> 'Sonda':
        """Retorna um modelo do dict

        :param dikt: Um dict.
        :type: dict
        :return: Um objeto do tipo Sonda
        :rtype: Sonda
        """
        return util.deserialize_model(dikt, cls)

    @property
    def posicao_x(self) -> int:
        """Retorna a posicao_x da Sonda.


        :return: A posicao_x da Sonda.
        :rtype: int
        """
        return self._posicao_x

    @posicao_x.setter
    def posicao_x(self, posicao_x: int):
        """Adiciona a posicao_x da Sonda.


        :param posicao_x: A posicao_x da Sonda.
        :type posicao_x: int
        """
        if posicao_x is None:
            raise ValueError("Posição X não pode ser nula.")

        self._posicao_x = posicao_x

    @property
    def posicao_y(self) -> int:
        """Retorna a posicao_y da Sonda.


        :return: A posicao_y da Sonda.
        :rtype: int
        """
        return self._posicao_y

    @posicao_y.setter
    def posicao_y(self, posicao_y: int):
        """Adiciona a posicao_y da Sonda.


        :param posicao_y: A posicao_y da Sonda.
        :type posicao_y: int
        """
        if posicao_y is None:
            raise ValueError("Posição Y não pode ser nula.")

        self._posicao_y = posicao_y

    @property
    def direcao_cardinal(self) -> str:
        """Retorna a direção cardinal da sonda

        Direção em que a sonda está apontando.

        :return: A direção cardinal da sonda.
        :rtype: str
        """
        return self._direcao_cardinal

    @direcao_cardinal.setter
    def direcao_cardinal(self, direcao_cardinal: str):
        """Adiciona a direcao_cardinal da Sonda.

        Direção em que a sonda está apontando

        :param direcao_cardinal: Direção cardinal da sonda.
        :type direcao_cardinal: str
        """
        allowed_values = ["N", "E", "S", "W"]
        if direcao_cardinal not in allowed_values:
            raise ValueError(
                f"{direcao_cardinal} é um valor inválido. Valores válidos: {allowed_values}"
            )

        self._direcao_cardinal = direcao_cardinal

    def alterar_posicoes(self, posicao_x, posicao_y, direcao_cardinal):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.direcao_cardinal = direcao_cardinal

    def __str__(self):
        return f"Status da sonda: " \
               f"Posicao X = {self.posicao_x}. " \
               f"Posicao Y = {self.posicao_y}. " \
               f"Direção Cardinal = {self.direcao_cardinal}"
