from server.models.planalto import Planalto


def criar_planalto(body):
    """Criar um novo planalto
    :param body: Objeto necessário para criar um planalto
    :type body: dict

    :rtype: Planalto
    """
    return Planalto(body['tamanho_x'], body['tamanho_y'])
