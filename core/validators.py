"""
Validators for input validation and sanitization
"""

from typing import Optional, Tuple


def validate_feedback_text(text: str) -> Tuple[bool, Optional[str]]:
    """
    Validate feedback text input.

    Args:
        text: Input feedback text to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text:
        return False, "O texto de feedback não pode estar vazio."

    if not isinstance(text, str):
        return False, "O texto deve ser uma string."

    text_stripped = text.strip()

    if len(text_stripped) < 10:
        return False, "O texto deve ter pelo menos 10 caracteres."

    if len(text_stripped) > 5000:
        return False, "O texto não pode exceder 5000 caracteres."

    return True, None


def validate_feedback_type(feedback_type: str) -> Tuple[bool, Optional[str]]:
    """Validate feedback type selection."""
    valid_types = ["geral", "desempenho", "comportamento", "técnico", "liderança"]
    if feedback_type not in valid_types:
        return False, f"Tipo de feedback inválido. Use: {', '.join(valid_types)}"
    return True, None


def validate_tone(tone: str) -> Tuple[bool, Optional[str]]:
    """Validate tone selection."""
    valid_tones = ["construtivo", "neutro", "encorajador", "direto"]
    if tone not in valid_tones:
        return False, f"Tom inválido. Use: {', '.join(valid_tones)}"
    return True, None


def validate_formality(formality: str) -> Tuple[bool, Optional[str]]:
    """Validate formality level selection."""
    valid_levels = ["formal", "neutro", "casual"]
    if formality not in valid_levels:
        return False, f"Nível de formalidade inválido. Use: {', '.join(valid_levels)}"
    return True, None


def sanitize_text(text: str) -> str:
    """
    Sanitize input text by removing excessive whitespace.

    Args:
        text: Input text to sanitize

    Returns:
        Sanitized text
    """
    if not text:
        return ""

    # Remove excessive whitespace but preserve single spaces
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.strip():
            # Remove multiple spaces within the line
            cleaned_line = ' '.join(line.split())
            cleaned_lines.append(cleaned_line)
    return '\n'.join(cleaned_lines)
