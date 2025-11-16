"""
Formatters for output presentation
"""

from typing import Dict, Any, List, Optional


def format_fis(fato_impacto_sugestao: Optional[Dict[str, str]]) -> str:
    """
    Format Fato-Impacto-Sugestão structure.

    Args:
        fato_impacto_sugestao: Dictionary with 'fato', 'impacto', 'sugestao'

    Returns:
        Formatted string
    """
    if not fato_impacto_sugestao or not isinstance(fato_impacto_sugestao, dict):
        fato_impacto_sugestao = {}

    fato = fato_impacto_sugestao.get("fato", "Não especificado")
    impacto = fato_impacto_sugestao.get("impacto", "Não especificado")
    sugestao = fato_impacto_sugestao.get("sugestao", "Não especificado")

    return f"""**FATO:**
{fato}

**IMPACTO:**
{impacto}

**SUGESTÃO:**
{sugestao}"""


def format_suggestions(sugestoes: List[str]) -> str:
    """
    Format suggestions list.

    Args:
        sugestoes: List of suggestion strings

    Returns:
        Formatted string with bullet points
    """
    if not sugestoes:
        return "Nenhuma sugestão adicional."

    formatted = "**Sugestões Extras:**\n\n"
    for i, sugestao in enumerate(sugestoes, 1):
        formatted += f"{i}. {sugestao}\n"

    return formatted.strip()


def format_full_output(response_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Format complete output for display.

    Args:
        response_data: Parsed response from model

    Returns:
        Dictionary with formatted strings for each output section
    """
    feedback_aprimorado = response_data.get("feedback_aprimorado", "Não disponível")
    versao_curta = response_data.get("versao_curta", "Não disponível")
    fato_impacto_sugestao = response_data.get("fato_impacto_sugestao", {})
    sugestoes_extras = response_data.get("sugestoes_extras", [])
    observacoes = response_data.get("observacoes", "")

    return {
        "feedback_aprimorado": feedback_aprimorado,
        "versao_curta": versao_curta,
        "fato_impacto_sugestao": format_fis(fato_impacto_sugestao),
        "sugestoes_extras": format_suggestions(sugestoes_extras),
        "observacoes": observacoes
    }


def create_copy_text(response_data: Dict[str, Any]) -> str:
    """
    Create a single text block for easy copying.

    Args:
        response_data: Parsed response from model

    Returns:
        Single formatted text block
    """
    formatted = format_full_output(response_data)

    copy_text = f"""FEEDBACK APRIMORADO
{'=' * 50}
{formatted['feedback_aprimorado']}

VERSÃO CURTA
{'=' * 50}
{formatted['versao_curta']}

FATO-IMPACTO-SUGESTÃO
{'=' * 50}
{formatted['fato_impacto_sugestao']}

SUGESTÕES EXTRAS
{'=' * 50}
{formatted['sugestoes_extras']}
"""

    if formatted['observacoes']:
        copy_text += f"""
OBSERVAÇÕES
{'=' * 50}
{formatted['observacoes']}
"""

    return copy_text
