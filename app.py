"""
FeedbackCraft AI - Main Application
Professional feedback enhancement tool using AI
"""

import gradio as gr
from typing import Tuple, Optional
import os

from core.prompt_builder import build_prompt
from core.model_client import ModelClient
from core.validators import (
    validate_feedback_text,
    validate_feedback_type,
    validate_tone,
    validate_formality,
    sanitize_text
)
from core.formatters import format_full_output, create_copy_text


# Initialize model client
model_client = ModelClient(
    model_name=os.getenv("HF_MODEL_NAME", "meta-llama/Meta-Llama-3.1-8B-Instruct"),
    api_key=os.getenv("HF_API_KEY", ""),
    use_local=os.getenv("USE_LOCAL_MODEL", "false").lower() == "true"
)


def process_feedback(
    feedback_text: str,
    feedback_type: str,
    tone: str,
    formality: str
) -> Tuple[str, str, str, str, str]:
    """
    Process feedback and return enhanced versions.

    Args:
        feedback_text: Original feedback text
        feedback_type: Type of feedback
        tone: Desired tone
        formality: Formality level

    Returns:
        Tuple of (enhanced_feedback, short_version, fis_format, suggestions, copy_text)
    """
    # Validate inputs
    is_valid, error_msg = validate_feedback_text(feedback_text)
    if not is_valid:
        return error_msg, "", "", "", ""

    is_valid, error_msg = validate_feedback_type(feedback_type)
    if not is_valid:
        return error_msg, "", "", "", ""

    is_valid, error_msg = validate_tone(tone)
    if not is_valid:
        return error_msg, "", "", "", ""

    is_valid, error_msg = validate_formality(formality)
    if not is_valid:
        return error_msg, "", "", "", ""

    # Sanitize input
    feedback_text = sanitize_text(feedback_text)

    # Build prompt
    prompt = build_prompt(feedback_text, feedback_type, tone, formality)

    # Generate response
    try:
        response_text = model_client.generate(prompt)
        response_data = model_client.parse_response(response_text)

        # Format output
        formatted = format_full_output(response_data)
        copy_text = create_copy_text(response_data)

        return (
            formatted["feedback_aprimorado"],
            formatted["versao_curta"],
            formatted["fato_impacto_sugestao"],
            formatted["sugestoes_extras"],
            copy_text
        )
    except Exception as e:
        error_message = f"Erro ao processar feedback: {str(e)}"
        return error_message, "", "", "", ""


def create_interface():
    """Create and configure Gradio interface."""

    # Custom CSS for better styling
    custom_css = """
    .gradio-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .output-box {
        min-height: 150px;
    }
    """

    with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as app:
        # Header
        gr.Markdown(
            """
            # 🎯 FeedbackCraft AI
            ### Transforme feedbacks rascunhados em comunicações profissionais, claras e acionáveis
            """,
            elem_classes=["main-header"]
        )

        gr.Markdown(
            """
            **Como usar:** Cole ou digite seu feedback rascunhado abaixo, ajuste as opções conforme necessário,
            e receba uma versão aprimorada, profissional e acionável.
            """
        )

        with gr.Row():
            with gr.Column(scale=2):
                feedback_input = gr.Textbox(
                    label="📝 Seu Feedback (Rascunho)",
                    placeholder="Cole ou digite aqui o feedback que deseja melhorar...",
                    lines=8,
                    max_lines=15
                )

                with gr.Row():
                    feedback_type = gr.Dropdown(
                        choices=["geral", "desempenho", "comportamento", "técnico", "liderança"],
                        value="geral",
                        label="Tipo de Feedback",
                        info="Contexto do feedback"
                    )

                    tone = gr.Dropdown(
                        choices=["construtivo", "neutro", "encorajador", "direto"],
                        value="construtivo",
                        label="Tom",
                        info="Tom da comunicação"
                    )

                    formality = gr.Dropdown(
                        choices=["formal", "neutro", "casual"],
                        value="neutro",
                        label="Formalidade",
                        info="Nível de formalidade"
                    )

                process_btn = gr.Button(
                    "✨ Melhorar Feedback",
                    variant="primary",
                    size="lg"
                )

            with gr.Column(scale=3):
                enhanced_output = gr.Textbox(
                    label="✨ Feedback Aprimorado",
                    lines=8,
                    interactive=False,
                    elem_classes=["output-box"]
                )

                short_output = gr.Textbox(
                    label="📋 Versão Curta",
                    lines=3,
                    interactive=False
                )

                fis_output = gr.Markdown(
                    label="📊 Formato Fato-Impacto-Sugestão"
                )

                suggestions_output = gr.Markdown(
                    label="💡 Sugestões Extras"
                )

        with gr.Row():
            copy_text_output = gr.Textbox(
                label="📄 Texto Completo para Copiar",
                lines=10,
                interactive=True,
                visible=True
            )

        copy_btn = gr.Button(
            "📋 Copiar Tudo",
            variant="secondary"
        )

        # Examples
        gr.Markdown("### 💡 Exemplos")
        examples = gr.Examples(
            examples=[
                [
                    "você precisa melhorar sua comunicação com a equipe. está difícil trabalhar assim.",
                    "comportamento",
                    "construtivo",
                    "neutro"
                ],
                [
                    "o código que você entregou tinha muitos bugs. precisa ser mais cuidadoso.",
                    "técnico",
                    "direto",
                    "formal"
                ],
                [
                    "parabéns pelo projeto! mas acho que poderia ter sido entregue antes.",
                    "desempenho",
                    "encorajador",
                    "casual"
                ]
            ],
            inputs=[feedback_input, feedback_type, tone, formality],
            label="Clique em um exemplo para testar"
        )

        # Footer
        gr.Markdown(
            """
            ---
            **FeedbackCraft AI** - Desenvolvido com ❤️ para melhorar a comunicação profissional

            💡 **Dica:** Seja específico no seu feedback original para obter melhores resultados.
            """
        )

        # Event handlers
        process_btn.click(
            fn=process_feedback,
            inputs=[feedback_input, feedback_type, tone, formality],
            outputs=[enhanced_output, short_output, fis_output, suggestions_output, copy_text_output]
        )

        # Copy button functionality - simplified for Gradio 4.0.0
        # The text box is already interactive, so users can select and copy manually
        # For Gradio 4.0.0 compatibility, we'll just show a message
        def show_copy_message(text):
            """Show message that text is ready to copy."""
            return text
        
        copy_btn.click(
            fn=show_copy_message,
            inputs=[copy_text_output],
            outputs=[copy_text_output]
        )

    return app


if __name__ == "__main__":
    app = create_interface()
    app.launch(
        server_name="0.0.0.0" if os.getenv("SPACE_ID") else "127.0.0.1",
        server_port=int(os.getenv("PORT", 7860)),
        share=False
    )
