def calcular_total(subtotal, regiao=None):
    # REQ-03: IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN exibir erro
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    # REQ-04: WHILE a região de entrega for 'Norte' ou 'Nordeste', frete de R$ 25,00 (R$ 15,00 + R$ 10,00), exceto se subtotal > 300,00 (frete grátis)
    if regiao in ("Norte", "Nordeste"):
        if subtotal > 300:
            frete = 0.0
        else:
            frete = 25.0
    else:
        # REQ-02: IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN frete grátis
        if subtotal >= 250:
            frete = 0.0
        else:
            # REQ-01: Taxa de frete padrão de R$ 15,00
            frete = 15.0

    # REQ-05: WHEN o valor total for calculado, arredondá-lo para 2 casas decimais
    return round(subtotal + frete, 2)
