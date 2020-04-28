%{
    #include stdio.h
%}

%token char int float void if else while for return break not lesser greater leq plus minus mult div lnot_eq lesser_eq greater_eq eq comma endline
%token openB closeB openK closeK openP closeP mult_eq div_eq plus_eq minus_eq

identifier string character interger floating

%%

function-definition: declaration-specifier declarator declaration compound-statement
;

declaration-specifier: type-specifier
                     | type-qualifier
;

type-specifier: void
                   | char
                   | int
                   | double
;

specifier-qualifier: type-specifier
                        | type-qualifier
;

declarator:  direct-declarator
;

type-qualifier: const
                   | volatile
;

constant-expression: conditional-expression
;

conditional-expression: logical-or-expression
;

logical-or-expression: logical-and-expression
                          | logical-or-expression lor logical-and-expression
;

logical-and-expression: inclusive-or-expression
                           | logical-and-expression land inclusive-or-expression
;

and-expression: equality-expression
                   | and-expression and equality-expression
;

or-expression: equality-expression
                   | or-expression or equality-expression
;

equality-expression: relational-expression
                        | equality-expression leq relational-expression
                        | equality-expression lnot_eq relational-expression
;

relational-expression: shift-expression
                          | relational-expression lesser  shift-expression
                          | relational-expression greater shift-expression
                          | relational-expression lesser_eq shift-expression
                          | relational-expression greater_eq shift-expression
;

additive-expression: multiplicative-expression
                        | additive-expression plus multiplicative-expression
                        | additive-expression minus multiplicative-expression
;

multiplicative-expression: cast-expression
                              | multiplicative-expression mult cast-expression
                              | multiplicative-expression div cast-expression
;

cast-expression: unary-expression
                    | openP type-name closeP cast-expression
;

unary-expression: postfix-expression
                     | unary-operator cast-expression
;

postfix-expression: primary-expression
                       | postfix-expression openK expression closeK
;

primary-expression: identifier
                       | constant
                       | string
                       | openP expression closeP
;

constant: integer-constant
             | character-constant
             | floating-constant
             | enumeration-constant
;

expression: assignment-expression
               | expression comma assignment-expression
;

assignment-expression: conditional-expression
                          | unary-expression assignment-operator assignment-expression
;

assignment-operator: eq
                        | mult_eq
                        | div_eq
                        | plus_eq
                        | minus_eq
;

unary-operator: 
                   | plus
                   | minus
                   
;

type-name: specifier-qualifier abstract-declarator
;

parameter-type-list: parameter-list
                        | parameter-list comma
;

parameter-list: parameter-declaration
                   | parameter-list comma parameter-declaration
;

parameter-declaration: declaration-specifier declarator
                          | declaration-specifier
;

enum-specifier: enum identifier openB enumerator-list closeB
                   | enum openB enumerator-list closeB
                   | enum identifier
;

enumerator-list: enumerator
                    | enumerator-list comma enumerator
;

enumerator: identifier
               | identifier eq constant-expression
;

typedef-name: identifier
;

declaration:  declaration-specifier init-declarator endline
;

init-declarator: declarator
                    | declarator eq initializer
;

initializer: assignment-expression
                | openB initializer-list closeB
                | openB initializer-list comma closeB
;

initializer-list: initializer
                     | initializer-list comma initializer
;

compound-statement: openB declaration statement closeB
;

statement: expression-statement
              | compound-statement
              | selection-statement
              | iteration-statement

;

expression-statement: expression endline
                        |endline
;

selection-statement: if openP expression closeP statement
                        | if openP expression closeP statement else statement
;

iteration-statement: while openP expression closeP statement
                    | for openP expression endline expression endline expression closeP statement
;