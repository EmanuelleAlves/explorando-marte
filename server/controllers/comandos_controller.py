from server.services import controle_service


def post_comandos(body):
    """Recebe os comandos enviados no body e envia para o service.
    :param body: Objeto necessário para realizar os comandos
    :type body: dict
    """
    return controle_service.realizar_comando(body), 200
