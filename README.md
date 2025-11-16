# 🎯 FeedbackCraft AI

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Gradio](https://img.shields.io/badge/gradio-4.0+-orange.svg)

**Transforme feedbacks rascunhados em comunicações profissionais, claras e acionáveis**

[🚀 Demo no Hugging Face](https://huggingface.co/spaces/seu-usuario/feedback-craft-ai) • [📖 Documentação](#documentação) • [🐛 Reportar Bug](https://github.com/seu-usuario/feedback-craft-ai/issues)

</div>

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Características](#características)
- [Demonstração](#demonstração)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Arquitetura](#arquitetura)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Deploy](#deploy)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [Licença](#licença)

---

## 🎯 Sobre o Projeto

**FeedbackCraft AI** é uma ferramenta inteligente que utiliza modelos de linguagem para transformar feedbacks rascunhados em comunicações profissionais, claras e acionáveis. O produto foi desenvolvido com foco em:

- **Profissionalismo**: Interface limpa e intuitiva
- **Qualidade**: Melhoria real na comunicação profissional
- **Praticidade**: Resultados imediatos e acionáveis
- **Arquitetura Limpa**: Código testável, escalável e manutenível

### Por que este produto demonstra maturidade profissional?

Este projeto demonstra:

✅ **Arquitetura Limpa**: Separação de responsabilidades, funções puras, testabilidade
✅ **Qualidade de Código**: Testes unitários abrangentes, validação robusta, tratamento de erros
✅ **UX Profissional**: Interface intuitiva, feedback visual, exemplos práticos
✅ **Documentação Completa**: README profissional, visão de produto, guias de deploy
✅ **Pronto para Produção**: Configuração de deploy, tratamento de edge cases, fallbacks
✅ **Boas Práticas**: Versionamento, estrutura escalável, código legível

---

## ✨ Características

- 🎨 **Interface Intuitiva**: Design limpo e profissional com Gradio
- 🤖 **IA Avançada**: Integração com modelos LLM (Llama 3.1, Gemma 2)
- 📊 **Múltiplos Formatos**: Feedback completo, versão curta, formato Fato-Impacto-Sugestão
- 🎛️ **Personalização**: Ajuste de tipo, tom e formalidade
- 📋 **Exportação Fácil**: Botão de copiar para uso imediato
- ✅ **Validação Robusta**: Validação de entrada e tratamento de erros
- 🧪 **Testado**: Cobertura de testes unitários abrangente

---

## 🖼️ Demonstração

### Interface Principal

```
┌─────────────────────────────────────────────────────────────┐
│              🎯 FeedbackCraft AI                            │
│  Transforme feedbacks rascunhados em comunicações          │
│              profissionais, claras e acionáveis             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────┐  ┌──────────────────────────────┐
│ 📝 Seu Feedback         │  │ ✨ Feedback Aprimorado        │
│                         │  │                               │
│ [Área de texto]         │  │ [Resultado melhorado]         │
│                         │  │                               │
│ Tipo: [geral ▼]         │  │ 📋 Versão Curta               │
│ Tom: [construtivo ▼]    │  │ [Resumo executivo]            │
│ Formalidade: [neutro ▼] │  │                               │
│                         │  │ 📊 Fato-Impacto-Sugestão      │
│ [✨ Melhorar Feedback]   │  │ [Estrutura FIS formatada]     │
└─────────────────────────┘  └──────────────────────────────┘
```

### Exemplo de Uso

**Input:**
```
você precisa melhorar sua comunicação com a equipe. está difícil trabalhar assim.
```

**Output:**
- **Feedback Aprimorado**: Versão completa e profissional
- **Versão Curta**: Resumo em 2-3 frases
- **Fato-Impacto-Sugestão**: Estrutura clara e acionável
- **Sugestões Extras**: Recomendações adicionais

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/feedback-craft-ai.git
   cd feedback-craft-ai
   ```

2. **Crie um ambiente virtual** (recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure variáveis de ambiente** (opcional)
   ```bash
   # Crie um arquivo .env
   echo "HF_API_KEY=sua_chave_aqui" >> .env
   echo "HF_MODEL_NAME=meta-llama/Meta-Llama-3.1-8B-Instruct" >> .env
   ```

---

## 💻 Uso

### Executar Localmente

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:7860`

### Uso Básico

1. **Cole ou digite** seu feedback rascunhado na área de texto
2. **Ajuste as opções** (tipo, tom, formalidade) conforme necessário
3. **Clique em "Melhorar Feedback"**
4. **Copie o resultado** usando o botão "Copiar Tudo"

### Opções Disponíveis

- **Tipo de Feedback**: geral, desempenho, comportamento, técnico, liderança
- **Tom**: construtivo, neutro, encorajador, direto
- **Formalidade**: formal, neutro, casual

---

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=core --cov=tests

# Testes específicos
pytest tests/test_validators.py
pytest tests/test_prompt_builder.py
```

### Estrutura de Testes

```
tests/
├── __init__.py
├── conftest.py              # Configuração e fixtures
├── test_validators.py       # Testes de validação
├── test_prompt_builder.py   # Testes de construção de prompts
├── test_formatters.py       # Testes de formatação
├── test_model_client.py     # Testes do cliente de modelo
└── test_edge_cases.py       # Testes de casos extremos
```

### Cobertura de Testes

- ✅ Validação de entrada
- ✅ Construção de prompts
- ✅ Formatação de saída
- ✅ Cliente de modelo (mockado)
- ✅ Casos extremos (texto vazio, muito longo, etc.)

---

## 🏗️ Arquitetura

### Princípios de Design

O projeto segue os princípios de **Clean Architecture Lite**:

1. **Separação de Responsabilidades**: Cada módulo tem uma responsabilidade única
2. **Funções Puras**: Funções testáveis sem efeitos colaterais
3. **Inversão de Dependências**: Abstrações para facilitar testes
4. **Testabilidade**: Código facilmente testável com mocks

### Fluxo de Dados

```
Input (Gradio)
    ↓
Validators (validação)
    ↓
Prompt Builder (construção do prompt)
    ↓
Model Client (chamada ao LLM)
    ↓
Formatters (formatação da saída)
    ↓
Output (Gradio)
```

### Camadas

- **Interface (app.py)**: Camada de apresentação com Gradio
- **Core**: Lógica de negócio pura
  - `validators.py`: Validação de entrada
  - `prompt_builder.py`: Construção de prompts
  - `model_client.py`: Integração com LLM
  - `formatters.py`: Formatação de saída
- **Prompts**: Templates de prompts
- **Tests**: Testes unitários

---

## 🛠️ Tecnologias

- **Python 3.10+**: Linguagem principal
- **Gradio 4.0+**: Interface web
- **pytest**: Framework de testes
- **requests**: Cliente HTTP para APIs
- **Hugging Face**: Modelos LLM e deploy

### Modelos Suportados

- Meta Llama 3.1 8B Instruct (recomendado)
- Google Gemma 2
- Qualquer modelo compatível com Hugging Face Inference API

---

## 📁 Estrutura do Projeto

```
feedback-craft-ai/
├── app.py                      # Aplicação principal (Gradio)
├── requirements.txt            # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
├── huggingface.yaml           # Configuração para HF Spaces
├── README.md                   # Este arquivo
├── PRODUCT_VISION.md          # Visão de produto
├── GITHUB_GUIDE.md            # Guia para GitHub
│
├── core/                       # Módulo core (lógica de negócio)
│   ├── __init__.py
│   ├── validators.py          # Validação de entrada
│   ├── prompt_builder.py      # Construção de prompts
│   ├── model_client.py        # Cliente de modelo LLM
│   └── formatters.py          # Formatação de saída
│
├── prompts/                    # Templates de prompts
│   └── master_prompt.txt      # Prompt mestre
│
└── tests/                      # Testes unitários
    ├── __init__.py
    ├── conftest.py            # Configuração pytest
    ├── test_validators.py
    ├── test_prompt_builder.py
    ├── test_formatters.py
    ├── test_model_client.py
    └── test_edge_cases.py
```

---

## 🚀 Deploy

### Hugging Face Spaces

1. **Crie uma conta** no [Hugging Face](https://huggingface.co)
2. **Crie um novo Space**:
   - SDK: Gradio
   - Hardware: CPU básico (ou GPU se necessário)
3. **Faça upload dos arquivos**:
   - `app.py`
   - `requirements.txt`
   - `huggingface.yaml`
   - Toda a pasta `core/`
   - Toda a pasta `prompts/`
4. **Configure variáveis de ambiente** (se necessário):
   - `HF_API_KEY`: Sua chave da API
   - `HF_MODEL_NAME`: Nome do modelo
5. **Aguarde o build** e acesse seu Space!

### Observações de Performance

- **Modelos Gratuitos**: Llama 3.1 e Gemma 2 têm limites de requisições
- **Timeout**: Configure timeout adequado (60s recomendado)
- **Fallback**: O sistema tem fallback para quando a API não está disponível
- **Cache**: Considere implementar cache para prompts similares (futuro)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📈 Roadmap

### Versão 1.1 (Próxima)
- [ ] Cache de resultados
- [ ] Histórico de feedbacks
- [ ] Exportação em PDF
- [ ] Suporte a múltiplos idiomas

### Versão 1.2
- [ ] API REST
- [ ] Integração com Slack/Teams
- [ ] Dashboard de analytics
- [ ] Templates personalizados

### Versão 2.0
- [ ] Plano Premium
- [ ] Modelos fine-tuned
- [ ] Integração com HRIS
- [ ] Aplicativo mobile

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**Seu Nome**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Perfil](https://linkedin.com/in/seu-perfil)
- Email: seu.email@exemplo.com

---

## 🙏 Agradecimentos

- [Hugging Face](https://huggingface.co) pela infraestrutura e modelos
- [Gradio](https://gradio.app) pela excelente biblioteca de UI
- Comunidade open source por inspiração e ferramentas

---

<div align="center">

**Feito com ❤️ para melhorar a comunicação profissional**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
