%{
#include <stdio.h>
#include <stdlib.h>

extern FILE *fp;
int yylex();
void yyerror(const char *s);

%}

%token INT FLOAT CHAR VOID
%token FOR WHILE 
%token IF ELSE PRINTF RETURN BREAK
%token NUM ID 

%right '='
%token AND OR
%token '<' '>' LE GE EQ NE LT GT

%%

function-definition: declaration-specifier declarator declaration compound-statement
;

declaration-specifier: type-specifier
                    
;

type-specifier: VOID
                   | CHAR
                   | INT
                   | FLOAT
;

specifier-qualifier: type-specifier
                        
;

declarator:  direct-declarator
;

direct-declarator: ID
                 | direct-declarator
                 | direct-declarator constant-expression 
                 | direct-declarator '(' multi-ID ')'
                 | direct-declarator '(' parameter-type-list ')'
                 | '(' declarator ')'

;

constant-expression: conditional-expression
;

conditional-expression: logical-or-expression
;

logical-or-expression: logical-and-expression
                          | logical-or-expression OR logical-and-expression
;

logical-and-expression: logical-or-expression
                           | logical-and-expression AND logical-or-expression
;

and-expression: equality-expression
                   | and-expression AND equality-expression
;

or-expression: equality-expression
                   | or-expression OR equality-expression
;

equality-expression: relational-expression
                        | equality-expression EQ relational-expression
                        | equality-expression NE relational-expression
;

relational-expression: additive-expression
                          | relational-expression LT    additive-expression
                          | relational-expression GT    additive-expression
                          | relational-expression LE    additive-expression
                          | relational-expression GE    additive-expression
;

additive-expression: multiplicative-expression
                        | additive-expression '+' multiplicative-expression
                        | additive-expression '-' multiplicative-expression
;

multiplicative-expression: cast-expression
                              | multiplicative-expression '*' cast-expression
                              | multiplicative-expression '/' cast-expression
;

cast-expression: unary-expression
                    | '(' type-name ')' cast-expression
;

unary-expression: postfix-expression
                     | unary-operator cast-expression
;

postfix-expression: primary-expression
                       | postfix-expression '[' expression ']'
;

primary-expression: ID
                    //    | constant
                    //    | string
                       | '(' expression ')'
;

constant: NUM
             | CHAR
             | FLOAT
;

expression: assignment-expression
               | expression ',' assignment-expression
;

assignment-expression: conditional-expression
                          | unary-expression assignment-operator assignment-expression
;

assignment-operator: '='
;

unary-operator: 
                   | '+'
                   | '-'
                   
;
abstract-declarator: '(' abstract-declarator ')'
                        | '[' constant-expression ']'
                        | abstract-declarator '[' ']'
                        | abstract-declarator '[' constant-expression ']'
                        | abstract-declarator '(' parameter-type-list ')'
                        | '(' parameter-type-list ')'
                        | abstract-declarator '(' ')'
;

type-name: specifier-qualifier abstract-declarator
;

parameter-type-list: parameter-list
                        | parameter-list ','
;

parameter-list: parameter-declaration
                   | parameter-list ',' parameter-declaration
;

parameter-declaration: declaration-specifier declarator
                          | declaration-specifier
;

enumerator-list: enumerator
                    | enumerator-list ',' enumerator
;

enumerator: ID
               | ID '=' constant-expression
;

typedef-name: ID
;

declaration:  declaration-specifier init-declarator ';'
;

init-declarator: declarator
                    | declarator '=' initializer
;

initializer: assignment-expression
                | '{' initializer-list '}'
                | '{' initializer-list ',' '}'
;

initializer-list: initializer
                     | initializer-list ',' initializer
;

compound-statement: '{' declaration statement '}'
;

statement: expression-statement
              | compound-statement
              | selection-statement
              | iteration-statement
              | return-statement

;

multi-ID: | ID
;

expression-statement: expression ';'
                        |';'
;

selection-statement: IF '(' expression ')' statement
                        | IF '(' expression ')' statement ELSE statement
;

iteration-statement: WHILE '(' expression ')' statement
                    | FOR '(' expression ';' expression ';' expression ')' statement
;
return-statement: RETURN expression ';'
                    | RETURN ';'
                    | BREAK ';'
; 

%%
#include"lex.yy.c"
#include<ctype.h>
int count=0;

int main(int argc, char *argv[])
{
	yyin = fopen(argv[1], "r");
	
   if(!yyparse())
		printf("\nParsing complete\n");
	else
		printf("\nParsing failed\n");
	
	fclose(yyin);
    RETURN 0;
}
         
yyerror(char *s) {
	printf("%d : %s %s\n", yylineno, s, yytext );
}         