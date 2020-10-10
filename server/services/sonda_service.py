from server.models.sonda import Sonda


def criar_sonda(body):
    """Criar uma nova sonda

    :param body: Objeto necessário para criar uma nova sonda
    :type body: dict | bytes

    :rtype: Sonda
    """
    return Sonda(body['posicao_x'], body['posicao_y'], body['direcao_cardinal'])

