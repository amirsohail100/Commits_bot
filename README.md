# 🟢 GitHub Contribution Consistency & Automation Bot

Welcome to this repository! If you are a recruiter, interviewer, or a fellow developer exploring my profile, **thank you for visiting.** I believe in complete transparency, which is why this repository exists and is kept public.

---

## 📢 Why Does This Repository Exist? (A Note on Transparency)

As a passionate developer and student, my primary focus is on **deep learning, core computer science concepts, and building meaningful projects** (like NLP pipelines and LSTM networks).

However, balancing intensive offline study, college work, and high-quality project development makes it difficult to push code to GitHub every single day. To solve this and keep my profile consistently active, I use a **50/50 Hybrid Approach**:

1. **50% Real Work:** I commit daily code updates, bug fixes, and feature additions from my actual working projects.
2. **50% Automation:** I use this dummy repository to bridge the gap on busy days, automated to generate calculated minor commits that maintain my consistency streak.

---

## 🧠 Why This Isn't "Cheating" — It's Smart Time Management

- **Quality Over Quantity:** Pushing 10-15 minor commits daily on a real project just to keep a streak green slows down actual deep learning and architecture design.
- **Prioritizing Learning:** My time is better spent reading research papers, understanding algorithms, or debugging code offline rather than figuring out what to push to GitHub for a streak.
- **Full Disclosure:** True cheaters hide their automated repositories or keep them private. I have kept this public and fully documented because I value honesty with potential employers.

---

## ⚡ Quick One-Liner Alternative (Instant Execution in Git Bash)

If you don't want to run the Python script, you can directly copy-paste this single Bash command into your Git Bash terminal to generate and push commits instantly:

```bash
for i in {1..15}; do echo "Daily update $i" >> daily_bot.txt; git add daily_bot.txt; git commit -m "chore: update daily contribution log $i"; done; git push origin main
```

---

## 🛠️ Tech Stack & How the Scripts Work

### 1️⃣ Interactive Python CLI Bot (`bot.py`) 🚀 _(Recommended)_

We upgraded the automation into a fun, interactive terminal application with a clean UI, colored logs, and emojis!

#### ✨ Key Features:

- 🎨 **Vibrant Terminal UI:** Formatted ANSI colors and emojis.
- 📁 **Auto File Creation:** Creates `daily_bot.txt` automatically if missing.
- 🎯 **Custom Goal:** Choose how many commits to make (Default is 10).
- 🌿 **Branch Flexibility:** Target any git branch (Default is `main`).
- 🌐 **Interactive Push:** Option to push to remote origin or keep local.

#### 🏃 Local Execution:

```bash
python bot.py
```

---

### 2️⃣ Multi-Line Bash Script Loop ⚡

Alternatively, you can also run the expanded multi-line loop in Git Bash:

```bash
for i in {1..15}; do
  echo "Daily update $i" >> daily_bot.txt;
  git add daily_bot.txt;
  git commit -m "chore: update daily contribution log $i";
done;
git push origin main
```

---

## 🚀 One-Liner Execution (No Repository Cloning Needed!)

Aapko repository clone karne ki bilkul zaroorat nahi hai. Bas apne Git Bash / Terminal mein niche diye gaye **dono options** me se koi bhi **ek command** paste karke run karein:

### 🔹 Option 1: Remote Python Bot Run (Interactive UI + Custom Commits)

Direct remote `bot.py` script run karne ke liye:

```bash
curl -sSL https://raw.githubusercontent.com/amirsohail100/Commits_bot/main/bot.py | python -
```
