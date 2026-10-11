"""Testes da nova funcionalidade de cupom de desconto.

Roteiro de testes: roteiro_testes.md (CT-11 a CT-13)
Especificação: specs/checkout_frete.md (REQ-07)
"""

import pytest
from carrinho import fechar_pedido


# CT-11 — Cupom aplica 10% de desconto
def test_ct11_cupom_aplica_10_porcento_desconto():
    # Cliente do Sudeste usa DESCONTO10: 1 item de R$ 100,00 -> subtotal R$ 90,00 + frete R$ 15,00 = R$ 105,00
    assert fechar_pedido([(100.00, 1)], "Sudeste", "DESCONTO10") == 105.00


# CT-12 — Desconto faz perder o frete grátis
def test_ct12_desconto_faz_perder_frete_gratis():
    # Subtotal acima do limite cai para baixo dele com o desconto:
    # 1 item de R$ 260,00 com DESCONTO10 -> subtotal R$ 234,00 + frete R$ 15,00 = R$ 249,00
    assert fechar_pedido([(260.00, 1)], cupom="DESCONTO10") == 249.00


# CT-13 — Cupom inválido é rejeitado
def test_ct13_cupom_invalido_rejeitado():
    # Cliente informa cupom inexistente ("XYZ") -> erro ValueError("Cupom inválido")
    with pytest.raises(ValueError, match="Cupom inválido"):
        fechar_pedido([(100.00, 1)], cupom="XYZ")
