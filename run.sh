#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Uso: ./run.sh <entrada.json> <saida.json>"
  exit 1
fi

python src/main.py "$1" "$2"
