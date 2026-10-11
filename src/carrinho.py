from frete import calcular_total


# REQ-06 (WHEN): WHEN o pedido for fechado, THE SYSTEM SHALL somar preço × quantidade de cada item do carrinho para obter o subtotal e calcular o total conforme REQ-01 a REQ-05.
def fechar_pedido(itens, regiao=None, cupom=None):
    subtotal = sum(preco * quantidade for preco, quantidade in itens)

    # REQ-07 (IF/THEN): IF o cliente informar o cupom 'DESCONTO10', THEN THE SYSTEM SHALL aplicar 10% de desconto sobre o subtotal dos itens antes de calcular o frete. Qualquer outro cupom SHALL ser rejeitado com o erro 'Cupom inválido'.
    if cupom == "DESCONTO10":
        subtotal *= 0.9
    elif cupom is not None:
        raise ValueError("Cupom inválido")

    return calcular_total(subtotal, regiao)
