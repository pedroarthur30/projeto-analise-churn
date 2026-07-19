import pandas as pd
import numpy as np
import statsmodels.api as sm
from typing import Tuple, Any

def preparar_dados(df_churn: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prepara os dados originais para a modelagem estatística, tratando valores nulos,
    realizando o encoding das variáveis categóricas e isolando as variáveis.
    """
    # tratamento de valores nulos
    mediana_fatura = df_churn['Fatura_Mensal'].median()
    df_churn['Fatura_Mensal'] = df_churn['Fatura_Mensal'].fillna(mediana_fatura)
    
    # 2. encodiing das variáveis categóricas
    df_model = pd.get_dummies(
        df_churn, 
        columns=['Tipo_Contrato', 'Servico_Internet'], 
        drop_first=True, 
        dtype=int
    )
    
    y = df_model['Churn']
    X = df_model.drop(['ID_Cliente', 'Churn'], axis=1)
    
    X = sm.add_constant(X)
    
    return X, y

def treinar_e_avaliar_modelo(X: pd.DataFrame, y: pd.Series) -> Any:
    """
    Treina um modelo de Regressão Logística para prever a probabilidade de churn
    e imprime as razões de chance (Odds Ratio) para avaliação de impacto.
    """
    modelo = sm.Logit(y, X)
    modelo_treinado = modelo.fit(disp=False) 
    
    params = modelo_treinado.params
    conf = modelo_treinado.conf_int()
    conf['Odds Ratio'] = params
    conf.columns = ['2.5%', '97.5%', 'Odds Ratio']
    conf = np.exp(conf)
    
    print("\nResumo do Modelo:")
    print(modelo_treinado.summary())
    print("\nRazão de Chances (Odds Ratio):")
    print(conf)
    
    return modelo_treinado