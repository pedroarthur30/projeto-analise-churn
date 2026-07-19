import pandas as pd
from src.gerador_dados import gera_dados_churn
from src.exploracao import plotar_taxa_churn_geral, plotar_churn_por_contrato, plotar_distribuicao_fidelidade
from src.modelagem import preparar_dados, treinar_e_avaliar_modelo

def main() -> None:
    
    print("Iniciando o pipeline de Churn da Connecta Telecom...")
    
    # 1. Geração de Dados
    df_churn = gera_dados_churn()
    pd.set_option('display.float_format', lambda x: '%.4f' % x)
    print(f"-> Dados carregados! Formato: {df_churn.shape}")
    
    # 2. Execução da Análise Exploratória
    print("-> Gerando gráficos da análise exploratória na pasta 'outputs/'...")
    plotar_taxa_churn_geral(df_churn)
    plotar_churn_por_contrato(df_churn)
    plotar_distribuicao_fidelidade(df_churn)
    
    # 3. Processamento e Modelagem Estatística
    print("-> Tratando os dados e treinando o modelo de Regressão Logística...")
    X, y = preparar_dados(df_churn)
    _ = treinar_e_avaliar_modelo(X, y)
    
    print("Verifique a pasta 'outputs/' para visualizar as análises visuais geradas.")

if __name__ == "__main__":
    main()