"""Testes de unidade para confirmar_frete utilizando Test Doubles (Dummy, Stub e Mock).

Especificação: specs/checkout_frete.md (REQ-08)
Módulo testado: src/expedicao.py
"""

from unittest.mock import Mock

from expedicao import confirmar_frete


# REQ-08 (WHEN): WHEN o frete de um pedido for confirmado, THE SYSTEM SHALL consultar a taxa de frete no ServicoLogisticaAPI, somá-la ao subtotal e chamar uma única vez enviar_notificacao_rastreio(pedido_id) do ServicoNotificacao.
def test_confirmar_frete_com_test_doubles():
    # Arrange
    pedido_id = 101
    subtotal = 100.00

    # Papel: Dummy - Objeto fictício que só preenche o parâmetro 'usuario' e não é usado na lógica
    dummy_usuario = Mock()

    # Papel: Stub - Simula ServicoLogisticaAPI, com consultar_taxa retornando a taxa fixa 20.00, sem chamada de rede
    stub_logistica = Mock()
    stub_logistica.consultar_taxa.return_value = 20.00

    # Papel: Mock - Simula ServicoNotificacao, permitindo verificar a chamada esperada
    mock_notificacao = Mock()

    # Act
    total = confirmar_frete(
        pedido_id,
        subtotal,
        dummy_usuario,
        stub_logistica,
        mock_notificacao,
    )

    # Assert
    assert total == 120.00
    mock_notificacao.enviar_notificacao_rastreio.assert_called_once_with(101)
    assert dummy_usuario.method_calls == []
