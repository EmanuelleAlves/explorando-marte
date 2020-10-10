from server.services import planalto_service, sonda_service, utils


def realizar_comando(body):
    """Recebe os comandos enviados pelo controller e realiza todas os passos necessário.
    :param body: Objeto necessário para realizar os comandos
    :type body: dict
    """
    sondas = body['sondas']
    planalto = planalto_service.criar_planalto(body['planalto'])
    sondas_final = []

    for count, sonda in enumerate(sondas, start=1):
        erros = []
        sonda_obj = sonda_service.criar_sonda(sonda['sonda_inicial'])
        movimento_valido, erro = utils.validar_movimento(sonda_obj.posicao_x,
                                                         sonda_obj.posicao_y,
                                                         planalto.tamanho_x,
                                                         planalto.tamanho_y)
        if movimento_valido:
            for movimento in sonda['movimentos']:
                realizar_movimento(sonda_obj, planalto, movimento, erros)
        else:
            erros.append("Você tentou aterrisar a sonda fora do planalto. Vamos fingir que nada aconteceu...")

        sondas_final.append({
            "sonda": str(sonda_obj),
            "avisos": erros if erros else "Não houve nenhum problema, conseguimos realizar todos movimentos!"
        })

    return sondas_final, 200


def realizar_movimento(sonda_obj, planalto, movimento, erros):
    proximo_x, proximo_y, proxima_direcao = utils.proximo_movimento(sonda_obj.posicao_x,
                                                                    sonda_obj.posicao_y,
                                                                    sonda_obj.direcao_cardinal,
                                                                    movimento
                                                                    )

    movimento_valido, erro = utils.validar_movimento(proximo_x,
                                                     proximo_y,
                                                     planalto.tamanho_x,
                                                     planalto.tamanho_y)

    if movimento_valido:
        sonda_obj.alterar_posicoes(proximo_x, proximo_y, proxima_direcao)
    else:
        erros.append(erro)

    return sonda_obj, erros
