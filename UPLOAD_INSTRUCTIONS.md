# 📤 Instruções de Upload - Hugging Face Space

## 🎯 Passo a Passo para Upload

### 1. Acesse o Space Criado

Vá para: `https://huggingface.co/spaces/AllanyGFilgueiras/feedback-craft-ai`

### 2. Abra a Aba "Files and versions"

- Clique na aba **"Files and versions"** (no topo do Space)

### 3. Clique em "Add file"

- Clique no botão **"Add file"** (canto superior direito)
- Selecione **"Upload files"**

### 4. Faça Upload dos Arquivos

#### 📄 Arquivos na Raiz (3 arquivos)

Arraste e solte ou selecione estes arquivos:

1. **`app.py`**
2. **`requirements.txt`**
3. **`huggingface.yaml`**

#### 📁 Pasta `core/` Completa (5 arquivos)

**Opção A: Upload da pasta inteira**
- Arraste a pasta `core/` inteira para a área de upload
- Isso fará upload de todos os arquivos dentro dela

**Opção B: Upload individual**
Se não conseguir arrastar a pasta, faça upload individual de:
1. `core/__init__.py`
2. `core/validators.py`
3. `core/prompt_builder.py`
4. `core/model_client.py`
5. `core/formatters.py`

#### 📁 Pasta `prompts/` Completa (1 arquivo)

**Opção A: Upload da pasta inteira**
- Arraste a pasta `prompts/` inteira

**Opção B: Upload individual**
- `prompts/master_prompt.txt`

### 5. Confirme o Upload

- Verifique que todos os arquivos aparecem na lista
- Clique em **"Upload X files"** (onde X é o número de arquivos)

### 6. Aguarde o Build

- O Hugging Face começará o build automaticamente
- Você verá os logs em tempo real
- Status: "Building" → "Running"
- Tempo estimado: 2-5 minutos

### 7. Teste o Space

- Quando o build terminar, acesse a aba **"App"**
- Teste com um exemplo de feedback
- Verifique se todos os outputs aparecem

---

## ✅ Checklist de Arquivos

Certifique-se de ter enviado:

### Na Raiz:
- [ ] `app.py`
- [ ] `requirements.txt`
- [ ] `huggingface.yaml`

### Pasta `core/`:
- [ ] `core/__init__.py`
- [ ] `core/validators.py`
- [ ] `core/prompt_builder.py`
- [ ] `core/model_client.py`
- [ ] `core/formatters.py`

### Pasta `prompts/`:
- [ ] `prompts/master_prompt.txt`

**Total: 9 arquivos**

---

## 🎯 Estrutura Final no Space

Após o upload, a estrutura deve ficar assim:

```
feedback-craft-ai/
├── app.py
├── requirements.txt
├── huggingface.yaml
├── core/
│   ├── __init__.py
│   ├── validators.py
│   ├── prompt_builder.py
│   ├── model_client.py
│   └── formatters.py
└── prompts/
    └── master_prompt.txt
```

---

## 🐛 Problemas Comuns

### Erro: "Module not found: core"
**Solução**: Certifique-se de que a pasta `core/` foi enviada completamente com todos os 5 arquivos.

### Erro: "File not found: prompts/master_prompt.txt"
**Solução**: Verifique se a pasta `prompts/` foi enviada ou se o arquivo `master_prompt.txt` está na raiz.

### Build falha
**Solução**:
- Verifique os logs do build
- Confirme que `requirements.txt` está correto
- Verifique se `app.py` está na raiz

---

## 💡 Dica

Se você arrastar as pastas `core/` e `prompts/` inteiras, o Hugging Face manterá a estrutura de pastas automaticamente. É mais fácil do que fazer upload arquivo por arquivo!

---

**Pronto! Após o upload, seu Space estará funcionando! 🚀**
