# Teste Técnico

Este repositório contém a implementação das soluções propostas para o teste técnico para a vaga FullStack Pleno 
na 3S Checkout, desenvolvidas em Python. O projeto foi organizado de forma simples, priorizando legibilidade,
testes automatizados e boas práticas de desenvolvimento.

## Requisitos

- Python 3.11 ou superior
- pip
- git

## Instalação

Acesse o link do repositório e execute:

```bash
git clone git@github.com:Bruno-H-Terto/coding-challenge.git
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando os testes

```bash
pytest
```

## Formatação de código

O projeto utiliza **Black** para formatação automática:

```bash
black .
```

## Análise estática

O projeto utiliza **Ruff** para análise estática e lint:

```bash
ruff check .
```

## Estrutura do projeto

```text
.
├── src/
│   ├── __init__.py
│   ├── question_1.py
│   ├── question_2.py
│   ├── question_3.py
│   └── question_4.py
├── tests/
│   ├── __init__.py
│   ├── test_question_1.py
│   ├── test_question_2.py
│   ├── test_question_3.py
│   └── test_question_4.py
├── requirements.txt
└── README.md
```

## Considerações

As soluções foram desenvolvidas priorizando:

- Clareza e simplicidade do código;
- Tipagem estática com Type Hints;
- Testes automatizados utilizando Pytest;
- Código formatado com Black;
- Análise estática com Ruff;
- Organização em módulos independentes por questão.