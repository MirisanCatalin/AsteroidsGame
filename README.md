# Build an AI Agent 🤖

A Python-based CLI tool that acts like a mini "Claude Code" agent. Give it a coding task, and it will automatically read, modify, and execute Python files to try and solve it!

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![CLI Tool](https://img.shields.io/badge/Tool-CLI-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Unspecified-lightgrey.svg)](#license)

***

## ✨ Features

This agent implements a basic AI-powered workflow for automating Python coding tasks:

* **Task Execution:** Accepts user-provided coding tasks via the CLI.
* **File Management:** Scans directories, reads files, and overwrites contents when needed.
* **Code Execution:** Runs Python files to test and validate changes.
* **Iterative Problem Solving:** Chooses functions intelligently and repeats until the task is complete (or fails hilariously 😅).
* **AI-Powered Decisions:** Uses a pre-trained LLM via Google Gemini API to determine actions.

---

## 🚀 Getting Started

Follow these instructions to get your agent running locally.

### Prerequisites

* Python 3.10+  
* [uv](https://uv.dev) project and package manager  
* Unix-like shell (e.g., zsh or bash)  

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Build-AI-Agent.git
cd Build-AI-Agent

# Install dependencies (if any)
pip install -r requirements.txt
```
# Usage
```
uv run main.py "fix my calculator app, it's not starting correctly"
```

## Example Output:
```
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly.
# The output shows the expression and the result in a formatted way.
```
🎓 What I Learned

Building this AI Agent taught me practical concepts in both Python and AI tooling:

1. Multi-Directory Python Projects

Learned to structure a larger Python project with modules and functions spread across directories.

2. AI Tools in Practice

Gained hands-on experience with using pre-trained LLMs to solve tasks, understanding prompts, and iterative problem solving.

3. Functional Programming

Applied Python functions effectively to manage file I/O, code execution, and agent logic.

4. CLI Tool Development

Developed a user-friendly CLI interface, learning argument parsing and output formatting.

🛠️ Built With

Python – Core language

Google Gemini API – Pre-trained LLM for decision-making

uv – Project and package management

🤝 Acknowledgements

Inspired by Cursor and Claude Code, this project is a hands-on exploration of AI-assisted programming agents and demonstrates how to leverage LLMs in real-world Python workflows.
