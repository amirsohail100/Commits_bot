"""
Auto Commit Bot - Chunk 1/2
Helper modules, ANSI styling, Git interface, and File Handler.
"""

import os
import sys
import subprocess
from datetime import datetime

# ANSI Color Codes for Terminal UI
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    banner = f"""{Colors.OKCYAN}{Colors.BOLD}
    ==================================================
       🚀 AUTOMATED GIT CONTRIBUTION & COMMIT BOT 🚀
    ==================================================
    {Colors.ENDC}"""
    print(banner)

def ensure_file_exists(filename="daily_bot.txt"):
    """Ensures that the contribution tracking text file exists."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Daily Contribution Log\n")
        print(f"{Colors.OKGREEN}[+] Created tracking file: {filename}{Colors.ENDC}")
    else:
        print(f"{Colors.OKBLUE}[i] Found tracking file: {filename}{Colors.ENDC}")

def run_git_command(command):
    """Executes a git command and returns success status."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()