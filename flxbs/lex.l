%{
    #include <stdio.h>
    #include <string.h>
    #include "eb.tab.h"
    void showError();;
%}

identifier   [a−zA−Z_][a−zA−Z0−9_]*
string      "[a−zA−Z_][a−zA−Z0−9_]*"
character    [a−zA−Z_]*
integer      [0-9]*
floating     [0-9]*\.?[0-9]

%%

[ \t]		;
[ \n]   { yylineno = yylineno + 1;}

int                 return(int);
char                return(char);
and                 return(and);
or                  return(or);
">"                 return(greater);
"<"                 return(lesser);
"=="                return(leq);;
"-"                 return(minus);
"+"                 return(plus);
"*"                 return(mult);
"/"                 return(div);
if                  return(if);
else                return(else);
while               return(while);
for                 return(for);
func                return(func);
return              return(return);

";"                 return(endline);
","                 return(comma);
"("                 return(openP);
");"                 return(closeP);
"}"                 return(closeB);
"{"                 return(openB);
"["                 return(openK);
"]"                 return(closeK);

.      		        {showError(); return(OTHER);}

%%

void showError(){
    printf("error");
}