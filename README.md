A Cmpl é uma linguagem que combina características de C e Python para criar uma linguagem de simples uso e fácil entendimento.

EBNF: [ebnf.txt](./ebnf.txt)

Apresentação: [Cmpl.pdf](./Cmpl.pdf)

Compilador: [main.py](./main.py )

Para compilar o programa criado pelo Flex & Bison:

    cd /flxbs
    make

Para analizar o programa com o parser criado pelo Bison:

    ./cmpl_parser ./test.cmpl

Para rodar o compilador da lingugem:

    python3 main.py ./test.cmpl
    
 ##### Guilherme Leite
