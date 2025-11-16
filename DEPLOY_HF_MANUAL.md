# 🤗 Deploy Manual no Hugging Face Spaces

## Opção 1: Via Interface Web (Mais Simples)

### Passo 1: Criar o Space

1. Acesse: https://huggingface.co/spaces
2. Clique em **"Create new Space"**
3. Configure:
   - **Space name**: `feedback-craft-ai`
   - **SDK**: `Gradio`
   - **Hardware**: `CPU basic` (gratuito)
   - **Visibility**: `Public`
4. Clique em **"Create Space"**

### Passo 2: Upload dos Arquivos

No Space criado, vá em **"Files and versions"** → **"Add file"** → **"Upload files"**

**Arquivos para upload:**

1. **Arquivos na raiz:**
   - `app.py`
   - `requirements.txt`
   - `huggingface.yaml`

2. **Pasta `core/` completa:**
   - `core/__init__.py`
   - `core/validators.py`
   - `core/prompt_builder.py`
   - `core/model_client.py`
   - `core/formatters.py`

3. **Pasta `prompts/` completa:**
   - `prompts/master_prompt.txt`

**Dica**: Você pode arrastar as pastas inteiras para fazer upload de todos os arquivos de uma vez.

### Passo 3: Aguardar Build

- O Hugging Face fará build automático
- Aguarde 2-5 minutos
- Acompanhe os logs em tempo real
- Quando terminar, o Space estará disponível!

---

## Opção 2: Via Git (Recomendado para Atualizações)

### Pré-requisitos

```bash
# Instalar Git LFS
brew install git-lfs  # Mac
# ou
apt install git-lfs    # Linux

# Instalar Hugging Face CLI
pip3 install huggingface_hub
```

### Passo 1: Login

```bash
huggingface-cli login
# Cole seu token (crie em: https://huggingface.co/settings/tokens)
```

### Passo 2: Criar Space (se não existir)

```bash
huggingface-cli repo create feedback-craft-ai --type space
```

### Passo 3: Configurar Git

```bash
cd /Users/allanygermanofilgueiras/feedback-craft-ai/feedback-craft-ai

# Inicializar Git LFS
git lfs install

# Adicionar remote do Hugging Face
git remote add huggingface https://huggingface.co/spaces/SEU-USUARIO/feedback-craft-ai

# Fazer push
git push huggingface main
```

---

## Opção 3: Usando o Script Automatizado

```bash
./deploy_to_hf.sh SEU-USUARIO-HF
```

O script irá:
- Verificar dependências
- Fazer login (se necessário)
- Criar o Space (se não existir)
- Fazer push dos arquivos

---

## ✅ Checklist de Arquivos

Certifique-se de ter estes arquivos:

- [x] `app.py`
- [x] `requirements.txt`
- [x] `huggingface.yaml`
- [x] `core/__init__.py`
- [x] `core/validators.py`
- [x] `core/prompt_builder.py`
- [x] `core/model_client.py`
- [x] `core/formatters.py`
- [x] `prompts/master_prompt.txt`

---

## 🐛 Troubleshooting

### Erro: "Module not found: core"

**Solução**: Certifique-se de que a pasta `core/` foi enviada completamente com todos os arquivos.

### Erro: "File not found: prompts/master_prompt.txt"

**Solução**: Verifique se a pasta `prompts/` foi enviada.

### Build falha

**Solução**: 
- Verifique os logs do build
- Confirme que `requirements.txt` está correto
- Verifique se `app.py` está na raiz

### Erro de autenticação Git

**Solução**: 
- Use Personal Access Token ao invés de senha
- Ou configure SSH keys no Hugging Face

---

## 📝 Após o Deploy

1. **Testar o Space**: Acesse e teste com um exemplo
2. **Compartilhar**: Adicione o link no README.md
3. **Monitorar**: Acompanhe uso e feedback

---

**Tempo estimado**: 5-10 minutos (upload manual) ou 2-3 minutos (Git)

