Aqui está um modelo de `README.md` estruturado e focado em destacar as suas competências de integração, engenharia de prompt e desenvolvimento backend para recrutadores.

Copie o conteúdo abaixo e grave-o como `README.md` na raiz do seu projeto.

---

# 🚀 Automação de Triagem de Tickets com IA Local

Este projeto é um microsserviço assíncrono que automatiza a triagem inicial de tickets de suporte de TI. Ele recebe a descrição de um problema, utiliza um modelo de inteligência artificial rodando localmente para inferir o **departamento correto** e o **nível de urgência**, e dispara um alerta estruturado para a equipa via **Discord Webhook**.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI + Uvicorn:** Criação de uma API RESTful de alta performance e documentação interativa automática (Swagger).
* **Ollama:** Execução local de Modelos de Linguagem (LLMs), garantindo privacidade dos dados e zero custo com APIs externas (modelo utilizado: `llama3.1:latest`).
* **Integração Webhook:** Comunicação direta com o Discord utilizando a biblioteca `requests`.

## ⚙️ Arquitetura e Fluxo de Dados

1. O cliente faz um `POST` para o endpoint `/triage-ticket/` enviando a descrição do problema.
2. O sistema formata um *System Prompt* com restrições rígidas (Prompt Engineering) e envia para o Ollama em modo `json`.
3. O LLM analisa o contexto e devolve estritamente um JSON estruturado com as chaves `urgencia` e `departamento`.
4. O backend intercepta esta resposta, formata visualmente os dados num "Card" (Embed) e dispara o alerta para o servidor do Discord.

## 📊 Evidências de Funcionamento (Showcase)

### 1. Inferência Inteligente e Retorno em JSON (Swagger UI)

A IA é capaz de interpretar contextos graves. No exemplo abaixo, a descrição *"O banco de dados de produção corrompeu..."* foi classificada automaticamente com urgência **Crítica** para o departamento de **Banco de Dados**. O sistema força a saída estrita em JSON com sucesso de retorno `HTTP 200`.

### 2. Integração e Alertas no Discord

O ticket processado é enviado instantaneamente para a equipa de suporte através do Discord. A automação inclui formatação condicional de cores (vermelho para urgências críticas).

## 🚀 Como Executar Localmente

**1. Pré-requisitos:**

* Ter o Python instalado.
* Ter o [Ollama](https://ollama.com/) instalado e a correr o modelo `llama3.1:latest`.

**2. Instalação:**

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/automacao-triagem-ia.git
cd automacao-triagem-ia

# Instale as dependências
pip install -r requirements.txt

```

**3. Configuração do Webhook:**
No ficheiro `src/ticket_service.py`, substitua o valor `"COLE_SUA_URL_AQUI"` pelo seu Webhook do Discord.

**4. Execução:**

```bash
python -m src.main

```

Acesse `http://localhost:2023/docs` para testar a aplicação na interface Swagger.

<img width="671" height="193" alt="image" src="https://github.com/user-attachments/assets/cb0aa36c-620f-462d-b330-87d9ebe128a3" />


## 🎯 Próximos Passos (Roadmap)

* Implementar filas de processamento (ex: Celery/RabbitMQ) para picos de volume de tickets.
* Expandir integrações para ferramentas de ITSM completas, como Jira ou Zendesk.
* Adicionar testes unitários automatizados com `pytest`.
