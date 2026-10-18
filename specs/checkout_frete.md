# Spec: Checkout — Cálculo de Frete

[ Especificação EARS - Parâmetros do Sistema ]

REQ-01 (Ubiquitous): THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.

REQ-02 (IF/THEN): IF o subtotal do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).

REQ-03 (IF/THEN): IF o subtotal do carrinho for menor ou igual a R$ 0,00, THEN THE SYSTEM SHALL exibir o erro 'Valor de carrinho inválido'.

REQ-04 (WHILE): WHILE a região de entrega for 'Norte', THE SYSTEM SHALL acrescentar R$ 10,00 à taxa de frete. Demais regiões: manter taxa padrão.

REQ-05 (WHEN): WHEN o valor total for calculado, THE SYSTEM SHALL arredondá-lo para 2 casas decimais.

REQ-06 (WHEN): WHEN o pedido for fechado, THE SYSTEM SHALL somar preço × quantidade de cada item do carrinho para obter o subtotal e calcular o total conforme REQ-01 a REQ-05.

REQ-07 (IF/THEN): IF o cliente informar o cupom 'DESCONTO10', THEN THE SYSTEM SHALL aplicar 10% de desconto sobre o subtotal dos itens antes de calcular o frete. Qualquer outro cupom SHALL ser rejeitado com o erro 'Cupom inválido'.

REQ-08 (WHEN): WHEN o frete de um pedido for confirmado, THE SYSTEM SHALL consultar a taxa de frete no ServicoLogisticaAPI, somá-la ao subtotal e chamar uma única vez enviar_notificacao_rastreio(pedido_id) do ServicoNotificacao.
