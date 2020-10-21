from server.services import planalto_service, sonda_service


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
        movimento_valido, erro = planalto.verificar_limite(sonda['sonda_inicial']['posicao_x'],
                                                           sonda['sonda_inicial']['posicao_y'])

        sonda_obj = sonda['sonda_inicial']

        if movimento_valido:
            sonda_obj = sonda_service.criar_sonda(planalto, sonda['sonda_inicial'])
            for movimento in sonda['movimentos']:
                movimento_valido, erro = sonda_obj.movimentar_sonda(movimento)

                if not movimento_valido:
                    erros.append(erro)
        else:
            erros.append("Você tentou aterrisar a sonda fora do planalto. Vamos fingir que nada aconteceu...")

        sondas_final.append({
            "sonda": str(sonda_obj),
            "avisos": erros if erros else ["Não houve nenhum problema, conseguimos realizar todos movimentos!"]
        })

    return sondas_final
