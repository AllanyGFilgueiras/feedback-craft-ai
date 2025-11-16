"""
Tests for validators module
"""

import pytest
from core.validators import (
    validate_feedback_text,
    validate_feedback_type,
    validate_tone,
    validate_formality,
    sanitize_text
)


class TestValidateFeedbackText:
    """Tests for feedback text validation."""

    def test_valid_text(self):
        """Test validation of valid feedback text."""
        text = "Este é um feedback válido com mais de 10 caracteres."
        is_valid, error = validate_feedback_text(text)
        assert is_valid is True
        assert error is None

    def test_empty_text(self):
        """Test validation of empty text."""
        is_valid, error = validate_feedback_text("")
        assert is_valid is False
        assert error is not None
        assert "vazio" in error.lower()

    def test_whitespace_only(self):
        """Test validation of whitespace-only text."""
        is_valid, error = validate_feedback_text("   \n\t  ")
        assert is_valid is False

    def test_too_short(self):
        """Test validation of text that's too short."""
        is_valid, error = validate_feedback_text("curto")
        assert is_valid is False
        assert "10" in error or "caracteres" in error.lower()

    def test_too_long(self):
        """Test validation of text that's too long."""
        long_text = "a" * 5001
        is_valid, error = validate_feedback_text(long_text)
        assert is_valid is False
        assert "5000" in error or "exceder" in error.lower()

    def test_non_string_input(self):
        """Test validation of non-string input."""
        is_valid, error = validate_feedback_text(123)
        assert is_valid is False
        assert "string" in error.lower()

    def test_valid_length_boundary(self):
        """Test validation at boundary conditions."""
        # Exactly 10 characters
        text = "a" * 10
        is_valid, error = validate_feedback_text(text)
        assert is_valid is True

        # Exactly 5000 characters
        text = "a" * 5000
        is_valid, error = validate_feedback_text(text)
        assert is_valid is True


class TestValidateFeedbackType:
    """Tests for feedback type validation."""

    def test_valid_types(self):
        """Test validation of valid feedback types."""
        valid_types = ["geral", "desempenho", "comportamento", "técnico", "liderança"]
        for feedback_type in valid_types:
            is_valid, error = validate_feedback_type(feedback_type)
            assert is_valid is True, f"Type {feedback_type} should be valid"
            assert error is None

    def test_invalid_type(self):
        """Test validation of invalid feedback type."""
        is_valid, error = validate_feedback_type("invalid")
        assert is_valid is False
        assert error is not None
        assert "inválido" in error.lower() or "invalid" in error.lower()


class TestValidateTone:
    """Tests for tone validation."""

    def test_valid_tones(self):
        """Test validation of valid tones."""
        valid_tones = ["construtivo", "neutro", "encorajador", "direto"]
        for tone in valid_tones:
            is_valid, error = validate_tone(tone)
            assert is_valid is True, f"Tone {tone} should be valid"
            assert error is None

    def test_invalid_tone(self):
        """Test validation of invalid tone."""
        is_valid, error = validate_tone("invalid")
        assert is_valid is False
        assert error is not None


class TestValidateFormality:
    """Tests for formality validation."""

    def test_valid_formality_levels(self):
        """Test validation of valid formality levels."""
        valid_levels = ["formal", "neutro", "casual"]
        for formality in valid_levels:
            is_valid, error = validate_formality(formality)
            assert is_valid is True, f"Formality {formality} should be valid"
            assert error is None

    def test_invalid_formality(self):
        """Test validation of invalid formality level."""
        is_valid, error = validate_formality("invalid")
        assert is_valid is False
        assert error is not None


class TestSanitizeText:
    """Tests for text sanitization."""

    def test_sanitize_normal_text(self):
        """Test sanitization of normal text."""
        text = "Este é um texto normal."
        result = sanitize_text(text)
        assert result == text

    def test_sanitize_whitespace(self):
        """Test sanitization of text with excessive whitespace."""
        text = "  Este   é   um   texto   com   espaços   extras.  "
        result = sanitize_text(text)
        assert "  " not in result  # No double spaces
        assert result.strip() == result  # No leading/trailing spaces

    def test_sanitize_multiline(self):
        """Test sanitization of multiline text."""
        text = "Linha 1\n\n\nLinha 2\n  \n  Linha 3  "
        result = sanitize_text(text)
        assert "\n\n\n" not in result
        assert len(result.split("\n")) <= 3

    def test_sanitize_empty(self):
        """Test sanitization of empty text."""
        result = sanitize_text("")
        assert result == ""

    def test_sanitize_only_whitespace(self):
        """Test sanitization of whitespace-only text."""
        result = sanitize_text("   \n\t  ")
        assert result == ""
