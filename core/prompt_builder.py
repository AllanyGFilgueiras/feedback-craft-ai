"""
Prompt builder for constructing LLM prompts
"""

from typing import Optional
from pathlib import Path


def load_master_prompt() -> str:
    """
    Load the master prompt template from file.

    Returns:
        Master prompt template as string
    """
    prompt_path = Path(__file__).parent.parent / "prompts" / "master_prompt.txt"

    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # Fallback prompt if file doesn't exist
        return """Você é um especialista em comunicação profissional e feedback construtivo.

Sua tarefa é melhorar textos de feedback, tornando-os:
- Claros e objetivos
- Respeitosos e profissionais
- Acionáveis (com sugestões concretas)
- Construtivos (focando em crescimento)

Siga o formato solicitado e adapte o tom e formalidade conforme as preferências."""


def build_prompt(
    feedback_text: str,
    feedback_type: str = "geral",
    tone: str = "construtivo",
    formality: str = "neutro"
) -> str:
    """
    Build a complete prompt for the LLM.

    Args:
        feedback_text: The original feedback text to improve
        feedback_type: Type of feedback (geral, desempenho, comportamento, técnico, liderança)
        tone: Desired tone (construtivo, neutro, encorajador, direto)
        formality: Formality level (formal, neutro, casual)

    Returns:
        Complete formatted prompt
    """
    master_prompt = load_master_prompt()

    # Map Portuguese labels to English for the model
    type_map = {
        "geral": "general",
        "desempenho": "performance",
        "comportamento": "behavioral",
        "técnico": "technical",
        "liderança": "leadership"
    }

    tone_map = {
        "construtivo": "constructive and supportive",
        "neutro": "neutral and balanced",
        "encorajador": "encouraging and positive",
        "direto": "direct and straightforward"
    }

    formality_map = {
        "formal": "formal and professional",
        "neutro": "neutral",
        "casual": "casual and friendly"
    }

    type_en = type_map.get(feedback_type, "general")
    tone_en = tone_map.get(tone, "constructive")
    formality_en = formality_map.get(formality, "neutral")

    prompt = f"""{master_prompt}

CONTEXTO:
- Tipo de feedback: {type_en}
- Tom desejado: {tone_en}
- Nível de formalidade: {formality_en}

TEXTO ORIGINAL PARA MELHORAR:
{feedback_text}

INSTRUÇÕES:
1. Analise o texto original
2. Identifique pontos que podem ser melhorados (clareza, respeito, objetividade)
3. Gere uma versão aprimorada do feedback
4. Crie uma versão curta (resumo executivo)
5. Formate no padrão Fato-Impacto-Sugestão
6. Forneça sugestões extras de melhoria

FORMATO DE RESPOSTA (JSON):
{{
    "feedback_aprimorado": "texto completo melhorado",
    "versao_curta": "resumo em 2-3 frases",
    "fato_impacto_sugestao": {{
        "fato": "o que aconteceu/foi observado",
        "impacto": "como isso afeta o trabalho/equipe",
        "sugestao": "ação recomendada"
    }},
    "sugestoes_extras": [
        "sugestão 1",
        "sugestão 2",
        "sugestão 3"
    ],
    "observacoes": "notas adicionais sobre o feedback original"
}}

Responda APENAS com o JSON válido, sem texto adicional antes ou depois."""

    return prompt
