"""
Example: Run MFO using the CLI programmatically
================================================
"""

import subprocess
from pathlib import Path

def main():
    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    # اجرای CLI
    command = [
        "poetry", "run", "mfo",
        "--fitness", "sphere",
        "--iterations", "50",
        "--moths", "30",
        "--output", str(output_dir)
    ]

    subprocess.run(command)

if __name__ == "__main__":
    main()
