default:
	clear
	flex -l lex.l
	bison -dv eb.y
	gcc -o test.tab.c lex.yy.c -lfl