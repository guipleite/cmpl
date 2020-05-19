default:
	clear
	flex -l lex.l
	bison -dv eb.y
	gcc eb.tab.c -ll -ly -o cmpl_parser
	# g++ -o test.tab.c lex.yy.c -lfl