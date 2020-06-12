cd /flxbs
make

./cmpl_parser ./test.cmpl

python3 main.py ./test.cmpl
