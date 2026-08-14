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


"""
Auto Commit Bot - Chunk 2/2
Core commit execution loop, push workflow, and CLI entry point.
"""

def perform_commits(count, filename="daily_bot.txt", branch="main"):
    """Executes the automated commit loop."""
    print(f"\n{Colors.WARNING}[*] Starting batch commit process ({count} commits)...{Colors.ENDC}\n")
    
    successful_commits = 0
    for i in range(1, count + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Daily update {i} - {timestamp}\n"
        
        # Append update to tracking file
        with open(filename, "a", encoding="utf-8") as f:
            f.write(log_entry)
            
        # Git Add
        add_success, add_err = run_git_command(f"git add {filename}")
        if not add_success:
            print(f"{Colors.FAIL}[!] Error adding file on commit {i}: {add_err}{Colors.ENDC}")
            break
            
        # Git Commit
        commit_msg = f"chore: update daily contribution log {i}"
        commit_success, commit_out = run_git_command(f'git commit -m "{commit_msg}"')
        
        if commit_success:
            successful_commits += 1
            print(f"{Colors.OKGREEN}[✓] Commit {i}/{count} complete: '{commit_msg}'{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[!] Commit {i} failed: {commit_out}{Colors.ENDC}")
            break

    print(f"\n{Colors.OKCYAN}=================================================={Colors.ENDC}")
    print(f"{Colors.BOLD}Completed {successful_commits}/{count} commits successfully.{Colors.ENDC}")
    
    if successful_commits > 0:
        push_choice = input(f"\n{Colors.BOLD}Do you want to push commits to origin {branch}? (Y/n): {Colors.ENDC}").strip().lower()
        if push_choice in ['', 'y', 'yes']:
            print(f"{Colors.WARNING}[*] Pushing to origin {branch}...{Colors.ENDC}")
            push_success, push_msg = run_git_command(f"git push origin {branch}")
            if push_success:
                print(f"{Colors.OKGREEN}[🚀] Successfully pushed all commits to GitHub!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}[!] Failed to push: {push_msg}{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}[i] Skipped pushing to remote repository.{Colors.ENDC}")

def main():
    print_banner()
    ensure_file_exists("daily_bot.txt")
    
    # User Input for Commit Count
    try:
        user_input = input(f"\nEnter required number of commits (Default [10]): ").strip()
        count = int(user_input) if user_input else 10
    except ValueError:
        print(f"{Colors.FAIL}Invalid input! Using default value: 10{Colors.ENDC}")
        count = 10

    # User Input for Branch Name
    branch_input = input(f"Enter target git branch (Default [main]): ").strip()
    branch = branch_input if branch_input else "main"

    perform_commits(count=count, filename="daily_bot.txt", branch=branch)

if __name__ == "__main__":
    main()