"""Suíte de testes para cálculo de frete no checkout.

Especificação: specs/checkout_frete.md
Task: tasks/TASK-01.md
Constituição: constitution.md
"""

import pytest
from frete import calcular_total


# REQ-01 (Ubiquitous): THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
def test_req01_adiciona_frete_padrao_ao_subtotal():
    # Subtotal de R$ 100,00 + frete padrão de R$ 15,00 = R$ 115,00
    assert calcular_total(100.0) == 115.00
    # Subtotal de R$ 50,00 + frete padrão de R$ 15,00 = R$ 65,00
    assert calcular_total(50.0) == 65.00


# REQ-02 (IF/THEN): IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
def test_req02_frete_gratis_para_subtotal_maior_ou_igual_250():
    # Limite exato: R$ 250,00 deve ter frete grátis
    assert calcular_total(250.0) == 250.00
    # Valor acima do limite: R$ 300,00 deve ter frete grátis
    assert calcular_total(300.0) == 300.00
    # Logo abaixo do limite: R$ 249.99 deve cobrar taxa de frete padrão
    assert calcular_total(249.99) == 264.99
    # Frete grátis para outras regiões (ex: Sudeste) quando subtotal >= 250,00
    assert calcular_total(250.0, regiao="Sudeste") == 250.00


# REQ-03 (IF/THEN): IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN THE SYSTEM SHALL exibir o erro 'Valor de carrinho inválido'.
def test_req03_erro_subtotal_menor_ou_igual_a_zero():
    # Subtotal igual a R$ 0,00
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_total(0.0)

    # Subtotal negativo (menor que zero)
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_total(-10.0)


# REQ-04 (WHILE): WHILE a região de entrega for 'Norte' ou 'Nordeste', THE SYSTEM SHALL acrescentar R$ 10,00 à taxa base de frete de R$ 15,00. Demais regiões: manter taxa padrão.
def test_req04_acrescimo_regiao_norte_e_manutencao_demais_regioes():
    # Regiões Norte e Nordeste: taxa padrão (R$ 15,00) + R$ 10,00 = R$ 25,00
    assert calcular_total(100.0, regiao="Norte") == 125.00
    assert calcular_total(100.0, regiao="Nordeste") == 125.00

    # Demais regiões: taxa padrão (R$ 15,00)
    assert calcular_total(100.0, regiao="Sudeste") == 115.00
    assert calcular_total(100.0, regiao="Sul") == 115.00
    assert calcular_total(100.0, regiao="Centro-Oeste") == 115.00


# REQ-05 (WHEN): WHEN o valor total for calculado, THE SYSTEM SHALL arredondá-lo para 2 casas decimais.
def test_req05_arredondamento_duas_casas_decimais():
    # Arredondamento para 2 casas decimais em cálculos com casas fracionárias adicionais
    assert calcular_total(10.126) == 25.13
    assert calcular_total(10.123) == 25.12
    assert calcular_total(100.555) == 115.56
