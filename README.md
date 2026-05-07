# Sistema de Monitoramento de Fake News

Sistema simples para cadastro e classificação de notícias quanto à
qualidade da informação. O usuário pode registrar uma notícia informando a
classificação manualmente ou solicitar uma análise automática que considera
ausência de fonte declarada, presença de linguagem sensacionalista e
tamanho do texto.

Este projeto é o **Trabalho da Unidade I** da disciplina
**DIM0501 — Boas Práticas de Programação (UFRN, 2026.1)** e consiste em
refatorar um código inicial propositalmente mal estruturado, preservando
seu funcionamento externo.

## Requisitos

- Python 3.9 ou superior (uso de `dataclasses`, anotações de tipo modernas).

Não há dependências externas: o sistema usa apenas a biblioteca padrão.

## Como executar

A partir da raiz do projeto:

```bash
python main.py
```

O sistema iniciará no menu principal de linha de comando.

## Funcionalidades

- **Adicionar manualmente** — o usuário fornece o texto e a classificação
  (`confiavel`, `duvidosa` ou `falsa`). Se a classificação for omitida,
  assume `duvidosa`.
- **Adicionar automaticamente** — o sistema classifica o texto aplicando
  heurísticas simples de qualidade.
- **Listar** — exibe todas as notícias cadastradas na sessão atual.
- **Sair** — encerra o programa.

## Critérios da classificação automática

Cada indício abaixo soma um ponto. A pontuação total define a classificação.

| Indício                                           | Critério                  |
|---------------------------------------------------|---------------------------|
| Ausência de fonte declarada                       | `"FONTE"` não está no texto |
| Linguagem sensacionalista (excesso de exclamação) | `"!!!"` aparece no texto    |
| Linguagem sensacionalista (urgência)              | `"URGENTE"` aparece no texto |
| Texto muito curto                                 | menos de 10 caracteres      |

| Pontuação | Classificação |
|-----------|---------------|
| 0         | `confiavel`   |
| 1         | `duvidosa`    |
| 2 ou mais | `falsa`       |

## Estrutura do Projeto

```
projeto/
├── modelo/                    # Entidades de domínio
│   ├── __init__.py
│   └── noticia.py             # Noticia (dataclass) e Classificacao (Enum)
├── servico/                   # Regras de negócio
│   ├── __init__.py
│   ├── analisador.py          # Heurística de classificação automática
│   └── repositorio.py         # Armazenamento em memória das notícias
├── interface/                 # Camada de apresentação (CLI)
│   ├── __init__.py
│   └── cli.py                 # Menu, leitura de entradas e formatação
├── original/                  # Código inicial preservado para referência
│   └── Sistema.py
├── main.py                    # Ponto de entrada
├── README.md
└── RELATORIO_TECNICO.md       # Relatório técnico do trabalho
```

## Arquitetura

A separação de responsabilidades segue uma divisão clássica em camadas:

- `modelo/`: define **o que** é uma notícia. Não conhece a lógica de
  classificação nem como ela é exibida.
- `servico/`: define **as regras de negócio** — analisar um texto e
  guardar notícias. Depende apenas de `modelo/`.
- `interface/`: define **como** o usuário interage com o sistema. Depende
  de `servico/` e `modelo/`, mas não o contrário.
- `main.py`: monta tudo e inicia o loop principal.

Essa direção de dependências (interface → serviço → modelo) facilita
trocar a CLI por outra interface (ex.: web) sem alterar a lógica de
negócio.

## Boas práticas aplicadas

- Nomes descritivos em português, conforme o domínio do problema.
- Funções pequenas e com uma única responsabilidade.
- Constantes nomeadas em vez de números/strings mágicos.
- `Enum` para classificações em vez de strings espalhadas.
- `dataclass` imutável para a entidade `Noticia`.
- Anotações de tipo (`type hints`) em todos os parâmetros e retornos.
- Docstrings nos módulos, classes e funções públicas.
- Validação de entradas e tratamento de `EOFError`/`KeyboardInterrupt`.
- Mapeamento opção → ação no menu, evitando longas cadeias de `if/elif`.
