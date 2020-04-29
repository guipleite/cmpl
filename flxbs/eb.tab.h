/* A Bison parser, made by GNU Bison 3.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2019 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_EB_TAB_H_INCLUDED
# define YY_YY_EB_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    char = 258,
    int = 259,
    float = 260,
    void = 261,
    if = 262,
    else = 263,
    while = 264,
    for = 265,
    return = 266,
    break = 267,
    not = 268,
    lesser = 269,
    greater = 270,
    leq = 271,
    plus = 272,
    minus = 273,
    mult = 274,
    div = 275,
    lnot_eq = 276,
    lesser_eq = 277,
    greater_eq = 278,
    eq = 279,
    and = 280,
    or = 281,
    land = 282,
    lor = 283,
    openB = 284,
    closeB = 285,
    openK = 286,
    closeK = 287,
    openP = 288,
    closeP = 289,
    mult_eq = 290,
    div_eq = 291,
    plus_eq = 292,
    minus_eq = 293,
    comma = 294,
    endline = 295,
    identifier = 296,
    string = 297,
    character = 298,
    integer = 299,
    floating = 300,
    enum = 301
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_EB_TAB_H_INCLUDED  */
