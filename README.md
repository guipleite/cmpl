A Cmpl é uma linguagem que combina características de C e Python para criar uma linguagem de simples uso e fácil entendimento.

Apresentação: [Cmpl.pdf](./Cmpl.pdf)

Compilador: [main.py](./main.py )

EBNF: [ebnf.txt](./ebnf.txt)

Para compilar o programa criado pelo Flex & Bison:

    (cd ./flxbs && make)

Para analizar o programa com o parser criado pelo Bison:

    ./cmpl_parser ./test.cmpl

Para rodar o compilador da lingugem:

    python3 main.py ./test.cmpl
    
 ##### Guilherme Leite
