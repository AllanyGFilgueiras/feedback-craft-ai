"""
Tests for model client module
"""

import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from core.model_client import ModelClient


class TestModelClient:
    """Tests for ModelClient class."""

    def test_init_default(self):
        """Test ModelClient initialization with defaults."""
        client = ModelClient()
        assert client.model_name is not None
        assert isinstance(client.model_name, str)

    def test_init_custom_model(self):
        """Test ModelClient initialization with custom model."""
        client = ModelClient(model_name="test-model")
        assert client.model_name == "test-model"

    def test_init_with_api_key(self):
        """Test ModelClient initialization with API key."""
        client = ModelClient(api_key="test-key")
        assert client.api_key == "test-key"

    def test_parse_response_valid_json(self):
        """Test parsing valid JSON response."""
        client = ModelClient()
        json_response = json.dumps({
            "feedback_aprimorado": "Test",
            "versao_curta": "Short",
            "fato_impacto_sugestao": {"fato": "F", "impacto": "I", "sugestao": "S"},
            "sugestoes_extras": [],
            "observacoes": ""
        })

        result = client.parse_response(json_response)
        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result
        assert result["feedback_aprimorado"] == "Test"

    def test_parse_response_with_markdown(self):
        """Test parsing JSON response wrapped in markdown code blocks."""
        client = ModelClient()
        json_response = "```json\n" + json.dumps({"feedback_aprimorado": "Test"}) + "\n```"

        result = client.parse_response(json_response)
        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result

    def test_parse_response_invalid_json(self):
        """Test parsing invalid JSON response."""
        client = ModelClient()
        invalid_response = "This is not JSON"

        result = client.parse_response(invalid_response)
        assert isinstance(result, dict)
        # Should return a structured error response
        assert "feedback_aprimorado" in result

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        client = ModelClient()
        result = client.parse_response("")

        assert isinstance(result, dict)
        assert "feedback_aprimorado" in result

    @patch('core.model_client.requests.post')
    def test_generate_api_success(self, mock_post):
        """Test successful API generation."""
        # Mock successful API response
        mock_response = Mock()
        mock_response.json.return_value = [{"generated_text": json.dumps({"feedback_aprimorado": "Test"})}]
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = ModelClient(api_key="test-key")
        result = client.generate("Test prompt")

        assert isinstance(result, str)
        assert len(result) > 0
        mock_post.assert_called_once()

    @patch('core.model_client.requests.post')
    def test_generate_api_error(self, mock_post):
        """Test API generation with error (should use fallback)."""
        # Mock API error
        mock_post.side_effect = Exception("API Error")

        client = ModelClient(api_key="test-key")
        result = client.generate("Test prompt")

        # Should return fallback response
        assert isinstance(result, str)
        assert len(result) > 0

    def test_generate_fallback(self):
        """Test fallback generation."""
        client = ModelClient()
        prompt = "TEXTO ORIGINAL PARA MELHORAR:\nTest feedback\nINSTRUÇÕES:"

        result = client._generate_fallback(prompt)

        assert isinstance(result, str)
        # Should be valid JSON
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert "feedback_aprimorado" in parsed

    def test_generate_fallback_no_original_text(self):
        """Test fallback generation without original text in prompt."""
        client = ModelClient()
        prompt = "Just a regular prompt"

        result = client._generate_fallback(prompt)

        assert isinstance(result, str)
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert "feedback_aprimorado" in parsed
