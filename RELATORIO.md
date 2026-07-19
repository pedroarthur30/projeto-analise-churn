# Relatório Executivo: Análise de Churn e Modelagem Estatística
**Empresa Fictícia:** Connecta Telecom
**Autor:** Pedro Arthur Brandão
**GitHub:** [pedroarthur30](https://github.com/pedroarthur30)

---

## 1. Visão Geral do Problema e Escopo
A Connecta Telecom enfrenta uma taxa de cancelamento de serviços (churn) acima da média do mercado. Este projeto teve como objetivo identificar, por meio de modelagem estatística, quais variáveis comportamentais e contratuais impactam significativamente o risco de um cliente cancelar o serviço. 

A análise utilizou uma amostra de **2000 clientes** e aplicou uma **Regressão Logística** para isolar os fatores de risco e de proteção.

---

## 2. Principais Insights Visuais (Análise Exploratória)

Antes da modelagem, a análise exploratória dos dados revelou comportamentos claros na base de clientes.

### Taxa de Churn por Tipo de Contrato
Fica evidente que a esmagadora maioria dos cancelamentos ocorre no grupo de clientes que possuem contratos flexíveis (mensais).

### Distribuição do Tempo de Fidelidade
Clientes que cancelam o serviço (Churn = Sim) tendem a ter um tempo de vida (fidelidade) drasticamente menor na empresa, concentrando-se nos primeiros meses de assinatura.

---

## 3. Avaliação do Modelo Estatístico

O modelo de Regressão Logística apresentou um **Pseudo R-squared de 0.6105**. Em contextos de ciências sociais e comportamento do consumidor, valores acima de 0.2 a 0.4 já indicam um ajuste excelente. Isso significa que as variáveis escolhidas (tipo de contrato, tempo de fidelidade, número de chamadas ao suporte, etc.) explicam de forma muito robusta os motivos que levam os clientes a evadirem.

### Interpretação da Razão de Chances (Odds Ratio)
A tabela abaixo detalha o impacto de cada variável isolada no risco de cancelamento. 
*   **Valores acima de 1:** Fatores de risco (aumentam a chance de churn).
*   **Valores abaixo de 1:** Fatores de proteção (diminuem a chance de churn).

| Variável | Odds Ratio | Interpretação Prática para o Negócio |
| :--- | :--- | :--- |
| **const** | 0.0029 | *Intercepto estatístico.* É a probabilidade base do modelo quando as demais variáveis são zero. Não gera ação direta de negócio. |
| **Fidelidade_Meses** | 0.9438 | **Fator de Proteção.** A cada mês que o cliente permanece na base, o risco de churn cai em cerca de **5.6%** (1 - 0.9438). Reter o cliente nos primeiros meses é vital. |
| **Chamadas_Suporte** | 1.4779 | **Fator de Risco.** Cada ligação adicional feita para o suporte aumenta a chance de cancelamento em quase **47.8%**. Atrito técnico destrói a retenção rapidamente. |
| **Fatura_Mensal** | 1.0519 | **Fator de Risco.** Para cada R$ 1,00 de aumento na fatura, o risco de evasão sobe cerca de **5.2%**. A base possui alta sensibilidade a preço. |
| **Tipo_Contrato_Dois anos** | 0.4255 | **Fator de Proteção (Forte).** Clientes em contratos bienais possuem um risco **57.4% menor** (1 - 0.4255) de cancelar em comparação ao contrato anual. |
| **Tipo_Contrato_Mensal** | 127.2227 | **Maior Fator de Risco.** Clientes no plano mensal têm uma probabilidade quase **127 vezes maior** de cancelar o serviço. A ausência de fidelidade facilita a troca de provedor. |
| **Servico_Internet_Fibra Óptica** | 3.4004 | **Fator de Risco.** Clientes neste plano possuem **3.4 vezes mais chances** de churn em comparação à tecnologia DSL. Um alerta crítico de qualidade de serviço. |
| **Servico_Internet_Não** | 0.6763 | **Inconclusivo.** O p-valor foi de 0.185 (acima do aceitável de 0.05) e o intervalo de confiança cruza o 1 (0.37 a 1.20). Estatisticamente, não há evidências sólidas de impacto desta variável. |

---

## 4. Recomendações Estratégicas Acionáveis

Com base nas evidências matemáticas extraídas do modelo, recomenda-se à diretoria da Connecta Telecom as seguintes ações imediatas:

1.  **Campanha de Migração de Contratos:** O risco do contrato mensal é o mais alarmante do projeto (aumento de quase 127x na chance de saída). Deve-se estruturar uma campanha de retenção oferecendo descontos agressivos ou upgrades gratuitos para clientes mensais migrarem para planos de um ou dois anos.
2.  **Gatilhos de Customer Success:** O suporte técnico não está conseguindo resolver os problemas de forma definitiva. Como cada nova ligação eleva o risco em 47.8%, deve-se implementar uma regra no sistema: se um cliente ligar pela segunda vez no mesmo mês, o ticket deve escalar automaticamente para uma equipe de retenção de alta prioridade.
3.  **Auditoria Urgente na Fibra Óptica:** Como o produto premium (Fibra) está gerando mais cancelamentos (risco 3.4x maior) do que produtos legados, a equipe de Engenharia de Redes deve iniciar uma investigação imediata sobre estabilidade de conexão, e a equipe de Produto deve avaliar se o preço cobrado está aderente ao valor entregue.