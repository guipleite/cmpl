%{
#include <stdio.h>
#include <stdlib.h>

extern FILE *fp;
int yylex();
void yyerror(const char *s);

%}

%token FOR WHILE BREAK RETURN
%token IF ELSE PRINTF 
%token NUM ID
%token DOT COMMA SEMI OTHER

%right '='
%token AND OR
%token LE GE NE LT GT PLUS MINUS MULT DIV EQ
%%

start: function-definition 
	 | declaration
	 |
;

declaration: direct-declarator SEMI 
		   | function-reference SEMI 	
		   | error	
;

direct-declarator: ID '=' direct-declarator
			     | ID '=' function-reference
			     | ID COMMA direct-declarator
			     | NUM COMMA direct-declarator
			     | ID PLUS direct-declarator
			     | ID MINUS direct-declarator
			     | ID MULT direct-declarator
			     | ID DIV direct-declarator	
			     | NUM PLUS direct-declarator
			     | NUM MINUS direct-declarator
			     | NUM MULT direct-declarator
			     | NUM DIV direct-declarator
			     | '(' direct-declarator ')'
			     | MINUS '(' direct-declarator ')'
			     | MINUS NUM
			     | MINUS ID
			     | NUM
			     | ID
;

function-reference: ID'(' ')'
			      | ID'('direct-declarator')'
;

function-definition: ID '(' initializer ')' compound-statement 
;

initializer: initializer-lis
;

initializer-lis: initializer-lis COMMA declaration
		       | declaration
;

compound-statement:	'{' statement-list '}'
;

statement-list: statement-list statement
			  |
;

statement: iteration-statement
		 | declaration
		 | for-statement
		 | selection-statement
		 | print-statement
		 | SEMI
;

iteration-statement: WHILE '(' expression ')' statement  
			       | WHILE '(' expression ')' compound-statement 
;

for-statement: FOR '(' expression SEMI expression SEMI expression ')' statement 
			 | FOR '(' expression SEMI expression SEMI expression ')' compound-statement 
			 | FOR '(' expression ')' statement 
			 | FOR '(' expression ')' compound-statement 
;

selection-statement: IF '(' expression ')' statement 
;

print-statement: PRINTF '(' expression ')' SEMI
;

expression: expression LE expression 
		  | expression GE expression
	      | expression NE expression
		  | expression EQ expression
		  | expression GT expression
		  | expression LT expression
		  | direct-declarator
		  |
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
    return 0;
}
         
yyerror(char *s) {
	printf("%d : %s %s\n", yylineno, s, yytext );
}         