import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('outputs', exist_ok=True)

def plotar_taxa_churn_geral(df: pd.DataFrame) -> None:
    
    """Gera o gráfico de pizza da taxa de churn geral."""
    
    churn_counts = df['Churn'].value_counts().rename(index={1: 'Sim', 0: 'Não'})
    cores = ['#636EFA', '#EF553B']

    plt.figure(figsize=(6, 6))
    plt.pie(
        churn_counts.values, 
        labels=churn_counts.index, 
        autopct='%1.2f%%',
        startangle=140, 
        colors=cores,
        explode=[0.05 if label == 'Sim' else 0 for label in churn_counts.index]
    )
    plt.title('Taxa de Churn Geral', fontsize=14)
    
    plt.savefig('outputs/taxa_churn_geral.png', dpi=300, bbox_inches='tight')
    plt.close()

def plotar_churn_por_contrato(df: pd.DataFrame) -> None:
    
    """Gera o gráfico de barras por tipo de contrato."""
    
    plt.figure(figsize=(12, 4))
    sns.countplot(data=df, x='Tipo_Contrato', hue='Churn', palette={0: '#636EFA', 1: '#EF553B'})
    plt.title('Taxa de Churn Por Tipo de Contrato', fontsize=14)
    plt.xlabel('\nTipo de Contrato')
    plt.ylabel('Número de Clientes')
    plt.legend(title='Churn (0=Não, 1=Sim)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    plt.savefig('outputs/churn_por_contrato.png', dpi=300, bbox_inches='tight')
    plt.close()

def plotar_distribuicao_fidelidade(df: pd.DataFrame) -> None:
    """
    Gera uma análise de distribuição da fidelidade por churn contendo um Boxplot 
    e um Histograma.
    """
    fig, (ax_box, ax_hist) = plt.subplots(
        2, 1, 
        sharex=True, 
        gridspec_kw={"height_ratios": (0.2, 0.8)}, 
        figsize=(10, 6)
    )
    
    paleta_cores = {0: '#636EFA', 1: '#EF553B'}
    
    # Gráfico de Caixa na parte superior
    sns.boxplot(
        data=df, 
        x='Fidelidade_Meses', 
        y='Churn', 
        hue='Churn',
        orient='h', 
        palette=paleta_cores, 
        ax=ax_box,
        legend=False
    )
    ax_box.set(xlabel='', ylabel='Churn')
    ax_box.set_title('Distribuição da Fidelidade (em Meses) Por Churn\n', fontsize=14)
    
    # Histograma na parte inferior
    sns.histplot(
        data=df, 
        x='Fidelidade_Meses', 
        hue='Churn', 
        element='bars', 
        stat='count', 
        palette=paleta_cores, 
        multiple='layer',
        alpha=0.6,
        ax=ax_hist
    )
    ax_hist.set_xlabel('\nMeses de Fidelidade')
    ax_hist.set_ylabel('Número de Clientes')
    
    plt.tight_layout()
    plt.savefig('outputs/distribuicao_fidelidade.png', dpi=300, bbox_inches='tight')
    plt.close()