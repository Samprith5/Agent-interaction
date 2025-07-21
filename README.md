# Agent-interaction

Here's a sample **README.md** for your Two-Agent Python Code Generator:

---

# 🤖 Two-Agent Python Code Generator

*Built with LangChain + DeepSeek + LM Studio*

## Overview

This is a simple Python-based code generator that simulates a two-agent system:

* **Agent 1 (Messenger):** Handles user inputs and returns code responses.
* **Agent 2 (Coder):** Generates Python code using a local LLM (DeepSeek or any other supported by LM Studio).

The model is accessed via **LangChain** and **LM Studio API Server**, making it easy to interact with local models like `deepseek-coder-6.7b-instruct`.

---

## Features

* Generates Python functions for any natural language task request.
* Pure code output — no extra explanations.
* Works with any OpenAI-compatible local model via LM Studio.

---

## Requirements

* **Python 3.9+**
* **LM Studio** (with API Server running)
* Local Model (`deepseek-coder-6.7b-instruct`)
* Python Packages:

  * `langchain-core`
  * `langchain-openai`

Install dependencies:

```bash
pip install langchain-core langchain-openai
```

---

## Usage

1. **Start LM Studio API Server**

   * Open LM Studio.
   * Go to **API Server** tab.
   * Start the server with your preferred model.

2. **Run the Script**

```bash
python agent.py
```

3. **Interact**

```bash

<img width="758" height="356" alt="image" src="https://github.com/user-attachments/assets/475e5d6f-d3fa-4bdc-ac67-9933195b89c8" />



Type `exit` or `quit` to stop.

---

## How It Works

* **Agent 1** passes your task to **Agent 2**.
* **Agent 2** uses the selected LLM to generate Python code.
* You receive only clean, executable code.
