#!/bin/bash

# Script para fazer deploy do FeedbackCraft AI no Hugging Face Spaces
# Uso: ./deploy_to_hf.sh SEU-USUARIO-HF

if [ -z "$1" ]; then
    echo "❌ Erro: Forneça seu username do Hugging Face"
    echo "Uso: ./deploy_to_hf.sh SEU-USUARIO-HF"
    exit 1
fi

USERNAME=$1
SPACE_NAME="feedback-craft-ai"
SPACE_URL="https://huggingface.co/spaces/$USERNAME/$SPACE_NAME"

echo "🤗 Preparando deploy para Hugging Face Spaces..."
echo ""

# Verificar se huggingface-cli está instalado
if ! command -v huggingface-cli &> /dev/null; then
    echo "📦 Instalando Hugging Face CLI..."
    pip3 install -q huggingface_hub[cli]
fi

# Verificar login
echo "🔐 Verificando autenticação..."
if ! huggingface-cli whoami &> /dev/null; then
    echo "⚠️  Você precisa fazer login no Hugging Face"
    echo "   Execute: huggingface-cli login"
    echo "   Ou acesse: https://huggingface.co/settings/tokens"
    echo ""
    read -p "Deseja fazer login agora? (s/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        huggingface-cli login
    else
        echo "❌ Login necessário para continuar"
        exit 1
    fi
fi

# Verificar se git-lfs está instalado
if ! command -v git-lfs &> /dev/null; then
    echo "⚠️  Git LFS não encontrado. Instalando..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install git-lfs
    else
        echo "Por favor, instale git-lfs manualmente: https://git-lfs.github.com/"
        exit 1
    fi
fi

# Inicializar git-lfs
git lfs install

# Verificar se o Space já existe
echo ""
echo "🔍 Verificando se o Space já existe..."
if huggingface-cli repo exists "$USERNAME/$SPACE_NAME" --type space &> /dev/null; then
    echo "✅ Space já existe: $SPACE_URL"
    read -p "Deseja atualizar o Space existente? (s/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        echo "❌ Operação cancelada"
        exit 1
    fi
else
    echo "📦 Criando novo Space..."
    huggingface-cli repo create "$SPACE_NAME" --type space --organization "$USERNAME" || {
        echo "❌ Erro ao criar Space. Verifique se você tem permissões."
        exit 1
    }
    echo "✅ Space criado: $SPACE_URL"
fi

# Adicionar remote do Hugging Face
echo ""
echo "📡 Configurando Git remote..."
if git remote | grep -q "^huggingface$"; then
    echo "⚠️  Remote 'huggingface' já existe. Removendo..."
    git remote remove huggingface
fi

git remote add huggingface "https://huggingface.co/spaces/$USERNAME/$SPACE_NAME"

# Verificar arquivos necessários
echo ""
echo "📋 Verificando arquivos necessários..."
REQUIRED_FILES=("app.py" "requirements.txt" "huggingface.yaml")
MISSING_FILES=()

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -ne 0 ]; then
    echo "❌ Arquivos faltando: ${MISSING_FILES[*]}"
    exit 1
fi

if [ ! -d "core" ] || [ ! -d "prompts" ]; then
    echo "❌ Pastas 'core' ou 'prompts' não encontradas"
    exit 1
fi

echo "✅ Todos os arquivos necessários estão presentes"

# Fazer push
echo ""
echo "⬆️  Fazendo push para Hugging Face Spaces..."
echo "   Isso pode levar alguns minutos..."
echo ""

git push huggingface main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deploy realizado com sucesso!"
    echo ""
    echo "🌐 Acesse seu Space em: $SPACE_URL"
    echo ""
    echo "⏳ O build pode levar 2-5 minutos. Acompanhe em:"
    echo "   $SPACE_URL"
    echo ""
    echo "💡 Dica: Você pode verificar o status do build na aba 'Logs' do Space"
else
    echo ""
    echo "❌ Erro no push. Verifique:"
    echo "   1. Autenticação configurada?"
    echo "   2. Permissões no Space?"
    echo "   3. Git LFS instalado?"
    echo ""
    echo "💡 Alternativa: Faça upload manual dos arquivos via interface web"
fi

