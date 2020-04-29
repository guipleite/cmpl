# default:
# 	clear
# 	flex -l lex.l
# 	bison -dv eb.y
# 	gcc lex.yy.c
# 	#g++ -o test.tab.c lex.yy.c -lfl

default:
	clear
	flex -l lex2.l
	bison -dv eb1.y
	gcc eb2.tab.c -ll -ly -o cmpl_parser
	#g++ -o test.tab.c lex.yy.c -lfl