"""Testes unitários para a nova regra de frete por região (REQ-04).

Especificação: specs/checkout_frete.md (REQ-04)
"""

from frete import calcular_total


# REQ-04: WHILE a região de entrega for 'Norte' ou 'Nordeste', THE SYSTEM SHALL acrescentar R$ 10,00 à taxa base de frete de R$ 15,00.
# Cenário: Nordeste, subtotal 100.00 -> 125.00
def test_req04_nordeste_subtotal_100():
    # Arrange
    subtotal = 100.00
    regiao = "Nordeste"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 125.00


# REQ-04: WHILE a região de entrega for 'Norte' ou 'Nordeste', THE SYSTEM SHALL acrescentar R$ 10,00 à taxa base de frete de R$ 15,00.
# Cenário: Norte, subtotal 100.00 -> 125.00
def test_req04_norte_subtotal_100():
    # Arrange
    subtotal = 100.00
    regiao = "Norte"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 125.00


# REQ-04: Para 'Norte' ou 'Nordeste', entre 250 e 300 continua pagando R$ 25,00 de frete (substitui o limite do REQ-02).
# Cenário: Nordeste, subtotal 270.00 -> 295.00 (entre 250 e 300 continua pagando R$ 25,00)
def test_req04_nordeste_subtotal_270_entre_250_e_300():
    # Arrange
    subtotal = 270.00
    regiao = "Nordeste"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 295.00


# REQ-04: Exatamente 300.00 não é superior a 300.00, então continua pagando R$ 25,00 de frete.
# Cenário: Norte, subtotal 300.00 -> 325.00 (exatamente 300 não é superior, então paga)
def test_req04_norte_subtotal_300_limite_exato():
    # Arrange
    subtotal = 300.00
    regiao = "Norte"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 325.00


# REQ-04: Se o subtotal do carrinho for superior a R$ 300,00 para Norte ou Nordeste, o frete é grátis.
# Cenário: Nordeste, subtotal 300.01 -> 300.01 (acima de 300, frete grátis)
def test_req04_nordeste_subtotal_300_01_frete_gratis():
    # Arrange
    subtotal = 300.01
    regiao = "Nordeste"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 300.01


# REQ-04: Outras regiões não mudam e seguem a regra geral do REQ-02 (frete grátis a partir de R$ 250,00).
# Cenário: Sudeste, subtotal 270.00 -> 270.00 (outras regiões não mudam)
def test_req04_sudeste_subtotal_270_outras_regioes():
    # Arrange
    subtotal = 270.00
    regiao = "Sudeste"

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == 270.00
