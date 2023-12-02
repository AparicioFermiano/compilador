# Compilador

Este é um projeto final da disciplina de Teoria da Computação com o objetivo de simular um compilador.

O projeto é composto por analisadores, incluindo analisador léxico, sintático e semântico.

## Funcionamento

A entrada do sistema é o arquivo 'entrada.txt' e passa por uma bateria de testes.

### Formato da Entrada

O arquivo de entrada deve conter várias expressões matemáticas separadas por ';'.

### Análise Léxica

As expressões passam pelo analisador léxico para verificar se contêm apenas números, ponto, parênteses e os operadores ('+', '-', '*', '/').

### Análise Semântica e Sintática

Após a análise léxica, as expressões são submetidas aos analisadores semântico e sintático.

- **Análise Sintática:** Verifica se a sequência de tokens (gerada pela análise léxica) segue as regras da estrutura matemática.
  
- **Análise Semântica:** Garante que a expressão esteja na estrutura correta, considerando a estrutura de uma expressão matemática. Isso inclui verificação se um parêntese aberto foi fechado, se não existem dois operadores sequenciais, entre outros.

### Exemplo

Para exemplificar, o sistema verifica se um parêntese aberto foi fechado corretamente e se não existem operadores consecutivos:

(2 * 3) + (4 * 5); 6 - (7 - 8); 9 * (10 / 5); (11 / 3) * 4;

Esse é um exemplo do tipo de entrada que será processada e verificada pelos analisadores no sistema de compilação.
