"""
Tests for edge cases and special scenarios
"""

import pytest
from core.validators import validate_feedback_text, sanitize_text
from core.prompt_builder import build_prompt
from core.formatters import format_full_output, create_copy_text
from core.model_client import ModelClient


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_empty_string(self):
        """Test handling of empty string."""
        is_valid, error = validate_feedback_text("")
        assert is_valid is False
        assert error is not None

    def test_very_short_text(self):
        """Test handling of very short text."""
        is_valid, error = validate_feedback_text("abc")
        assert is_valid is False

    def test_aggressive_language(self):
        """Test handling of potentially aggressive language."""
        # Validator should accept it (it's not the validator's job to judge content)
        aggressive_text = "você está fazendo tudo errado e precisa mudar imediatamente"
        is_valid, error = validate_feedback_text(aggressive_text)
        assert is_valid is True  # Validator only checks length/format

    def test_confusing_text(self):
        """Test handling of confusing/unclear text."""
        confusing_text = "talvez você poderia pensar em considerar a possibilidade de talvez melhorar"
        is_valid, error = validate_feedback_text(confusing_text)
        assert is_valid is True

    def test_informal_text(self):
        """Test handling of very informal text."""
        informal_text = "cara, tipo, assim, você sabe, tipo, melhorar, tipo, sabe?"
        is_valid, error = validate_feedback_text(informal_text)
        assert is_valid is True

    def test_multiline_text(self):
        """Test handling of multiline text."""
        multiline = "Linha 1\nLinha 2\nLinha 3\n" * 10
        is_valid, error = validate_feedback_text(multiline)
        assert is_valid is True

    def test_special_characters(self):
        """Test handling of special characters."""
        special = "Feedback com caracteres especiais: @#$%^&*()[]{}|\\/<>?~`"
        is_valid, error = validate_feedback_text(special)
        assert is_valid is True

    def test_unicode_text(self):
        """Test handling of unicode characters."""
        unicode_text = "Feedback com emojis: 🎯✨🚀 e acentos: áéíóú ção"
        is_valid, error = validate_feedback_text(unicode_text)
        assert is_valid is True

    def test_very_long_single_word(self):
        """Test handling of very long single word."""
        long_word = "a" * 100
        is_valid, error = validate_feedback_text(long_word)
        assert is_valid is True

    def test_only_numbers(self):
        """Test handling of text with only numbers."""
        numbers = "1234567890" * 2  # 20 characters
        is_valid, error = validate_feedback_text(numbers)
        assert is_valid is True

    def test_prompt_with_edge_cases(self):
        """Test prompt building with edge case inputs."""
        edge_cases = [
            "a" * 50,  # Repetitive
            "test\n\n\n\n\n",  # Many newlines
            "  spaced  out  text  ",  # Excessive spaces
        ]

        for text in edge_cases:
            prompt = build_prompt(text)
            assert isinstance(prompt, str)
            assert len(prompt) > 0

    def test_formatter_with_missing_data(self):
        """Test formatters with missing or incomplete data."""
        incomplete_data = {
            "feedback_aprimorado": "Test"
            # Missing other fields
        }

        result = format_full_output(incomplete_data)
        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result

    def test_formatter_with_none_values(self):
        """Test formatters with None values."""
        data_with_none = {
            "feedback_aprimorado": None,
            "versao_curta": None,
            "fato_impacto_sugestao": None,
            "sugestoes_extras": None
        }

        result = format_full_output(data_with_none)
        assert isinstance(result, dict)

    def test_model_client_empty_prompt(self):
        """Test model client with empty prompt."""
        client = ModelClient()
        result = client._generate_fallback("")

        assert isinstance(result, str)
        # Should handle gracefully
        parsed = client.parse_response(result)
        assert isinstance(parsed, dict)

    def test_sanitize_edge_cases(self):
        """Test sanitization of edge case texts."""
        edge_cases = [
            "   ",
            "\n\n\n",
            "\t\t\t",
            "  a  b  c  ",
            "\n\na\n\nb\n\n",
        ]

        for text in edge_cases:
            result = sanitize_text(text)
            assert isinstance(result, str)

    def test_boundary_lengths(self):
        """Test validation at exact boundary lengths."""
        # Exactly 10 characters (minimum)
        min_text = "a" * 10
        is_valid, _ = validate_feedback_text(min_text)
        assert is_valid is True

        # Exactly 5000 characters (maximum)
        max_text = "a" * 5000
        is_valid, _ = validate_feedback_text(max_text)
        assert is_valid is True

        # 9 characters (below minimum)
        too_short = "a" * 9
        is_valid, _ = validate_feedback_text(too_short)
        assert is_valid is False

        # 5001 characters (above maximum)
        too_long = "a" * 5001
        is_valid, _ = validate_feedback_text(too_long)
        assert is_valid is False
