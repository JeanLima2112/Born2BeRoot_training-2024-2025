cd $1

# Seleciona o comando Python (python ou python3)
PYTHON=$(command -v python >/dev/null 2>&1 && echo "python" || echo "python3")

for i in $(seq 1 $(ls -1 input | wc -l)); do
    $PYTHON $1.py < input/$i.txt > result/$i.txt

    echo $i
    diff output/$i.txt result/$i.txt
done