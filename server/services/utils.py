movimentos = {
    "N": {"L": "W", "R": "E", "M": {"y": 1, "x": 0}},
    "E": {"L": "N", "R": "S", "M": {"y": 0, "x": 1}},
    "S": {"L": "E", "R": "W", "M": {"y": -1, "x": 0}},
    "W": {"L": "S", "R": "N", "M": {"y": 0, "x": -1}}
}


def proximo_movimento(x_atual, y_atual, direcao_atual, movimento):
    """
        Verifica qual o próximo movimento
    """

    if movimento == "M":
        x_atual = x_atual + movimentos[direcao_atual][movimento]['x']
        y_atual = y_atual + movimentos[direcao_atual][movimento]['y']
    else:
        direcao_atual = movimentos[direcao_atual][movimento]

    return x_atual, y_atual, direcao_atual


def validar_movimento(x_atual, y_atual, x_maximo, y_maximo):
    """
        Verifica se o movimento a ser realizado é válido
    """
    if x_atual < 0 or x_atual > x_maximo:
        return False, "A movimentação no eixo X é inválida. Esse movimento foi ignorado."
    if y_atual < 0 or y_atual > y_maximo:
        return False, "A movimentação no eixo Y é inválida. Esse movimento foi ignorado."

    return True, None

