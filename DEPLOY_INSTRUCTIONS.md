# 🚀 Instruções de Deploy - FeedbackCraft AI

Este guia fornece instruções passo a passo para fazer deploy do FeedbackCraft AI no GitHub e Hugging Face Spaces.

---

## 📦 Deploy no GitHub

### 1. Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com) e faça login
2. Clique em **"New repository"** (ou acesse https://github.com/new)
3. Configure:
   - **Repository name**: `feedback-craft-ai`
   - **Description**: `Transforme feedbacks rascunhados em comunicações profissionais com IA`
   - **Visibility**: Público (ou Privado, conforme preferir)
   - **NÃO** marque "Initialize with README" (já temos arquivos)
4. Clique em **"Create repository"**

### 2. Conectar Repositório Local ao GitHub

Execute os seguintes comandos no terminal:

```bash
cd /Users/allanygermanofilgueiras/feedback-craft-ai/feedback-craft-ai

# Remover upstream antigo se existir
git branch --unset-upstream 2>/dev/null || true

# Adicionar remote do GitHub (substitua SEU-USUARIO pelo seu username)
git remote add origin https://github.com/SEU-USUARIO/feedback-craft-ai.git

# Ou se preferir SSH:
# git remote add origin git@github.com:SEU-USUARIO/feedback-craft-ai.git

# Verificar remote
git remote -v
```

### 3. Fazer Push dos Commits

```bash
# Fazer push da branch main
git push -u origin main
```

Se pedir autenticação:
- **HTTPS**: Use Personal Access Token (não senha)
- **SSH**: Configure chave SSH primeiro

### 4. Configurar Repositório no GitHub

Após o push, configure:

1. **About** (lado direito do repositório):
   - Website: `https://huggingface.co/spaces/SEU-USUARIO/feedback-craft-ai`
   - Topics: `ai, feedback, llm, gradio, huggingface, python, clean-architecture`

2. **Settings** → **Branches**:
   - Adicionar branch protection para `main` (opcional, mas recomendado)

3. **Releases**:
   - Criar primeira release: `v1.0.0 - MVP Profissional`
   - Seguir template do GITHUB_GUIDE.md

---

## 🤗 Deploy no Hugging Face Spaces

### 1. Criar Conta e Space

1. Acesse [Hugging Face](https://huggingface.co) e faça login (ou crie conta)
2. Clique em **"Spaces"** no menu superior
3. Clique em **"Create new Space"**
4. Configure:
   - **Space name**: `feedback-craft-ai`
   - **SDK**: `Gradio`
   - **Hardware**: `CPU basic` (ou `CPU upgrade` se necessário)
   - **Visibility**: Público
5. Clique em **"Create Space"**

### 2. Fazer Upload dos Arquivos

Você tem duas opções:

#### Opção A: Upload Manual (Recomendado para primeira vez)

1. No Space criado, clique em **"Files and versions"**
2. Clique em **"Add file"** → **"Upload files"**
3. Faça upload dos seguintes arquivos:
   - `app.py`
   - `requirements.txt`
   - `huggingface.yaml`
   - Toda a pasta `core/` (arraste a pasta inteira)
   - Toda a pasta `prompts/` (arraste a pasta inteira)

#### Opção B: Git Push (Recomendado para atualizações)

1. No Space criado, vá em **"Settings"** → **"Repository"**
2. Copie a URL do repositório Git (ex: `https://huggingface.co/spaces/SEU-USUARIO/feedback-craft-ai`)
3. No terminal local:

```bash
# Adicionar remote do Hugging Face
git remote add huggingface https://huggingface.co/spaces/SEU-USUARIO/feedback-craft-ai

# Fazer push
git push huggingface main
```

**Nota**: Para usar Git push no HF, você precisa:
- Instalar `git-lfs`: `brew install git-lfs` (Mac) ou `apt install git-lfs` (Linux)
- Autenticar: `huggingface-cli login`

### 3. Configurar Variáveis de Ambiente (Opcional)

Se quiser usar um modelo específico ou API key:

1. No Space, vá em **"Settings"** → **"Repository secrets"**
2. Adicione:
   - `HF_API_KEY`: Sua chave da API (se necessário)
   - `HF_MODEL_NAME`: Nome do modelo (opcional, já tem default)

### 4. Aguardar Build

- O Hugging Face fará build automático
- Aguarde alguns minutos
- Você verá logs do build em tempo real
- Quando terminar, o Space estará disponível em: `https://huggingface.co/spaces/SEU-USUARIO/feedback-craft-ai`

### 5. Verificar Funcionamento

1. Acesse o Space
2. Teste com um exemplo de feedback
3. Verifique se todos os outputs aparecem corretamente

---

## 🔄 Atualizações Futuras

### Atualizar GitHub

```bash
# Fazer mudanças e commits
git add .
git commit -m "feat: nova funcionalidade"

# Push
git push origin main
```

### Atualizar Hugging Face

```bash
# Se configurou Git remote:
git push huggingface main

# Ou fazer upload manual dos arquivos modificados
```

---

## ✅ Checklist de Deploy

### GitHub
- [ ] Repositório criado
- [ ] Remote configurado
- [ ] Push realizado
- [ ] About configurado
- [ ] Topics adicionados
- [ ] Release v1.0.0 criada

### Hugging Face
- [ ] Space criado
- [ ] Arquivos enviados
- [ ] Build concluído com sucesso
- [ ] Space funcionando
- [ ] Testado com exemplos

---

## 🐛 Troubleshooting

### Erro no Build do Hugging Face

- Verifique se `requirements.txt` está correto
- Confirme que `app.py` está na raiz
- Verifique logs do build para erros específicos

### Erro de Import no Hugging Face

- Certifique-se que a pasta `core/` foi enviada completamente
- Verifique se `__init__.py` existe em `core/`

### Erro de Autenticação no GitHub

- Use Personal Access Token ao invés de senha
- Ou configure SSH keys

---

## 📝 Próximos Passos

Após deploy bem-sucedido:

1. **Atualizar README.md** com links reais:
   - Link do Hugging Face Space
   - Link do GitHub
   - Badges (se quiser)

2. **Compartilhar**:
   - Postar no LinkedIn/Twitter
   - Adicionar ao portfólio
   - Compartilhar com comunidade

3. **Monitorar**:
   - Verificar uso do Space
   - Coletar feedback
   - Planejar melhorias

---

**Boa sorte com o deploy! 🚀**

