#!/bin/bash

# Script para fazer push do FeedbackCraft AI para GitHub
# Uso: ./push_to_github.sh SEU-USUARIO

if [ -z "$1" ]; then
    echo "❌ Erro: Forneça seu username do GitHub"
    echo "Uso: ./push_to_github.sh SEU-USUARIO"
    exit 1
fi

USERNAME=$1
REPO_URL="https://github.com/$USERNAME/feedback-craft-ai.git"

echo "🚀 Preparando push para GitHub..."
echo ""

# Verificar se já existe remote
if git remote | grep -q "^origin$"; then
    echo "⚠️  Remote 'origin' já existe. Removendo..."
    git remote remove origin
fi

# Adicionar remote
echo "📦 Adicionando remote GitHub..."
git remote add origin $REPO_URL

# Verificar status
echo ""
echo "📊 Status do repositório:"
git status

echo ""
echo "📝 Últimos commits:"
git log --oneline -5

echo ""
read -p "Deseja fazer push para GitHub? (s/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "⬆️  Fazendo push..."
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Push realizado com sucesso!"
        echo "🌐 Acesse: https://github.com/$USERNAME/feedback-craft-ai"
    else
        echo ""
        echo "❌ Erro no push. Verifique:"
        echo "   1. Repositório criado no GitHub?"
        echo "   2. Autenticação configurada?"
        echo "   3. Permissões corretas?"
    fi
else
    echo "❌ Push cancelado."
fi
