# 📚 Guia GitHub - FeedbackCraft AI

Este guia fornece instruções completas para configurar e gerenciar o repositório GitHub do FeedbackCraft AI.

---

## 📋 Sumário

- [Estrutura do Repositório](#estrutura-do-repositório)
- [Configuração Inicial](#configuração-inicial)
- [Mensagens de Commit](#mensagens-de-commit)
- [Branches](#branches)
- [Releases](#releases)
- [Issues e Pull Requests](#issues-e-pull-requests)
- [Boas Práticas](#boas-práticas)

---

## 📁 Estrutura do Repositório

### Estrutura Recomendada

```
feedback-craft-ai/
├── .github/
│   ├── workflows/          # GitHub Actions (CI/CD)
│   │   └── test.yml
│   └── ISSUE_TEMPLATE/     # Templates de issues
│       ├── bug_report.md
│       └── feature_request.md
├── docs/                   # Documentação adicional
│   ├── api.md
│   └── deployment.md
├── core/                   # Código principal
├── prompts/                # Templates
├── tests/                  # Testes
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
├── PRODUCT_VISION.md
└── GITHUB_GUIDE.md
```

---

## 🚀 Configuração Inicial

### 1. Criar Repositório

1. Acesse [GitHub](https://github.com)
2. Clique em "New repository"
3. Configure:
   - **Nome**: `feedback-craft-ai`
   - **Descrição**: "Transforme feedbacks rascunhados em comunicações profissionais com IA"
   - **Visibilidade**: Público (ou Privado)
   - **Initialize**: Não marque nenhuma opção (já temos arquivos)

### 2. Descrição Curta do Repositório

```
Transforme feedbacks rascunhados em comunicações profissionais, claras e acionáveis usando IA
```

### 3. Descrição Longa (About)

```
FeedbackCraft AI é uma ferramenta profissional que utiliza modelos de linguagem para melhorar feedbacks, tornando-os claros, respeitosos, objetivos e acionáveis. Desenvolvido com arquitetura limpa, testes unitários completos e pronto para produção.
```

### 4. Topics (Tags)

```
ai, feedback, llm, gradio, huggingface, python, clean-architecture, professional-communication, nlp, machine-learning
```

### 5. Website (se tiver)

```
https://huggingface.co/spaces/seu-usuario/feedback-craft-ai
```

---

## 💬 Mensagens de Commit

### Padrão Recomendado

Use o padrão **Conventional Commits**:

```
<tipo>(<escopo>): <descrição curta>

[corpo opcional]

[rodapé opcional]
```

### Tipos de Commit

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças em documentação
- `style`: Formatação, ponto e vírgula, etc (não afeta código)
- `refactor`: Refatoração de código
- `test`: Adição ou correção de testes
- `chore`: Tarefas de manutenção, build, etc

### Exemplos de Commits

```bash
# Feature
git commit -m "feat(core): adiciona validação de feedback text"

# Fix
git commit -m "fix(app): corrige erro ao processar texto vazio"

# Docs
git commit -m "docs(readme): atualiza instruções de instalação"

# Test
git commit -m "test(validators): adiciona testes para edge cases"

# Refactor
git commit -m "refactor(model_client): simplifica lógica de parsing"

# Chore
git commit -m "chore(deps): atualiza gradio para 4.0.1"
```

### Commits com Corpo

```bash
git commit -m "feat(app): adiciona botão de copiar

- Implementa funcionalidade de copiar texto completo
- Adiciona feedback visual ao copiar
- Melhora UX com mensagem de confirmação"
```

---

## 🌿 Branches

### Estrutura de Branches Recomendada

```
main                    # Produção (protegida)
├── develop             # Desenvolvimento
├── feature/xxx         # Features
├── fix/xxx             # Correções
├── docs/xxx            # Documentação
└── release/v1.x.x      # Preparação de release
```

### Branches Principais

#### `main`
- **Proteção**: Sim (requer PR e aprovação)
- **Uso**: Código de produção
- **Merge**: Apenas via Pull Request de `develop` ou `release/*`

#### `develop`
- **Proteção**: Opcional
- **Uso**: Integração de features
- **Merge**: Features e fixes são mergeados aqui primeiro

### Branches de Trabalho

#### `feature/nome-da-feature`
```bash
# Criar
git checkout -b feature/adicionar-cache develop

# Trabalhar e commitar
git commit -m "feat(cache): implementa cache de resultados"

# Push
git push origin feature/adicionar-cache

# Criar PR para develop
```

#### `fix/nome-do-fix`
```bash
# Criar
git checkout -b fix/corrige-validacao develop

# Trabalhar e commitar
git commit -m "fix(validators): corrige validação de texto vazio"

# Push e criar PR
```

#### `docs/nome-da-doc`
```bash
# Criar
git checkout -b docs/atualiza-readme develop

# Trabalhar e commitar
git commit -m "docs(readme): adiciona seção de troubleshooting"
```

### Exemplo de Fluxo

```bash
# 1. Criar feature branch
git checkout develop
git pull origin develop
git checkout -b feature/export-pdf

# 2. Trabalhar e commitar
git add .
git commit -m "feat(export): adiciona exportação em PDF"

# 3. Push
git push origin feature/export-pdf

# 4. Criar PR no GitHub (feature/export-pdf → develop)

# 5. Após merge, deletar branch local
git checkout develop
git pull origin develop
git branch -d feature/export-pdf
```

---

## 🏷️ Releases

### Estrutura de Versionamento

Use **Semantic Versioning** (SemVer):

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Mudanças incompatíveis
- **MINOR**: Novas funcionalidades (compatíveis)
- **PATCH**: Correções de bugs

### Criar Release

#### 1. Preparar Release Branch

```bash
# Criar branch de release
git checkout -b release/v1.0.0 develop

# Atualizar versão nos arquivos
# - __init__.py
# - README.md
# - CHANGELOG.md (se tiver)

# Commit
git commit -m "chore(release): prepara versão 1.0.0"
git push origin release/v1.0.0
```

#### 2. Criar Release no GitHub

1. Acesse **Releases** → **Draft a new release**
2. **Tag**: `v1.0.0`
3. **Target**: `release/v1.0.0` ou `main`
4. **Title**: `v1.0.0 - MVP Profissional`
5. **Description**:

```markdown
## 🎉 Primeira Release - MVP Profissional

### ✨ Funcionalidades
- Interface Gradio intuitiva
- Melhoria de feedback com IA
- Múltiplos formatos de saída
- Personalização (tipo, tom, formalidade)
- Validação robusta
- Testes unitários completos

### 🐛 Correções
- N/A (primeira versão)

### 📚 Documentação
- README completo
- Visão de produto
- Guia GitHub

### 🚀 Deploy
- Configurado para Hugging Face Spaces
- Pronto para produção
```

6. Marque como **Pre-release** se for beta
7. Clique em **Publish release**

#### 3. Merge para Main e Develop

```bash
# Merge para main
git checkout main
git merge release/v1.0.0
git tag v1.0.0
git push origin main --tags

# Merge para develop
git checkout develop
git merge release/v1.0.0
git push origin develop

# Deletar branch de release
git branch -d release/v1.0.0
git push origin --delete release/v1.0.0
```

### Exemplo de Release Notes

```markdown
## v1.1.0 - Melhorias de UX

### Adicionado
- Cache de resultados
- Histórico de feedbacks
- Exportação em PDF
- Suporte a múltiplos idiomas

### Melhorado
- Performance de resposta (50% mais rápido com cache)
- Interface visual
- Tratamento de erros

### Corrigido
- Bug ao processar textos muito longos
- Erro de validação em edge cases

### Documentação
- Atualizado README com novas features
- Adicionado guia de uso da API
```

---

## 🐛 Issues e Pull Requests

### Templates de Issues

#### Bug Report

```markdown
**Descrição do Bug**
Descrição clara do problema

**Como Reproduzir**
1. Passo 1
2. Passo 2
3. Ver erro

**Comportamento Esperado**
O que deveria acontecer

**Screenshots**
Se aplicável

**Ambiente**
- OS: [ex: macOS 14.0]
- Python: [ex: 3.10]
- Versão: [ex: 1.0.0]
```

#### Feature Request

```markdown
**Funcionalidade Desejada**
Descrição da feature

**Problema que Resolve**
Qual problema isso resolve?

**Solução Proposta**
Como você imagina que funcionaria?

**Alternativas Consideradas**
Outras soluções que você pensou

**Contexto Adicional**
Qualquer informação adicional
```

### Pull Requests

#### Template de PR

```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Documentação

## Checklist
- [ ] Código segue padrões do projeto
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Sem warnings de linter
- [ ] Testes passando

## Screenshots (se aplicável)

## Issues Relacionadas
Closes #123
```

---

## ✅ Boas Práticas

### 1. Commits Frequentes

- Commite frequentemente (não acumule muitas mudanças)
- Commits pequenos e focados são melhores

### 2. Pull Requests

- Mantenha PRs pequenos e focados
- Um PR = uma feature/fix
- Descreva claramente o que foi feito

### 3. Code Review

- Revise código antes de mergear
- Seja construtivo em comentários
- Aprove PRs rapidamente se estiverem OK

### 4. Issues

- Use labels apropriadas
- Atribua issues quando possível
- Feche issues quando resolvidas

### 5. Documentação

- Atualize README quando necessário
- Documente mudanças significativas
- Mantenha CHANGELOG atualizado

### 6. Segurança

- Não commite secrets/API keys
- Use `.env` e `.gitignore`
- Revise dependências regularmente

---

## 🔧 Configurações Recomendadas

### Branch Protection Rules (main)

- ✅ Require pull request reviews
- ✅ Require status checks to pass
- ✅ Require branches to be up to date
- ✅ Include administrators

### GitHub Actions (Opcional)

Crie `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest --cov=core
```

---

## 📊 Métricas e Insights

### GitHub Insights Úteis

- **Pulse**: Visão geral de atividade
- **Contributors**: Quem contribuiu
- **Traffic**: Clones e visualizações
- **Community**: Saúde do projeto

---

## 🎯 Conclusão

Este guia fornece uma base sólida para gerenciar o repositório GitHub do FeedbackCraft AI. Adapte conforme necessário para seu workflow específico.

**Lembre-se**:
- Seja consistente com mensagens de commit
- Mantenha branches organizadas
- Documente releases adequadamente
- Use issues e PRs efetivamente

---

**Última Atualização**: 2024
**Versão do Guia**: 1.0
