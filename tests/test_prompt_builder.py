"""
Tests for prompt builder module
"""

import pytest
from pathlib import Path
from core.prompt_builder import build_prompt, load_master_prompt


class TestLoadMasterPrompt:
    """Tests for loading master prompt."""

    def test_load_master_prompt_exists(self):
        """Test loading master prompt when file exists."""
        prompt = load_master_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_load_master_prompt_contains_keywords(self):
        """Test that master prompt contains expected keywords."""
        prompt = load_master_prompt()
        # Should contain some key concepts
        assert "feedback" in prompt.lower() or "comunicação" in prompt.lower()


class TestBuildPrompt:
    """Tests for prompt building."""

    def test_build_prompt_basic(self):
        """Test building a basic prompt."""
        feedback_text = "Você precisa melhorar sua comunicação."
        prompt = build_prompt(feedback_text)

        assert isinstance(prompt, str)
        assert feedback_text in prompt
        assert "TEXTO ORIGINAL" in prompt or "ORIGINAL" in prompt

    def test_build_prompt_with_type(self):
        """Test building prompt with feedback type."""
        feedback_text = "Test feedback"
        prompt = build_prompt(feedback_text, feedback_type="desempenho")

        assert "desempenho" in prompt.lower() or "performance" in prompt.lower()

    def test_build_prompt_with_tone(self):
        """Test building prompt with tone."""
        feedback_text = "Test feedback"
        prompt = build_prompt(feedback_text, tone="construtivo")

        assert "construtivo" in prompt.lower() or "constructive" in prompt.lower()

    def test_build_prompt_with_formality(self):
        """Test building prompt with formality level."""
        feedback_text = "Test feedback"
        prompt = build_prompt(feedback_text, formality="formal")

        assert "formal" in prompt.lower()

    def test_build_prompt_all_parameters(self):
        """Test building prompt with all parameters."""
        feedback_text = "Este é um feedback de teste."
        prompt = build_prompt(
            feedback_text,
            feedback_type="técnico",
            tone="direto",
            formality="formal"
        )

        assert feedback_text in prompt
        assert "técnico" in prompt.lower() or "technical" in prompt.lower()
        assert "direto" in prompt.lower() or "direct" in prompt.lower()
        assert "formal" in prompt.lower()

    def test_build_prompt_contains_instructions(self):
        """Test that prompt contains instructions."""
        feedback_text = "Test"
        prompt = build_prompt(feedback_text)

        assert "INSTRUÇÕES" in prompt or "instruções" in prompt.lower() or "instructions" in prompt.lower()

    def test_build_prompt_contains_json_format(self):
        """Test that prompt requests JSON format."""
        feedback_text = "Test"
        prompt = build_prompt(feedback_text)

        # Should mention JSON format
        assert "json" in prompt.lower() or "JSON" in prompt

    def test_build_prompt_different_types(self):
        """Test building prompts with different feedback types."""
        feedback_text = "Test"
        types = ["geral", "desempenho", "comportamento", "técnico", "liderança"]

        for feedback_type in types:
            prompt = build_prompt(feedback_text, feedback_type=feedback_type)
            assert feedback_text in prompt
            assert isinstance(prompt, str)
            assert len(prompt) > len(feedback_text)
