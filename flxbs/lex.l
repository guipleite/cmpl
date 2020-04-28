%{
    #include <stdio.h>
    #include <string.h>
    void showError();
%}

identifier   [a−zA−Z_][a−zA−Z0−9_]*
string      "[a−zA−Z_][a−zA−Z0−9_]*"
character    [a−zA−Z_]*
interger    ([0-9])+
floating     [0-9]*\.?[0-9]

%%

identifier          TOKEN(identifier)
string              TOKEN(string)
int                 TOKEN(int)

and                 TOKEN(and)
or                  TOKEN(or)
">"                 TOKEN(greater)
"<"                 TOKEN(lesser)
"=="                TOKEN(leq)
"-"                 TOKEN(minus)
"+"                 TOKEN(plus)
"*"                 TOKEN(mult)
"/"                 TOKEN(div)

if                  TOKEN(if)
else                TOKEN(else)
while               TOKEN(while)
for                 TOKEN(for)
func                TOKEN(func)

";"                 TOKEN(endline)
","                 TOKEN(comma)
"("                 TOKEN(openP)
")"                 TOKEN(closeP)
"}"                 TOKEN(closeB)
"{"                 TOKEN(openB)
"["                 TOKEN(openK)
"]"                 TOKEN(closeK)

.      		        {showError(); return(OTHER);}

%%

void showError(){
    printf("error");
}