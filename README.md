# 📊 Análise de Churn e Modelagem Preditiva - Connecta Telecom

**Autor:** Pedro Arthur
**GitHub:** [pedroarthur30](https://github.com/pedroarthur30)

> **⚠️ Nota de Esclarecimento:** A empresa "Connecta Telecom" e todos os dados presentes neste repositório são estritamente **fictícios**. O conjunto de dados foi gerado sinteticamente (com injeção de ruídos, outliers e correlações lógicas) com o propósito exclusivo de estudo em Ciência de Dados.

---

## 🎯 O que este projeto faz?

Este projeto simula um cenário real de negócios onde uma empresa de telecomunicações enfrenta uma alta taxa de cancelamento de clientes (Churn). O pipeline automatizado resolve este problema de ponta a ponta através de três etapas:

1. **Geração de Dados Realistas (`gerador_dados.py`):** Cria um banco de dados sintético de 2000 clientes, simulando variáveis contratuais, tempo de fidelidade, número de chamadas ao suporte técnico e inserindo falhas de sistema (valores nulos e outliers) para tornar o desafio mais realista.
2. **Análise Exploratória de Dados (EDA) Automatizada (`exploracao.py`):** Processa os dados e exporta automaticamente gráficos de análise bivariada e de distribuição diretamente para a pasta `outputs/`.
3. **Modelagem Estatística (`modelagem.py`):** Aplica tratamento de dados ausentes (imputação pela mediana), realiza o encoding de variáveis categóricas (One-Hot Encoding) e treina um modelo de **Regressão Logística** usando a biblioteca `statsmodels`.

O resultado final é a extração da **Razão de Chances (Odds Ratio)**, permitindo quantificar matematicamente o peso de cada variável na decisão de cancelamento do cliente.

---

## 📂 Estrutura do Projeto

O código foi construído abandonando o uso de notebooks monolíticos para criar um pipeline executável via terminal.

```text
projeto_analisechurn/
├── outputs/                 # Gráficos gerados automaticamente pela análise
├── src/                     # Código-fonte principal
│   ├── __init__.py
│   ├── exploracao.py        # Módulo de plotagem e salvamento de gráficos
│   ├── gerador_dados.py     # Algoritmo de criação do dataset sintético
│   └── modelagem.py         # Tratamento de dados e Regressão Logística
├── .gitignore               # Arquivos ignorados pelo Git
├── main.py                  # Ponto de entrada (Orquestrador do pipeline)
├── README.md                # Documentação principal
├── RELATORIO.md             # Análise aprofundada dos resultados de negócio
└── requirements.txt         # Dependências do projeto
```


## 🚀 Como Executar

Este projeto foi desenvolvido em ambiente **Linux Ubuntu** e utiliza o **Anaconda (Conda)** para o gerenciamento do ambiente virtual. Siga os passos abaixo para replicar o ambiente e rodar o pipeline completo:

### 1. Clonar o repositório
Abra o seu terminal e clone o projeto do GitHub:
```bash
git clone https://github.com/pedroarthur30/projeto-analise-churn.git
cd cd projeto-analise-churn
```

### 2. Criar o ambiente virtual
Crie um ambiente isolado com Python 3.10 para garantir a compatibilidade:
```bash
conda create --name churn_env python=3.10 -y
conda activate churn_env
```

Caso não utilize o gerenciador Conda, você pode rodar o projeto utilizando as ferramentas nativas do Python
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências
instale as bibliotecas necessárias a partir do arquivo requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Executar o Pipeline
Rode o script principal. Ele cuidará da geração sintética dos dados, da criação dos gráficos e do treinamento da Regressão Logística.
```bash
python main.py
```

## 📈 Resultados Esperados

Ao executar o pipeline, o projeto gera automaticamente:
- Gráficos de distribuição e análise bivariada na pasta `outputs/`;
- Tabela com os coeficientes da Regressão Logística;
- Razão de Chances (Odds Ratio) para interpretação dos fatores que influenciam o churn.





