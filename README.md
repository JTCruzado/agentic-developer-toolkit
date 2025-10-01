# The Agentic Coding Cookbook & Toolkit 

An open-source collection of scripts, best practices, and practical "recipes" designed to supercharge developer productivity with large language model (LLM) coding assistants like Google's Gemini and Anthropic's Claude.

This toolkit is for developers who want to move beyond basic prompting and integrate AI-assisted workflows directly into their development environment for maximum efficiency.

---

##  Features

* **Automated Context Gathering:** A suite of Python scripts to scan complex codebases and package relevant context, minimizing manual setup for AI tasks.
* **Practical Recipes:** A library of copy-pasteable prompts and workflow guides for common development tasks (e.g., refactoring, documentation generation, unit test creation).
* **Workflow Integration Scripts:** Shell scripts to chain together CLI commands and LLM interactions for powerful, one-line automations.
* **Authoritative Guides:** In-depth documentation on advanced topics like prompt engineering for code, managing context windows, and fine-tuning your AI assistant's behavior.

---

##  Technologies Used

* **Primary Language:** Python
* **Scripting:** Shell Scripting (Bash)
* **Documentation:** Markdown

---

##  Getting Started

### Prerequisites

* Python 3.9+
* Git
* An API key for your chosen LLM provider (e.g., Google AI Studio, Anthropic)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/JTCruzado/agentic-coding-cookbook.git](https://github.com/JTCruzado/agentic-coding-cookbook.git)
    cd agentic-coding-cookbook
    ```

2.  **Set up a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure your API key:**
    Create a `.env` file by copying the example file:
    ```sh
    cp .env.example .env
    ```
    Now, open the `.env` file and add your API key.

---

## 📖 Usage & Examples

### Example: Automated Context Gathering

The `context_gatherer.py` script helps you quickly pull together all relevant code snippets for a specific task.

**Scenario:** You need to refactor a function named `calculate_total_price` in your e-commerce application. This function depends on several other helper functions and classes across multiple files.

**Command:**
```sh
python scripts/context_gatherer.py \
  --path /path/to/your/project \
  --query "function calculate_total_price" \
  --output context.txt
