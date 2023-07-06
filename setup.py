import subprocess
import sys
import os


def create_and_activate_virtual_environment():
    subprocess.check_call([sys.executable, "-m", "venv", "env"])

    activate_file = (
        "env/bin/activate" if sys.platform != "win32" else "env\\Scripts\\activate.bat"
    )

    if not os.path.isfile(activate_file):
        raise FileNotFoundError(
            "Virtual environment activation script not found. "
            "Was the virtual environment created correctly?"
        )

    print(f"\n\nVirtual environment created. Activate it using: source {activate_file}")


def install_dependencies():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    )
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pre-commit"])
    subprocess.check_call([sys.executable, "-m", "pre_commit", "install"])


def main():
    create_and_activate_virtual_environment()
    install_dependencies()


if __name__ == "__main__":
    main()
