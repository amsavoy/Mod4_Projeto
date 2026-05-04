# Script de setup para ambiente de desenvolvimento Python
# Cria ambiente virtual e instala dependências

Write-Host "Criando ambiente virtual (.venv)..."
python -m venv .venv

Write-Host "Ativando ambiente virtual..."
& .\.venv\Scripts\Activate.ps1

Write-Host "Atualizando pip..."
pip install --upgrade pip

Write-Host "Instalando dependências do requirements.txt..."
pip install -r requirements.txt

Write-Host "Ambiente virtual criado e dependências instaladas com sucesso!"