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

```text
(2 * 3) + (4 * 5); 6 - (7 - 8); 9 * (10 / 5); (11 / 3) * 4;
```

Esse é um exemplo do tipo de entrada que será processada e verificada pelos analisadores no sistema de compilação.

### Como executar

Para executar o compilador, siga estas etapas:

1. Adicione a expressão desejada no arquivo `entrada.txt`.
2. Acesse a pasta do projeto.
3. No terminal, execute o seguinte comando:

```bash
python3 compilador.py < entrada.txt > saida.txt
```

Este comando redireciona a entrada do programa para o arquivo entrada.txt e a saída é escrita no arquivo saida.txt. Certifique-se de ter o Python instalado em seu sistema para executar o comando com sucesso.