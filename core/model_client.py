"""
Model client for interacting with LLM APIs
"""

import json
import os
from typing import Dict, Optional, Any
import requests


class ModelClient:
    """Client for interacting with LLM models via Hugging Face Inference API."""

    def __init__(
        self,
        model_name: Optional[str] = None,
        api_key: Optional[str] = None,
        use_local: bool = False
    ):
        """
        Initialize the model client.

        Args:
            model_name: Hugging Face model name (default: meta-llama/Meta-Llama-3.1-8B-Instruct)
            api_key: Hugging Face API key (optional, can use env var HF_API_KEY)
            use_local: Whether to use local model (for future implementation)
        """
        self.model_name = model_name or os.getenv(
            "HF_MODEL_NAME",
            "meta-llama/Meta-Llama-3.1-8B-Instruct"
        )
        self.api_key = api_key or os.getenv("HF_API_KEY", "")
        self.use_local = use_local
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"

    def generate(
        self,
        prompt: str,
        max_length: int = 1500,
        temperature: float = 0.7,
        top_p: float = 0.9
    ) -> str:
        """
        Generate text using the LLM.

        Args:
            prompt: Input prompt
            max_length: Maximum response length
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter

        Returns:
            Generated text response
        """
        if self.use_local:
            return self._generate_local(prompt, max_length, temperature, top_p)
        else:
            return self._generate_api(prompt, max_length, temperature, top_p)

    def _generate_api(
        self,
        prompt: str,
        max_length: int,
        temperature: float,
        top_p: float
    ) -> str:
        """Generate using Hugging Face Inference API."""
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_length,
                "temperature": temperature,
                "top_p": top_p,
                "return_full_text": False
            },
            "options": {
                "wait_for_model": True
            }
        }

        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            
            # Check if model is loading (503 status)
            if response.status_code == 503:
                # Model is loading, use fallback with message
                fallback_response = self._generate_fallback(prompt)
                # Add note about model loading
                data = json.loads(fallback_response)
                data["observacoes"] = "⚠️ Modelo está carregando. Aguarde alguns segundos e tente novamente. Usando melhoria básica enquanto isso."
                return json.dumps(data, ensure_ascii=False, indent=2)
            
            response.raise_for_status()
            
            result = response.json()
            
            # Handle different response formats
            if isinstance(result, list) and len(result) > 0:
                if "generated_text" in result[0]:
                    return result[0]["generated_text"]
                elif "text" in result[0]:
                    return result[0]["text"]
            
            if isinstance(result, dict):
                if "generated_text" in result:
                    return result["generated_text"]
                elif "text" in result:
                    return result["text"]
            
            # Fallback: return as string
            return str(result)
            
        except requests.exceptions.HTTPError as e:
            # HTTP error (401, 403, etc.) - likely API key issue
            fallback_response = self._generate_fallback(prompt)
            data = json.loads(fallback_response)
            data["observacoes"] = f"⚠️ Erro na API ({e.response.status_code}). Usando melhoria básica. Configure HF_API_KEY para usar modelo completo."
            return json.dumps(data, ensure_ascii=False, indent=2)
        except (requests.exceptions.RequestException, Exception) as e:
            # Fallback response for demo purposes (catch all exceptions)
            fallback_response = self._generate_fallback(prompt)
            data = json.loads(fallback_response)
            data["observacoes"] = f"⚠️ Erro de conexão. Usando melhoria básica. Erro: {str(e)[:100]}"
            return json.dumps(data, ensure_ascii=False, indent=2)

    def _generate_local(
        self,
        prompt: str,
        max_length: int,
        temperature: float,
        top_p: float
    ) -> str:
        """Generate using local model (placeholder for future implementation)."""
        # This would use transformers library for local inference
        # For now, return fallback
        return self._generate_fallback(prompt)

    def _generate_fallback(self, prompt: str) -> str:
        """
        Fallback response when API is unavailable.
        This provides a basic structure for demonstration with improved text processing.
        """
        # Extract feedback text from prompt (simple extraction)
        if "TEXTO ORIGINAL PARA MELHORAR:" in prompt:
            parts = prompt.split("TEXTO ORIGINAL PARA MELHORAR:")
            if len(parts) > 1:
                original_text = parts[1].split("INSTRUÇÕES:")[0].strip()
                
                # Improved text processing (better than just capitalize)
                improved = self._improve_text_basic(original_text)
                
                # Create short version
                words = improved.split()
                short_version = " ".join(words[:15]) + ("..." if len(words) > 15 else "")

                return json.dumps({
                    "feedback_aprimorado": improved,
                    "versao_curta": short_version,
                    "fato_impacto_sugestao": {
                        "fato": "Feedback recebido para análise e melhoria",
                        "impacto": "Oportunidade de aprimorar a comunicação profissional",
                        "sugestao": "Revisar o feedback aprimorado e aplicar as sugestões fornecidas"
                    },
                    "sugestoes_extras": [
                        "Seja específico sobre comportamentos observados",
                        "Foque em ações, não em características pessoais",
                        "Ofereça exemplos concretos quando possível",
                        "Use linguagem respeitosa e construtiva"
                    ],
                    "observacoes": "⚠️ Modo fallback ativo. Para melhorias mais sofisticadas, configure uma chave de API do Hugging Face ou use um modelo local."
                }, ensure_ascii=False, indent=2)

        return json.dumps({
            "feedback_aprimorado": "Erro ao processar feedback.",
            "versao_curta": "Erro no processamento",
            "fato_impacto_sugestao": {
                "fato": "Erro no processamento",
                "impacto": "Não foi possível melhorar o feedback",
                "sugestao": "Tente novamente ou verifique a conexão"
            },
            "sugestoes_extras": [],
            "observacoes": "Erro no processamento do feedback."
        }, ensure_ascii=False, indent=2)
    
    def _improve_text_basic(self, text: str) -> str:
        """
        Basic text improvement when LLM is not available.
        This is a simple rule-based improvement.
        """
        if not text:
            return text
        
        # Capitalize first letter
        improved = text.strip().capitalize()
        
        # Ensure it ends with punctuation
        if improved and improved[-1] not in '.!?':
            improved += '.'
        
        # Replace common informal patterns
        replacements = {
            'vc': 'você',
            'pq': 'porque',
            'tb': 'também',
            'tbm': 'também',
            'nao': 'não',
            'eh': 'é',
            'ta': 'está',
            'to': 'estou',
        }
        
        words = improved.split()
        improved_words = []
        for word in words:
            word_lower = word.lower().rstrip('.,!?;:')
            if word_lower in replacements:
                # Preserve capitalization and punctuation
                punct = word[len(word_lower):]
                improved_words.append(replacements[word_lower].capitalize() + punct)
            else:
                improved_words.append(word)
        
        improved = ' '.join(improved_words)
        
        # Add professional touch
        if not any(improved.startswith(prefix) for prefix in ['Sua', 'Você', 'O', 'A', 'Os', 'As']):
            # Try to make it more professional
            if improved.lower().startswith('você'):
                improved = improved[0].upper() + improved[1:]
        
        return improved

    def parse_response(self, response_text: str) -> Dict[str, Any]:
        """
        Parse LLM response into structured format.

        Args:
            response_text: Raw response from LLM

        Returns:
            Parsed response dictionary
        """
        # Try to extract JSON from response
        response_text = response_text.strip()

        # Remove markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        response_text = response_text.strip()

        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            # If JSON parsing fails, return a structured error response
            return {
                "feedback_aprimorado": response_text[:500] if response_text else "Erro ao processar resposta.",
                "versao_curta": "Resposta não formatada corretamente",
                "fato_impacto_sugestao": {
                    "fato": "Resposta do modelo não está no formato esperado",
                    "impacto": "Dados podem estar incompletos",
                    "sugestao": "Tente novamente ou verifique a configuração do modelo"
                },
                "sugestoes_extras": [],
                "observacoes": f"Resposta original: {response_text[:200]}"
            }
