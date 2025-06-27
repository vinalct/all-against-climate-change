# Projeto Extensionista do Curso Técnologo de Banco de Dados

Este repositório contém a infraestrutura e o código para extrair dados da API do OpenWeatherMap, carregar o JSON bruto no BigQuery e orquestrar a execução com Airflow (Cloud Composer) no Google Cloud Platform (GCP).

---

## ✨ Visão Geral

1. **Infraestrutura**: Provisionada via Terraform para:
   - Cloud Composer (Airflow gerenciado)
   - Dataset e tabela no BigQuery (raw)
   - Service Account e permissões necessárias
2. **Código ETL**:
   - ``: consulta a API e retorna JSON
   - ``: insere JSON bruto no BigQuery
3. **DAG Airflow**:
   - ``: extrai e carrega a cada hora
4. **Configuração local**:
   - Variáveis de ambiente via `.env`
   - Dependências em `requirements.txt` e `airflow/requirements.txt`

---

## 📁 Estrutura do Repositório

```
all-against-climate-change/
├── infra/terraform/             # Código Terraform para infra na GCP
│   ├── providers.tf
│   ├── variables.tf
│   ├── main.tf
│   └── outputs.tf
├── .gitignore
├── README.md                    # Este arquivo
├── requirements.txt             # Dependências para testes locais e src/
├── airflow/                     # Configuração do Airflow (Composer)
│   ├── dags/
│   │   └── owm_raw_weather.py
│   └── requirements.txt         # Dependências para Airflow
└── src/                         # Código Python ETL
    ├── extract/openweathermap.py
    └── load/to_bq.py
```

---

## 🚀 Pré-requisitos

- Conta ativa no Google Cloud Platform (GCP)
- Projeto GCP criado e habilitado com:
  - APIs: BigQuery, Cloud Composer
- Terraform >= 1.0 instalado
- Python >= 3.9
- Google Cloud SDK (gcloud) configurado e autenticado

---

## 🔧 Configuração

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/vinalct/all-against-climate-change.git
   cd all-against-climate-change
   ```

2. **Crie o arquivo de variáveis**:

   ```bash
   cp .env.example .env
   # Abra .env e preencha:
   #   OWM_API_KEY=TOKEN_OPENWEATHERMAP
   #   GCP_PROJECT=projeto-gcp
   #   BQ_DATASET=owm_weather
   #   BQ_RAW_TABLE=raw_weather
   ```


