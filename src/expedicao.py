class ServicoLogisticaAPI:
    def consultar_taxa(self):
        raise NotImplementedError


class ServicoNotificacao:
    def enviar_notificacao_rastreio(self, pedido_id):
        raise NotImplementedError


# REQ-08: WHEN o frete de um pedido for confirmado, THE SYSTEM SHALL consultar a taxa de frete no ServicoLogisticaAPI, somá-la ao subtotal e chamar uma única vez enviar_notificacao_rastreio(pedido_id) do ServicoNotificacao.
def confirmar_frete(pedido_id, subtotal, usuario, servico_logistica, servico_notificacao):
    taxa = servico_logistica.consultar_taxa()
    servico_notificacao.enviar_notificacao_rastreio(pedido_id)
    return subtotal + taxa
