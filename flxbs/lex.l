%{
    #include <stdio.h>
    #include <string.h>
    #include "eb.tab.h"
    void showError();;
%}

alpha [a-zA-Z]
digit [0-9]

%%

[ \t]		;
[ \n]   { yylineno = yylineno + 1;}

and                 return(AND);
or                  return(OR);
if                  return(IF);
else                return(ELSE);
while               return(WHILE);
for                 return(FOR);
break               return(BREAK);
return              return(RETURN);

{digit}+                    return (NUM);
{alpha}({alpha}|{digit})*   return (ID);
"<="                        return LE;
">="                        return GE;
"=="                        return EQ;
"!="                        return NE;
">"	                        return GT;
"<" 	                    return LT;
"."                         return DOT;
"-"                 return(MINUS);
"+"                 return(PLUS);
"*"                 return(MULT);
"/"                 return(DIV);
";"                 return(SEMI);
","                 return(COMMA);

\/\/.* ;
\/\*(.*\n)*.*\*\/ ;
.                           return yytext[0];

%%

void showError(){
    printf("error");
}
