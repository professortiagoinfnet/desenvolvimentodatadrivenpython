# Desenvolvimento Data-Driven com Python

Repositório de códigos e exemplos práticos da disciplina **Desenvolvimento Data-Driven com Python**.

A disciplina aborda a construção de aplicações orientadas a dados, iniciando pelo desenvolvimento de APIs com **FastAPI** e avançando para a integração de **modelos de linguagem de grande porte (LLMs)**, **Hugging Face Transformers**, **LangChain**, agentes de IA e aplicações interativas com **Streamlit**.

## Objetivos da disciplina

Ao longo das nove etapas, os estudantes desenvolverão competências para:

- Construir e organizar APIs utilizando FastAPI, incluindo rotas, modelos de dados e tratamento de respostas.
- Integrar modelos de linguagem a aplicações Python por meio do ecossistema Hugging Face.
- Utilizar LangChain para desenvolver aplicações baseadas em LLMs.
- Criar chains, integrar ferramentas e desenvolver agentes para tarefas mais complexas.
- Aplicar padrões de agentes, como ReAct, e gerenciar memória conversacional.
- Construir soluções orientadas a dados que envolvam sumarização, extração estruturada, perguntas e respostas, conversação e recomendação.

## Conteúdo programático

| Etapa | Tema | Principais conteúdos |
| :---: | --- | --- |
| **1** | Introdução ao FastAPI e configuração do ambiente de desenvolvimento | Configuração do ambiente, primeira aplicação, definição de rotas e parâmetros. |
| **2** | Estruturando aplicações em FastAPI | Organização de projetos, modelos de resposta, tratamento de erros HTTP e papel das APIs em ciência de dados. |
| **3** | Apps inteligentes com LLMs, Hugging Face e FastAPI | Componentes de aplicações com LLMs, biblioteca Transformers, pipelines e integração de modelos do Hugging Face com APIs. |
| **4** | Introdução ao framework LangChain | Limitações dos LLMs, componentes do LangChain, configuração, Fake LLMs e integração com OpenAI e Hugging Face. |
| **5** | Tarefas complexas com Chains e LLMs | Composição de chains, integração com ferramentas e desenvolvimento de agentes para automação de tarefas. |
| **6** | ReAct e memória conversacional com LangChain | Padrão ReAct, combinação de raciocínio e ações e memória conversacional. |
| **7** | Aplicações em ciência de dados I | Sumarização de textos, extração estruturada de informações e agentes de perguntas e respostas com LangChain e Streamlit. |
| **8** | Aplicações em ciência de dados II | Agentes com estratégias de raciocínio, aplicações conversacionais e recomendadores de filmes com LLMs, LangChain e Streamlit. |
| **9** | Aplicações em ciência de dados III | Utilização de agentes com LLMs na resolução de problemas de ciência de dados. |

## Tecnologias abordadas

- **Python:** linguagem principal de desenvolvimento.
- **FastAPI:** construção de APIs HTTP.
- **Pydantic:** definição e validação de modelos de dados.
- **Uvicorn:** servidor ASGI para executar aplicações FastAPI.
- **Hugging Face Transformers:** acesso e execução de modelos de linguagem.
- **LangChain:** integração e composição de componentes de aplicações com LLMs.
- **OpenAI API:** integração com modelos por API.
- **Streamlit:** desenvolvimento de interfaces interativas para aplicações orientadas a dados.

> As tecnologias são introduzidas progressivamente, conforme o conteúdo de cada etapa.

## Organização do repositório

Os exemplos das duas primeiras etapas estão organizados da seguinte maneira:

```text
.
├── etapa1/
│   ├── app.py
│   ├── model.py
│   ├── todo.py
│   └── test.py
├── etapa2/
│   ├── app.py
│   ├── model.py
│   ├── todo.py
│   └── test.py
└── README.md
```

As demais etapas fazem parte do planejamento da disciplina e poderão ser incorporadas progressivamente ao repositório.

### Etapa 1 — Introdução ao FastAPI

Os exemplos incluem:

- Instanciação da aplicação `FastAPI` e inclusão de um `APIRouter`.
- Definição de rotas HTTP `GET` e `POST`.
- Recebimento de parâmetros de consulta (*query parameters*) e de caminho (*path parameters*).
- Definição de um modelo `Todo` com Pydantic para receber dados estruturados.
- Armazenamento demonstrativo de itens em listas e dicionários em memória.
- Realização de uma requisição HTTP simples utilizando `requests`.

### Etapa 2 — Estruturando aplicações em FastAPI

A segunda etapa retoma os exemplos iniciais e introduz:

- Separação entre inicialização da aplicação (`app.py`), modelos (`model.py`) e rotas (`todo.py`).
- Definição do modelo de saída `TodoOut`.
- Utilização de `response_model` para controlar os campos retornados por endpoints.
- Respostas com modelos individuais e listas de modelos.

> **Nota:** o tratamento de exceções HTTP integra o conteúdo programático da etapa 2, mas não está demonstrado nos arquivos fornecidos até aqui. Os exemplos utilizam armazenamento em memória, sem persistência em banco de dados.

## Como executar os exemplos

### 1. Preparar o ambiente

É necessário ter o Python instalado. Na raiz do projeto, crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências necessárias para executar os exemplos iniciais:

```powershell
python -m pip install fastapi "uvicorn[standard]" requests
```

Essas dependências são suficientes para as duas primeiras etapas apresentadas neste repositório; as etapas posteriores poderão exigir bibliotecas adicionais.

### 2. Executar a API

A partir da raiz do repositório, entre na pasta da etapa desejada. Por exemplo, para executar a etapa 1:

```powershell
cd etapa1
python -m uvicorn app:app --port 8000 --reload
```

Para a etapa 2, execute o mesmo comando a partir de `etapa2`.

### 3. Acessar e testar

Com o servidor em execução, acesse:

| Endereço | Descrição |
| --- | --- |
| <http://127.0.0.1:8000/> | Rota inicial da aplicação. |
| <http://127.0.0.1:8000/status> | Consulta de status. |
| <http://127.0.0.1:8000/todo> | Consulta dos itens armazenados em memória. |
| <http://127.0.0.1:8000/docs> | Documentação interativa Swagger UI. |
| <http://127.0.0.1:8000/redoc> | Documentação alternativa ReDoc. |

O arquivo `test.py`, presente em ambas as pastas, contém um exemplo de requisição à rota inicial utilizando `requests`:

```powershell
python test.py
```

> **Importante:** mantenha o servidor Uvicorn em execução em outro terminal antes de executar `test.py`. Os dados mantidos em memória são reiniciados quando o processo da aplicação é encerrado ou recarregado.

## Progressão de aprendizagem

A disciplina segue uma sequência que parte da infraestrutura de aplicações e avança até soluções orientadas a dados com LLMs:

**APIs com FastAPI** → **Integração de LLMs** → **LangChain** → **Chains e agentes** → **ReAct e memória** → **Aplicações de ciência de dados com Streamlit**.

---

**Finalidade do repositório:** apoiar o acompanhamento das aulas, a consulta aos exemplos e a evolução das aplicações desenvolvidas ao longo da disciplina.
