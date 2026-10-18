"""Testes funcionais simulando cenários do cliente conforme a especificação.

Roteiro de testes: roteiro_testes.md (CT-09 e CT-10)
Especificação: specs/checkout_frete.md
"""

import pytest

from carrinho import fechar_pedido

# CT-09 — Compra comum no Sudeste
def test_ct09_compra_comum_sudeste():
    # Cliente do Sudeste compra uma camiseta (R$ 79,90) e um boné (R$ 49,90)
    itens = [
        (79.90, 1),  # Camiseta
        (49.90, 1),  # Boné
    ]
    # Subtotal R$ 129,80 + frete padrão R$ 15,00 = R$ 144,80
    assert fechar_pedido(itens, "Sudeste") == 144.80


# CT-10 — Compra grande no Norte paga frete regional
def test_ct10_compra_grande_norte_paga_frete_regional():
    # Cliente do Norte compra 3 livros de R$ 89,90
    itens = [
        (89.90, 3),  # 3 Livros
    ]
    # Subtotal R$ 269,70 + frete regional R$ 25,00 (não passa de R$ 300,00) = R$ 294,70
    assert fechar_pedido(itens, "Norte") == 294.70
