"""
Tests for formatters module
"""

import pytest
from core.formatters import (
    format_fis,
    format_suggestions,
    format_full_output,
    create_copy_text
)


class TestFormatFIS:
    """Tests for Fato-Impacto-Sugestão formatting."""

    def test_format_fis_complete(self):
        """Test formatting complete FIS structure."""
        fis_data = {
            "fato": "O projeto foi entregue com atraso",
            "impacto": "Isso afetou o cronograma da equipe",
            "sugestao": "Planejar melhor o tempo de desenvolvimento"
        }
        result = format_fis(fis_data)

        assert "FATO" in result
        assert "IMPACTO" in result
        assert "SUGESTÃO" in result
        assert fis_data["fato"] in result
        assert fis_data["impacto"] in result
        assert fis_data["sugestao"] in result

    def test_format_fis_missing_fields(self):
        """Test formatting FIS with missing fields."""
        fis_data = {
            "fato": "Teste"
        }
        result = format_fis(fis_data)

        assert "FATO" in result
        assert "Não especificado" in result or "IMPACTO" in result

    def test_format_fis_empty(self):
        """Test formatting empty FIS structure."""
        fis_data = {}
        result = format_fis(fis_data)

        assert "FATO" in result
        assert "IMPACTO" in result
        assert "SUGESTÃO" in result


class TestFormatSuggestions:
    """Tests for suggestions formatting."""

    def test_format_suggestions_normal(self):
        """Test formatting normal suggestions list."""
        suggestions = [
            "Sugestão 1",
            "Sugestão 2",
            "Sugestão 3"
        ]
        result = format_suggestions(suggestions)

        assert "Sugestões Extras" in result or "sugestões" in result.lower()
        assert "Sugestão 1" in result
        assert "Sugestão 2" in result
        assert "Sugestão 3" in result

    def test_format_suggestions_empty(self):
        """Test formatting empty suggestions list."""
        result = format_suggestions([])
        assert "Nenhuma" in result or "nenhuma" in result.lower()

    def test_format_suggestions_single(self):
        """Test formatting single suggestion."""
        suggestions = ["Uma única sugestão"]
        result = format_suggestions(suggestions)

        assert "Uma única sugestão" in result
        assert "1." in result or "1" in result


class TestFormatFullOutput:
    """Tests for full output formatting."""

    def test_format_full_output_complete(self):
        """Test formatting complete output."""
        response_data = {
            "feedback_aprimorado": "Feedback melhorado",
            "versao_curta": "Versão curta",
            "fato_impacto_sugestao": {
                "fato": "Fato",
                "impacto": "Impacto",
                "sugestao": "Sugestão"
            },
            "sugestoes_extras": ["Sugestão 1", "Sugestão 2"],
            "observacoes": "Observações"
        }
        result = format_full_output(response_data)

        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result
        assert "versao_curta" in result
        assert "fato_impacto_sugestao" in result
        assert "sugestoes_extras" in result
        assert result["feedback_aprimorado"] == "Feedback melhorado"

    def test_format_full_output_missing_fields(self):
        """Test formatting output with missing fields."""
        response_data = {
            "feedback_aprimorado": "Teste"
        }
        result = format_full_output(response_data)

        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result
        assert result["feedback_aprimorado"] == "Teste"

    def test_format_full_output_empty(self):
        """Test formatting empty output."""
        response_data = {}
        result = format_full_output(response_data)

        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result


class TestCreateCopyText:
    """Tests for copy text creation."""

    def test_create_copy_text_complete(self):
        """Test creating complete copy text."""
        response_data = {
            "feedback_aprimorado": "Feedback melhorado",
            "versao_curta": "Versão curta",
            "fato_impacto_sugestao": {
                "fato": "Fato",
                "impacto": "Impacto",
                "sugestao": "Sugestão"
            },
            "sugestoes_extras": ["Sugestão 1"],
            "observacoes": "Observações"
        }
        result = create_copy_text(response_data)

        assert isinstance(result, str)
        assert "FEEDBACK APRIMORADO" in result
        assert "VERSÃO CURTA" in result or "VERSAO CURTA" in result
        assert "Feedback melhorado" in result
        assert "Versão curta" in result

    def test_create_copy_text_no_observations(self):
        """Test creating copy text without observations."""
        response_data = {
            "feedback_aprimorado": "Feedback",
            "versao_curta": "Curto",
            "fato_impacto_sugestao": {
                "fato": "Fato",
                "impacto": "Impacto",
                "sugestao": "Sugestão"
            },
            "sugestoes_extras": []
        }
        result = create_copy_text(response_data)

        assert isinstance(result, str)
        assert "OBSERVAÇÕES" not in result or "observações" not in result.lower()
