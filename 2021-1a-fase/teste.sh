#!/bin/bash

DESAFIO="$1"

# Verifica se o argumento foi passado
if [[ -z "$DESAFIO" ]]; then
    echo 'É necessário informar o desafio'
    exit 1
fi

# Seleciona o comando Python (python ou python3)
PYTHON=$(command -v python >/dev/null 2>&1 && echo "python" || echo "python3")

# Entra no diretório do desafio
if ! cd "$DESAFIO"; then
    echo "Erro: Não foi possível entrar no diretório '$DESAFIO'"
    exit 1
fi

# Cria o diretório 'result' se não existir
mkdir -p result

echo "TESTANDO"

# Executa o script para cada arquivo de entrada
time (
    for i in $(seq 1 $(ls -1 input | wc -l)); do
        $PYTHON "$DESAFIO.py" < "input/$i.txt" > "result/$i.txt"
    done
)

echo "VALIDANDO"

# Compara os arquivos de saída com os resultados esperados
for i in $(seq 1 $(ls -1 input | wc -l)); do
    echo $i
    diff "output/$i.txt" "result/$i.txt"
done
