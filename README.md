# Compilador

Projeto final de Teoria da Computação: simula um compilador de expressões matemáticas, com análise léxica, sintática e semântica, e calcula o resultado de cada expressão válida.

## Requisitos

Python 3 (só biblioteca padrão).

## Rodar

```bash
python compilador.py < entrada.txt > saida.txt
```

(Em Linux/macOS pode ser `python3`.) O resultado de cada expressão sai numa linha de `saida.txt`.

## Entrada

`entrada.txt` traz expressões separadas por `;`, com números, ponto, parênteses e `+ - * /`:

```text
(2 * 3) + (4 * 5); 6 - (7 - 8); 9 * (10 / 5); (11 / 3) * 4;
```

## O que cada análise verifica

- **Léxica** — só aparecem números, ponto, parênteses e os quatro operadores.
- **Sintática** — a sequência de tokens segue a estrutura de uma expressão.
- **Semântica** — parênteses abertos são fechados, não há dois operadores seguidos, etc.

## Homologação

Não há ambiente de homologação.
