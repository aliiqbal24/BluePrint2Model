"""
setup_env.py
-------------
Bootstraps the environment for BluePrint2Model:
- Creates virtual environment
- Installs requirements
- Prompts for API keys
- Writes .env file
"""

import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VENV_DIR = PROJECT_ROOT / "venv"
ENV_FILE = PROJECT_ROOT / ".env"
REQ_FILE = PROJECT_ROOT / "requirements.txt"

def run(cmd):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def create_virtualenv():
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        run(f"python -m venv \"{VENV_DIR}\"")
    else:
        print("Virtual environment already exists.")

def install_requirements():
    print("Installing dependencies...")
    pip_path = VENV_DIR / "Scripts" / "pip.exe" if os.name == "nt" else VENV_DIR / "bin" / "pip"
    run(f"\"{pip_path}\" install -r \"{REQ_FILE}\"")

def setup_env_file():
    if ENV_FILE.exists():
        print(".env file already exists.")
        return

    print("Creating .env file automatically...")

    # Option 1: hardcode placeholders (safe default)
    openai_key = os.getenv("OPENAI_API_KEY", "")
    anthropic_key = ""
    google_key = ""

    # Option 2 (optional): read from system environment if already exported
    openai_key = os.getenv("OPENAI_API_KEY", openai_key)
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", anthropic_key)
    google_key = os.getenv("GOOGLE_API_KEY", google_key)

    ENV_FILE.write_text(
        f"OPENAI_API_KEY={openai_key}\n"
        f"ANTHROPIC_API_KEY={anthropic_key}\n"
        f"GOOGLE_API_KEY={google_key}\n"
    )
    print("✅ .env file created.")

def main():
    print("=== BluePrint2Model Environment Setup ===")
    create_virtualenv()
    install_requirements()
    setup_env_file()
    print("✅ Setup complete. Activate with:")
    print(f"    {VENV_DIR}\\Scripts\\activate" if os.name == "nt" else f"source {VENV_DIR}/bin/activate")

if __name__ == "__main__":
    main()
