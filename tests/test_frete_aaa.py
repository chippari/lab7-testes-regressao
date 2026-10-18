"""Testes para o cálculo de frete utilizando estritamente o padrão AAA (Arrange, Act, Assert).

Especificação: specs/checkout_frete.md
Módulo testado: src/frete.py
"""

from frete import calcular_total


# REQ-01: Frete padrão de R$ 15,00 para subtotal inferior a R$ 250,00 (cenário R$ 100,00)
def test_frete_padrao_subtotal_100():
    # Arrange
    subtotal = 100.00
    esperado = 115.00

    # Act
    resultado = calcular_total(subtotal)

    # Assert
    assert resultado == esperado


# REQ-01: Frete padrão de R$ 15,00 para subtotal inferior a R$ 250,00 (cenário R$ 249,99)
def test_frete_padrao_subtotal_249_99():
    # Arrange
    subtotal = 249.99
    esperado = 264.99

    # Act
    resultado = calcular_total(subtotal)

    # Assert
    assert resultado == esperado


# REQ-02: Frete grátis para subtotal igual a R$ 250,00 (cenário de borda R$ 250,00)
def test_frete_gratis_subtotal_250():
    # Arrange
    subtotal = 250.00
    esperado = 250.00

    # Act
    resultado = calcular_total(subtotal)

    # Assert
    assert resultado == esperado


# REQ-02: Frete grátis para subtotal superior a R$ 250,00 (cenário R$ 300,00)
def test_frete_gratis_subtotal_300():
    # Arrange
    subtotal = 300.00
    esperado = 300.00

    # Act
    resultado = calcular_total(subtotal)

    # Assert
    assert resultado == esperado
