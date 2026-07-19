import pandas as pd
import numpy as np

def gera_dados_churn(num_clientes: int = 2000) -> pd.DataFrame:
    """
    Gera um DataFrame de dados fictícios e realistas de clientes 
    da Connecta Telecom, incluindo ruídos, correlações e valores nulos.
    """
    np.random.seed(42)  

    fidelidade_meses = np.random.randint(1, 73, size=num_clientes)
    
    probs_contrato = []
    for meses in fidelidade_meses:
        if meses < 12:
            probs_contrato.append([0.8, 0.15, 0.05])  # Novos clientes preferem mensal
        elif meses < 48:
            probs_contrato.append([0.4, 0.4, 0.2])    # Clientes médios distribuem mais
        else:
            probs_contrato.append([0.1, 0.3, 0.6])    # Clientes antigos preferem dois anos
            
    tipo_contrato = [np.random.choice(['Mensal', 'Anual', 'Dois anos'], p=p) for p in probs_contrato]
    
    # Adiciona variáveis comportamentais 
    servico_internet = np.random.choice(['Fibra Óptica', 'DSL', 'Não'], size=num_clientes, p=[0.55, 0.35, 0.10])
    chamadas_suporte = np.random.poisson(lam=1.5, size=num_clientes) 
    
    # Fatura Mensal com cálculo base
    fatura_base = {'Mensal': 60, 'Anual': 70, 'Dois anos': 80}
    fatura_mensal = [fatura_base[c] + (fidelidade_meses[i] * 0.15) + np.random.normal(0, 8) for i, c in enumerate(tipo_contrato)]
    fatura_mensal = np.clip(fatura_mensal, 20, 120)
    
    # Injeção de Outliers 
    outlier_indices = np.random.choice(num_clientes, size=int(num_clientes * 0.01), replace=False)
    for idx in outlier_indices:
        fatura_mensal[idx] = np.random.uniform(200, 350)

    # Lógica de Churn 
    prob_churn_log = -2.5
    prob_churn_log += -0.05 * fidelidade_meses
    prob_churn_log += np.array([3.0 if c == 'Mensal' else -1.5 if c == 'Anual' else -2.5 for c in tipo_contrato])
    prob_churn_log += np.array([0.8 if s == 'Fibra Óptica' else -0.5 for s in servico_internet])
    prob_churn_log += 0.4 * chamadas_suporte 
    prob_churn_log += 0.03 * np.array(fatura_mensal)
    
    prob_churn = 1 / (1 + np.exp(-prob_churn_log))
    churn = np.random.binomial(1, prob_churn)

    df = pd.DataFrame({
        'ID_Cliente': range(1, num_clientes + 1),
        'Fidelidade_Meses': fidelidade_meses,
        'Tipo_Contrato': tipo_contrato,
        'Servico_Internet': servico_internet,
        'Chamadas_Suporte': chamadas_suporte,
        'Fatura_Mensal': fatura_mensal,
        'Churn': churn
    })

    # 6. Injetando Valores Nulos (NaNs aleatórios para simular falha no banco de dados)
    nulos_indices = np.random.choice(num_clientes, size=int(num_clientes * 0.03), replace=False)
    df.loc[nulos_indices, 'Fatura_Mensal'] = np.nan

    return df