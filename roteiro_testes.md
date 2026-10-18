# Roteiro de Testes — Cálculo de Frete (Exercício 7.1)

- **Spec:** specs/checkout_frete.md (REQ-01 a REQ-07)
- **Plataforma:** Windows 11, Python 3.14, pytest, PyCharm
- **Pré-requisito:** .venv ativo com pytest instalado
- **Componentes:** calcular_total(subtotal, regiao) em frete.py e fechar_pedido(itens, regiao, cupom) em carrinho.py
- Resultado obtido e status são preenchidos na execução (exercícios 7.2 a 7.5).

## Testes Unitários (componente único: `calcular_total`)
 
### CT-01 — Frete padrão (REQ-01)
- **Cenário:** cliente do Sudeste com subtotal abaixo do limite de frete grátis
- **Passos:** chamar `calcular_total(100.00, "Sudeste")`
- **Dados:** subtotal R$ 100,00; região Sudeste
- **Resultado esperado:** R$ 115,00
- **Resultado obtido:** R$ 115,00
- **Status:** Sucesso
### CT-02 — Frete grátis no limite (REQ-02)
- **Cenário:** subtotal exatamente no limite e um centavo abaixo
- **Passos:** chamar `calcular_total(250.00)` e `calcular_total(249.99)`
- **Dados:** subtotais R$ 250,00 e R$ 249,99
- **Resultado esperado:** R$ 250,00 (grátis) e R$ 264,99 (paga frete)
- **Resultado obtido:** R$ 250,00 e R$ 264,99
- **Status:** Sucesso
### CT-03 — Carrinho com valor inválido (REQ-03)
- **Cenário:** subtotal zero
- **Passos:** chamar `calcular_total(0.00)`
- **Dados:** subtotal R$ 0,00
- **Resultado esperado:** erro `ValueError("Valor de carrinho inválido")`
- **Resultado obtido:** erro ValueError("Valor de carrinho inválido")
- **Status:** Sucesso
### CT-04 — Adicional da região Norte (REQ-04)
- **Cenário:** cliente do Norte com subtotal abaixo do limite
- **Passos:** chamar `calcular_total(100.00, "Norte")`
- **Dados:** subtotal R$ 100,00; região Norte
- **Resultado esperado:** R$ 125,00 (R$ 15,00 + R$ 10,00 de frete)
- **Resultado obtido:** R$ 125,00
- **Status:** Sucesso
### CT-05 — Arredondamento em 2 casas (REQ-05)
- **Cenário:** subtotal com mais de 2 casas decimais
- **Passos:** chamar `calcular_total(10.126)`
- **Dados:** subtotal R$ 10,126
- **Resultado esperado:** R$ 25,13
- **Resultado obtido:** R$ 25,13
- **Status:** Sucesso
 
## Testes de Integração (`carrinho` + `frete` conectados)
 
### CT-06 — Carrinho calcula subtotal e aplica frete do Norte
- **Cenário:** o carrinho soma os itens e passa o subtotal para o frete
- **Pré-requisito:** `carrinho.py` e `frete.py` disponíveis
- **Passos:** chamar `fechar_pedido([(50.00, 2)], "Norte")`
- **Dados:** 2 itens de R$ 50,00; região Norte
- **Resultado esperado:** R$ 125,00 (subtotal R$ 100,00 + frete R$ 25,00)
- **Resultado obtido:** R$ 125,00
- **Status:** Sucesso
### CT-07 — Soma de itens diferentes atinge o frete grátis
- **Cenário:** vários itens cuja soma chega exatamente ao limite
- **Passos:** chamar `fechar_pedido([(100.00, 1), (75.00, 2)])`
- **Dados:** 1 item de R$ 100,00 e 2 itens de R$ 75,00
- **Resultado esperado:** R$ 250,00 (subtotal R$ 250,00, frete grátis)
- **Resultado obtido:** R$ 250,00
- **Status:** Sucesso
### CT-08 — Carrinho vazio propaga o erro do frete
- **Cenário:** o carrinho não tem itens, então o subtotal é zero
- **Passos:** chamar `fechar_pedido([])`
- **Dados:** lista de itens vazia
- **Resultado esperado:** erro `ValueError("Valor de carrinho inválido")` vindo do `frete`
- **Resultado obtido:** erro ValueError(“Valor de carrinho inválido”)
- **Status:** Sucesso
 
## Testes Funcionais (cenário do cliente, conforme a spec)
 
### CT-09 — Compra comum no Sudeste
- **Cenário:** cliente do Sudeste compra uma camiseta e um boné
- **Passos:** montar o pedido e chamar `fechar_pedido` com os itens e a região
- **Dados:** camiseta R$ 79,90 e boné R$ 49,90; região Sudeste
- **Resultado esperado:** R$ 144,80 (subtotal R$ 129,80 + frete R$ 15,00)
- **Resultado obtido:** R$ 144,80
- **Status:** Sucesso
### CT-10 — Compra grande no Norte ganha frete grátis
- **Cenário:** cliente do Norte compra 3 livros e passa do limite
- **Passos:** montar o pedido e chamar `fechar_pedido` com os itens e a região
- **Dados:** 3 livros de R$ 89,90; região Norte
- **Resultado esperado:** R$ 294,70 (subtotal R$ 269,70 + frete R$ 25,00; atualizado pelo novo REQ-04)
- **Resultado obtido:** R$ 294,70
- **Status:** Sucesso


## Testes da Nova Funcionalidade (cupom, REQ-07)

### CT-11 — Cupom aplica 10% de desconto
- **Cenário:** cliente do Sudeste usa DESCONTO10
- **Passos:** chamar `fechar_pedido([(100.00, 1)], "Sudeste", "DESCONTO10")`
- **Dados:** 1 item de R$ 100,00; cupom DESCONTO10
- **Resultado esperado:** R$ 105,00 (subtotal R$ 90,00 + frete R$ 15,00)
- **Resultado obtido:** R$ 105,00
- **Status:** Sucesso
### CT-12 — Desconto faz perder o frete grátis
- **Cenário:** subtotal acima do limite cai para baixo dele com o desconto
- **Passos:** chamar `fechar_pedido([(260.00, 1)], cupom="DESCONTO10")`
- **Dados:** 1 item de R$ 260,00; cupom DESCONTO10
- **Resultado esperado:** R$ 249,00 (subtotal R$ 234,00 + frete R$ 15,00)
- **Resultado obtido:** R$ 249,00
- **Status:** Sucesso
### CT-13 — Cupom inválido é rejeitado
- **Cenário:** cliente informa um cupom que não existe
- **Passos:** chamar `fechar_pedido([(100.00, 1)], cupom="XYZ")`
- **Dados:** cupom XYZ
- **Resultado esperado:** erro `ValueError("Cupom inválido")`
- **Resultado obtido:** erro ValueError(“Cupom inválido”)
- **Status:** Sucesso