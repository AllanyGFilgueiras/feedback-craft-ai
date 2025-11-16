"""
Pytest configuration and fixtures
"""

import pytest
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def sample_feedback_text():
    """Sample feedback text for testing."""
    return "Você precisa melhorar sua comunicação com a equipe. Está difícil trabalhar assim."


@pytest.fixture
def sample_response_data():
    """Sample response data structure for testing."""
    return {
        "feedback_aprimorado": "Sua comunicação com a equipe pode ser aprimorada para facilitar a colaboração.",
        "versao_curta": "Melhorar comunicação com a equipe para facilitar colaboração.",
        "fato_impacto_sugestao": {
            "fato": "Comunicação com a equipe precisa de melhorias",
            "impacto": "Dificulta o trabalho em equipe e a colaboração",
            "sugestao": "Praticar comunicação clara e objetiva, buscando feedback regular"
        },
        "sugestoes_extras": [
            "Agendar reuniões regulares de alinhamento",
            "Usar ferramentas de comunicação de forma mais eficiente",
            "Solicitar feedback da equipe sobre sua comunicação"
        ],
        "observacoes": "Feedback original era direto mas poderia ser mais construtivo."
    }
