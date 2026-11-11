# Tradutor Braille

Tradutor de texto para Braille em Python, **baseado em regras e orientado a tabelas**. O sistema lê arquivos de texto, normaliza o conteúdo e o traduz para Braille em português do Brasil (pt-BR), gerando a saída em formato binário e em Unicode Braille.

> **Status:** em desenvolvimento (protótipo). A estrutura e as interfaces descritas abaixo podem mudar.

## Sumário

- [Visão geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Formatos](#formatos)
- [Como funciona](#como-funciona)
- [Representação das células](#representação-das-células)
- [Tabelas de tradução](#tabelas-de-tradução)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Instalação e uso](#instalação-e-uso)
- [Escopo](#escopo)

## Visão geral

O conhecimento sobre Braille fica nas **tabelas JSON**, e o código apenas as carrega e as aplica. Isso torna o comportamento do sistema fácil de inspecionar e de ajustar: para corrigir uma regra ou suportar outro idioma, altera-se a tabela, e não o programa.

Principais características:

- **Baseado em regras e tabelas**: a mesma entrada sempre produz a mesma saída, sem uso de IA.
- **Organizado em pipeline**: o texto passa por etapas independentes (leitura, normalização, tradução e codificação).
- **Uma tradução, várias saídas**: o motor produz uma representação intermediária única, da qual saem o binário e o Unicode Braille.
- **Extensível**: novos idiomas e novas regras entram como novas tabelas.

## Funcionalidades

- [x] Leitura de arquivos `.txt`
- [x] Leitura de arquivos `.epub`
- [x] Normalização do texto (Unicode NFC, espaços, quebras e tokenização)
- [x] Carregamento e validação das tabelas JSON
- [x] Motor de tradução baseado em tabelas e regras (pt-BR)
- [x] Saída em arquivo binário (`.bin`, com cabeçalho)
- [x] Saída em Unicode Braille (visualização e depuração)
- [x] Interface de linha de comando (CLI)
- [ ] Suporte a outros idiomas por meio de novas tabelas

## Formatos

| | Formato | Situação | Uso |
|---|---|---|---|
| **Entrada** | `.txt` | protótipo | texto simples |
| **Entrada** | `.epub` | protótipo | livros digitais |
| **Saída** | `.bin` com cabeçalho | principal | leitura por dispositivos Braille |
| **Saída** | Unicode Braille (`U+2800` a `U+28FF`) | auxiliar | visualização e depuração |

## Como funciona

```
Arquivo (.txt / .epub)
        │
   ┌────▼─────┐
   │  Readers │  um leitor por formato → blocos de texto (títulos e parágrafos)
   └────┬─────┘
   ┌────▼──────────┐
   │ Normalização  │  Unicode NFC, espaços, quebras, tokenização
   └────┬──────────┘
   ┌────▼──────────┐   ┌──────────────┐
   │ Motor de      │◄──│ Loader e      │  carrega e valida as tabelas JSON
   │ tradução      │   │ validador     │
   └────┬──────────┘   └──────────────┘
        │  representação intermediária: lista de células (0–255)
   ┌────▼──────────┐
   │ Encoders      │  binário (.bin) │ Unicode Braille
   └───────────────┘
```

- **Readers**: cada formato de entrada tem um leitor próprio. Todos devolvem o mesmo formato (uma lista de blocos com tipo e texto), então as etapas seguintes não dependem do formato original. Um seletor escolhe o leitor pela extensão do arquivo.
- **Normalização**: deixa o texto previsível antes da tradução. Unifica a forma dos caracteres acentuados (NFC), padroniza espaços e quebras e divide o texto em palavras.
- **Motor de tradução**: aplica as tabelas e as regras de contexto ao texto normalizado e produz as células Braille. Os dados vêm do loader, que carrega e valida as tabelas.
- **Encoders**: convertem a representação intermediária no formato final.

## Representação das células

Cada célula Braille é guardada como um número, em que cada ponto corresponde a um bit:

| Ponto | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Bit | 0 | 1 | 2 | 3 | 4 | 5 |
| Valor | 1 | 2 | 4 | 8 | 16 | 32 |

Esse mapeamento coincide com o do bloco Unicode Braille. Por isso as duas saídas derivam do mesmo número:

- **Unicode**: `chr(0x2800 + máscara)`
- **Binário**: a própria máscara, gravada como byte

Exemplo: a letra `b` usa os pontos 1 e 2, então a máscara é `3` e o caractere Unicode é `⠃` (`U+2803`).

## Tabelas de tradução

As tabelas ficam em arquivos JSON separados por idioma. Os pontos são escritos como listas, por serem legíveis e fáceis de conferir com a norma, e convertidos em máscara de bits quando a tabela é carregada.

Exemplo ilustrativo (o formato pode mudar durante o desenvolvimento):

```json
{
  "meta": { "id": "pt-br", "idioma": "pt-BR", "versao": "0.1.0", "pontos": 6 },
  "indicadores": { "maiuscula": [6], "numero": [3, 4, 5, 6] },
  "caracteres": { "a": [1], "b": [1, 2], "ç": [1, 2, 3, 4, 6], " ": [] },
  "regras": [
    {
      "id": "sinal-de-numero",
      "quando": { "anterior": "nao_digito", "atual": "digito" },
      "emitir": ["numero"]
    }
  ],
  "fallback": [1, 2, 3, 4, 5, 6]
}
```

| Seção | Função |
|---|---|
| `meta` | identificação da tabela (id, idioma, versão, número de pontos) |
| `indicadores` | sinais que alteram o sentido do que vem depois (maiúscula, número) |
| `caracteres` | símbolo → pontos |
| `regras` | decisões que dependem do contexto (símbolo anterior e atual), avaliadas em ordem |
| `fallback` | célula usada quando o símbolo não existe nas tabelas |

## Estrutura do projeto

```
.
├── tables/
│   └── ptbr/          # tabelas JSON do português do Brasil
├── src/               # leitores, normalização, motor de tradução e encoders
├── tests/
├── requirements.txt
└── README.md
```

## Instalação e uso

**Requisitos:** Python 3.

```bash
git clone https://github.com/LiBraille/Tradutor-Libraille.git
cd Tradutor-Libraille
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Interface:

```bash
# gera o arquivo binário
python -m libraille livro.epub --tabela ptbr --saida livro.bin

# mostra o resultado em Unicode Braille
python -m libraille texto.txt --tabela ptbr --formato unicode
```

## Escopo

**Dentro deste projeto:**

- leitura de arquivos `.txt` e `.epub`;
- normalização do texto;
- tabelas de tradução e motor de tradução (pt-BR);
- geração das saídas em binário e em Unicode Braille.

**Fora deste projeto:**

- o hardware e o software dos dispositivos que consomem a saída;
- aplicações que usam o resultado, como interfaces web.

---

<p align="center">
Desenvolvido por <a href="https://github.com/LiBraille"><b>LiBraille</b></a>
</p>
