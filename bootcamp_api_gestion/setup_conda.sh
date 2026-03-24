#!/bin/bash
echo "=== Script de Configuración del Entorno Virtual (Conda) ==="
echo ""
echo "Creando el entorno 'bootcamp_git' con Python..."

source ~/miniconda3/etc/profile.d/conda.sh || source ~/anaconda3/etc/profile.d/conda.sh
conda create -n bootcamp_git python=3.10 -y

echo "Activando el entorno e instalando dependencias..."
conda activate bootcamp_git
pip install -r requirements.txt

echo ""
echo "¡Todo listo!"
echo "Para empezar a trabajar, abre tu terminal y ejecuta:"
echo "conda activate bootcamp_git"
