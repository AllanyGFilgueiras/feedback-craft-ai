#!/usr/bin/env python3
"""
Script para fazer deploy do FeedbackCraft AI no Hugging Face Spaces
Uso: python3 deploy_hf.py SEU-USUARIO-HF
"""

import sys
import os
from pathlib import Path

try:
    from huggingface_hub import HfApi, create_repo, login
    from huggingface_hub.utils import HfHubHTTPError
except ImportError:
    print("❌ Erro: huggingface_hub não está instalado")
    print("   Execute: pip3 install huggingface_hub")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("❌ Erro: Forneça seu username do Hugging Face")
        print("Uso: python3 deploy_hf.py SEU-USUARIO-HF")
        sys.exit(1)

    username = sys.argv[1]
    space_name = "feedback-craft-ai"
    repo_id = f"{username}/{space_name}"

    print("🤗 Preparando deploy para Hugging Face Spaces...")
    print()

    # Verificar login
    api = HfApi()
    try:
        user_info = api.whoami()
        print(f"✅ Autenticado como: {user_info.get('name', 'Usuário')}")
    except Exception:
        print("⚠️  Você precisa fazer login no Hugging Face")
        print("   Execute: huggingface-cli login")
        print("   Ou acesse: https://huggingface.co/settings/tokens")
        print()
        token = input("Cole seu token (ou pressione Enter para fazer login interativo): ").strip()
        if token:
            login(token=token)
        else:
            login()
        api = HfApi()
        user_info = api.whoami()
        print(f"✅ Autenticado como: {user_info.get('name', 'Usuário')}")

    print()

    # Verificar se Space existe
    try:
        api.repo_info(repo_id, repo_type="space")
        print(f"✅ Space já existe: https://huggingface.co/spaces/{repo_id}")
        response = input("Deseja atualizar o Space existente? (s/n): ").strip().lower()
        if response != 's':
            print("❌ Operação cancelada")
            sys.exit(0)
    except HfHubHTTPError as e:
        if e.status_code == 404:
            print(f"📦 Criando novo Space: {repo_id}")
            try:
                create_repo(
                    repo_id=repo_id,
                    repo_type="space",
                    space_sdk="gradio",
                    space_hardware="cpu-basic",
                )
                print(f"✅ Space criado: https://huggingface.co/spaces/{repo_id}")
            except Exception as e:
                print(f"❌ Erro ao criar Space: {e}")
                sys.exit(1)
        else:
            print(f"❌ Erro: {e}")
            sys.exit(1)

    # Verificar arquivos necessários
    print()
    print("📋 Verificando arquivos necessários...")

    required_files = [
        "app.py",
        "requirements.txt",
        "huggingface.yaml",
    ]

    required_dirs = [
        "core",
        "prompts",
    ]

    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)

    for dir_name in required_dirs:
        if not Path(dir_name).is_dir():
            missing.append(f"{dir_name}/")

    if missing:
        print(f"❌ Arquivos/pastas faltando: {', '.join(missing)}")
        sys.exit(1)

    print("✅ Todos os arquivos necessários estão presentes")

    # Instruções para Git push
    print()
    print("📡 Para fazer upload dos arquivos, você tem duas opções:")
    print()
    print("OPÇÃO 1: Via Git (Recomendado)")
    print("-" * 50)
    print("1. Instale Git LFS: brew install git-lfs")
    print("2. Execute:")
    print(f"   git lfs install")
    print(f"   git remote add huggingface https://huggingface.co/spaces/{repo_id}")
    print(f"   git push huggingface main")
    print()
    print("OPÇÃO 2: Via Interface Web (Mais Simples)")
    print("-" * 50)
    print(f"1. Acesse: https://huggingface.co/spaces/{repo_id}")
    print("2. Vá em 'Files and versions' → 'Add file' → 'Upload files'")
    print("3. Faça upload de:")
    print("   - app.py")
    print("   - requirements.txt")
    print("   - huggingface.yaml")
    print("   - Pasta core/ completa")
    print("   - Pasta prompts/ completa")
    print()
    print(f"🌐 Seu Space: https://huggingface.co/spaces/{repo_id}")
    print()


if __name__ == "__main__":
    main()
