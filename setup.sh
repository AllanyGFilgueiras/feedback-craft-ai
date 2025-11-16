#!/bin/bash

# FeedbackCraft AI - Setup Script
# Este script configura o ambiente de desenvolvimento

echo "🎯 FeedbackCraft AI - Setup"
echo "=========================="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.10 ou superior."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION encontrado"

# Criar ambiente virtual
echo ""
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo ""
echo "⬆️  Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo ""
echo "📥 Instalando dependências..."
pip install -r requirements.txt

# Criar arquivo .env se não existir
if [ ! -f .env ]; then
    echo ""
    echo "📝 Criando arquivo .env..."
    cp .env.example .env
    echo "⚠️  Por favor, edite o arquivo .env e adicione sua chave da API do Hugging Face (opcional)"
fi

# Executar testes
echo ""
echo "🧪 Executando testes..."
pytest -v

echo ""
echo "✅ Setup completo!"
echo ""
echo "Para iniciar a aplicação:"
echo "  1. Ative o ambiente virtual: source venv/bin/activate"
echo "  2. Execute: python app.py"
echo ""
echo "Para executar testes:"
echo "  pytest"
echo ""
