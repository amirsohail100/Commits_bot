"""
Auto Commit Bot - Chunk 1/2
Helper modules, Friendly Emoji ANSI styling, Git interface, and File Handler.
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
    =======================================================
       ✨ 🚀 AUTOMATED GIT CONTRIBUTION & COMMIT BOT 🚀 ✨
         Maintain your daily streak with ease & fun! 😎
    =======================================================
    {Colors.ENDC}"""
    print(banner)

def ensure_file_exists(filename="daily_bot.txt"):
    """Ensures that the contribution tracking text file exists."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Daily Contribution Log\n")
        print(f"{Colors.OKGREEN}🎉 [Created] New tracking file generated: {filename} 📝{Colors.ENDC}")
    else:
        print(f"{Colors.OKBLUE}🔍 [Found] Existing tracking file detected: {filename} 👌{Colors.ENDC}")

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
Core execution loop with expressive emojis, feedback, and interactive CLI prompts.
"""

def perform_commits(count, filename="daily_bot.txt", branch="main"):
    """Executes the automated commit loop."""
    print(f"\n{Colors.WARNING}⚡ Starting batch commit magic ({count} commits loading...)... ⚡{Colors.ENDC}\n")
    
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
            print(f"{Colors.FAIL}❌ Oops! Error staging changes on commit {i}: {add_err}{Colors.ENDC}")
            break
            
        # Git Commit
        commit_msg = f"chore: update daily contribution log {i}"
        commit_success, commit_out = run_git_command(f'git commit -m "{commit_msg}"')
        
        if commit_success:
            successful_commits += 1
            print(f"{Colors.OKGREEN}✅ [{i}/{count}] Commit successful! 🎯 -> '{commit_msg}'{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}💥 [{i}/{count}] Commit failed: {commit_out}{Colors.ENDC}")
            break

    print(f"\n{Colors.OKCYAN}======================================================={Colors.ENDC}")
    print(f"{Colors.BOLD}🎈 Summary: {successful_commits}/{count} commits generated smoothly! 📊{Colors.ENDC}")
    
    if successful_commits > 0:
        push_choice = input(f"\n{Colors.BOLD}🌐 Ready to push these commits to origin/{branch}? (Y/n) [Default: Y]: {Colors.ENDC}").strip().lower()
        if push_choice in ['', 'y', 'yes']:
            print(f"{Colors.WARNING}🚀 Blast off! Pushing to GitHub ({branch})...{Colors.ENDC}")
            push_success, push_msg = run_git_command(f"git push origin {branch}")
            if push_success:
                print(f"{Colors.OKGREEN}🔥 Booyah! All commits successfully pushed to GitHub! 💚{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}⚠️ Couldn't push to remote: {push_msg}{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}⏸️ Saved locally! Skipped pushing to remote repo.{Colors.ENDC}")

def main():
    print_banner()
    ensure_file_exists("daily_bot.txt")
    
    # User Input for Commit Count
    try:
        user_input = input(f"\n🎯 How many commits do you need today? (Default [10]): ").strip()
        count = int(user_input) if user_input else 10
    except ValueError:
        print(f"{Colors.FAIL}⚠️ Invalid entry! Falling back to default: 10 commits{Colors.ENDC}")
        count = 10

    # User Input for Branch Name
    branch_input = input(f"🌿 Which Git branch are you working on? (Default [main]): ").strip()
    branch = branch_input if branch_input else "main"

    perform_commits(count=count, filename="daily_bot.txt", branch=branch)

if __name__ == "__main__":
    main()