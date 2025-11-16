# 🚀 Deploy Simples no Hugging Face - Passo a Passo

## ⚡ Método Mais Rápido (Interface Web)

### 1. Criar o Space (2 minutos)

1. Acesse: **https://huggingface.co/spaces**
2. Clique em **"Create new Space"**
3. Preencha:
   - **Space name**: `feedback-craft-ai`
   - **SDK**: Selecione **"Gradio"**
   - **Hardware**: Selecione **"CPU basic"** (gratuito)
   - **Visibility**: **Public**
4. Clique em **"Create Space"**

### 2. Upload dos Arquivos (3 minutos)

No Space criado:

1. Clique em **"Files and versions"** (aba superior)
2. Clique em **"Add file"** → **"Upload files"**
3. **Arraste e solte** ou **selecione** os seguintes arquivos:

**Arquivos na raiz:**
- `app.py`
- `requirements.txt`  
- `huggingface.yaml`

**Pastas completas:**
- Arraste a pasta `core/` inteira
- Arraste a pasta `prompts/` inteira

4. Clique em **"Upload X files"**

### 3. Aguardar Build (2-5 minutos)

- O Hugging Face fará build automático
- Você verá os logs em tempo real
- Quando terminar, aparecerá: **"Building"** → **"Running"**

### 4. Pronto! 🎉

Acesse seu Space e teste!

---

## 🔧 Método via Git (Para Atualizações Futuras)

### Pré-requisitos

```bash
# Instalar Git LFS
brew install git-lfs

# Instalar Hugging Face CLI
pip3 install huggingface_hub
```

### Passos

```bash
# 1. Login no Hugging Face
huggingface-cli login
# Cole seu token (crie em: https://huggingface.co/settings/tokens)

# 2. Criar Space (se não existir)
huggingface-cli repo create feedback-craft-ai --type space

# 3. Configurar Git
cd /Users/allanygermanofilgueiras/feedback-craft-ai/feedback-craft-ai
git lfs install
git remote add huggingface https://huggingface.co/spaces/AllanyGFilgueiras/feedback-craft-ai

# 4. Push
git push huggingface main
```

---

## ✅ Checklist de Arquivos

Certifique-se de ter:

- [x] `app.py` (raiz)
- [x] `requirements.txt` (raiz)
- [x] `huggingface.yaml` (raiz)
- [x] `core/__init__.py`
- [x] `core/validators.py`
- [x] `core/prompt_builder.py`
- [x] `core/model_client.py`
- [x] `core/formatters.py`
- [x] `prompts/master_prompt.txt`

---

## 🎯 Seu Space Será:

**URL**: `https://huggingface.co/spaces/AllanyGFilgueiras/feedback-craft-ai`

---

## 💡 Dica

O método via interface web é o mais simples e não requer configuração adicional. Use o método Git apenas para atualizações futuras.

