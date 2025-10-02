# Agentic Developer Toolkit

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Claude Compatible](https://img.shields.io/badge/Claude%204.5-Compatible-orange.svg)](https://www.anthropic.com/claude)
[![Gemini Compatible](https://img.shields.io/badge/Gemini%202.5-Compatible-blue.svg)](https://ai.google.dev/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Master AI-assisted development workflows with Claude 4.5 and Gemini 2.5**

An open-source collection of scripts, best practices, and practical "recipes" designed to supercharge developer productivity with the latest large language model (LLM) coding assistants.

[Features](#-key-features) • [Quick Start](#-quick-start) • [Recipes](#-recipes-library) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Supported LLMs](#-supported-llm-providers)
- [Quick Start](#-quick-start)
- [LLM Provider Setup](#-llm-provider-setup)
- [Usage Examples](#-usage-examples)
- [Recipes Library](#-recipes-library)
- [Context Management](#-managing-context-windows)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

Move beyond basic prompting and integrate AI-assisted workflows directly into your development environment for maximum efficiency. This toolkit is designed for developers who want to leverage the latest Claude 4.5 Sonnet and Gemini 2.5 Pro models for real coding tasks—not just conversations.

**Perfect for:**
- Developers working with large, complex codebases
- Teams wanting to standardize AI-assisted workflows
- Anyone tired of copy-pasting code back and forth with ChatGPT
- Professionals seeking reproducible, automated AI coding patterns

**Time Saved:** Users report 40-60% faster completion of routine coding tasks like refactoring, documentation, and test generation.

---

## ✨ Key Features

- **🔍 Automated Context Gathering** - Python scripts to scan complex codebases and package relevant context, minimizing manual setup for AI tasks
- **📖 Practical Recipes** - Library of copy-pasteable prompts and workflow guides for common development tasks (refactoring, documentation, unit tests)
- **⚡ Workflow Integration Scripts** - Shell scripts to chain together CLI commands and LLM interactions for powerful, one-line automations
- **📚 Authoritative Guides** - In-depth documentation on advanced topics like prompt engineering for code, managing context windows, and fine-tuning AI assistant behavior
- **🤖 Multi-LLM Support** - Works seamlessly with both Anthropic's Claude 4.5 and Google's Gemini 2.5
- **🎯 Smart Context Limits** - Automatically manages token limits to stay within model constraints
- **💰 Cost Optimization** - Intelligent model selection to minimize API costs while maximizing quality

---

## 🤖 Supported LLM Providers

### Latest Models (Recommended)

| Provider | Latest Model | Context Window | Best For |
|----------|--------------|----------------|----------|
| **Anthropic Claude 4** | Sonnet 4.5 | 200K tokens | Code generation, refactoring, complex reasoning, security analysis |
| **Google Gemini 2** | 2.5 Pro | 2M tokens | Massive codebase analysis, repository-wide tasks, cost-effective workflows |

### All Supported Models

| Model | Context Window | Input Cost* | Output Cost* | Recommended Use |
|-------|----------------|-------------|--------------|-----------------|
| **claude-sonnet-4-5-20250929** ⭐ | 200K | $3/1M | $15/1M | Primary choice for all coding tasks |
| claude-opus-4-20250514 | 200K | $15/1M | $75/1M | Most capable, complex architecture |
| claude-3-5-sonnet-20241022 | 200K | $3/1M | $15/1M | Legacy support, stable |
| **gemini-2.5-pro** ⭐ | 2M | $1.25/1M | $5/1M | Large repos, cost-effective analysis |
| gemini-2.0-flash-exp | 1M | $0.075/1M | $0.30/1M | Fast iteration, high-volume tasks |
| gemini-1.5-pro | 2M | $1.25/1M | $5/1M | Legacy support |

*Prices as of October 2025, subject to change

**⭐ = Recommended for most users**

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Git
- An API key for [Claude](https://console.anthropic.com/) or [Gemini](https://aistudio.google.com/)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/JTCruzado/agentic-developer-toolkit.git
cd agentic-developer-toolkit

# 2. Set up virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your API keys
cp .env.example .env
# Edit .env and add your API keys (see LLM Provider Setup below)
```

### Verify Installation

```bash
# Test with a simple command
python scripts/context_gatherer.py --help

# Should display help text with available options
```

**Next Step:** Configure your LLM provider (see below)

---

## 🔑 LLM Provider Setup

Choose your preferred LLM provider and follow the setup steps:

### Option A: Anthropic Claude 4.5 (Recommended)

1. **Get your API key**:
   - Visit [Anthropic Console](https://console.anthropic.com/)
   - Sign up or log in
   - Navigate to API Keys → Create new key
   - Copy the key (starts with `sk-ant-`)

2. **Add to `.env`**:
   ```bash
   LLM_PROVIDER=anthropic
   ANTHROPIC_API_KEY=sk-ant-xxxxx
   DEFAULT_MODEL=claude-sonnet-4-5-20250929
   ```

3. **Available Claude 4 models**:
   - `claude-sonnet-4-5-20250929` ⭐ **RECOMMENDED** - Latest, smartest, best for coding
   - `claude-opus-4-20250514` - Most capable for complex reasoning
   - `claude-3-5-sonnet-20241022` - Previous generation (stable)

**Why Claude 4.5 Sonnet?**
- 🚀 Superior code reasoning and following instructions
- 🔒 Excellent at security analysis
- 📝 Natural documentation generation
- ⚡ Faster than Opus 4 with similar quality
- 💰 Better price/performance ratio

### Option B: Google Gemini 2.5 Pro

1. **Get your API key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Click "Get API Key"
   - Copy the key (starts with `AIzaSy`)

2. **Add to `.env`**:
   ```bash
   LLM_PROVIDER=google
   GOOGLE_API_KEY=AIzaSyxxxxx
   DEFAULT_MODEL=gemini-2.5-pro
   ```

3. **Available Gemini 2 models**:
   - `gemini-2.5-pro` ⭐ **RECOMMENDED** - Latest, 2M context, excellent reasoning
   - `gemini-2.0-flash-exp` - Fastest, 1M context, ultra-low cost
   - `gemini-1.5-pro` - Previous generation (stable)

**Why Gemini 2.5 Pro?**
- 📊 Massive 2M token context window
- 💰 75% cheaper than Claude Opus
- ⚡ Fast inference speeds
- 🔍 Excellent for large codebase analysis
- 🎯 Strong multimodal capabilities

### Complete `.env` Example

```bash
# LLM Configuration
LLM_PROVIDER=anthropic  # or 'google'

# Primary Model Selection
# For Claude: claude-sonnet-4-5-20250929 (recommended)
# For Gemini: gemini-2.5-pro (recommended)
DEFAULT_MODEL=claude-sonnet-4-5-20250929

# Anthropic Claude API
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Google Gemini API
GOOGLE_API_KEY=AIzaSyxxxxx

# Optional Settings
MAX_TOKENS=8192
TEMPERATURE=0.7
DEBUG_MODE=false
```

---

## 💡 Usage Examples

### Example 1: Generate Unit Tests with Claude 4.5

```bash
# Step 1: Gather context for your function
python scripts/context_gatherer.py \
  --path ./src \
  --query "function calculate_total_price" \
  --output context.txt

# Step 2: Generate comprehensive tests using Claude 4.5 Sonnet
python scripts/generate_tests.py \
  --context context.txt \
  --model claude-sonnet-4-5-20250929 \
  --output tests/test_pricing.py

# Result: Complete test file with edge cases, mocks, and documentation
```

### Example 2: Analyze Large Codebase with Gemini 2.5 Pro

```bash
# Leverage 2M context window to analyze entire repository
python scripts/analyze_codebase.py \
  --path . \
  --model gemini-2.5-pro \
  --include-all-files \
  --output analysis.md

# Result: Comprehensive architecture analysis, dependency graph, improvement suggestions
```

### Example 3: Refactor Legacy Code with Claude 4.5

```bash
# Refactor an entire file to modern standards
python scripts/refactor_code.py \
  --file src/legacy/payment_processor.py \
  --instruction "Refactor to use async/await, add type hints, improve error handling" \
  --model claude-sonnet-4-5-20250929 \
  --output src/payment_processor.py
```

### Example 4: Cost-Effective Documentation with Gemini 2.0 Flash

```bash
# Generate comprehensive docs using ultra-fast, cheap model
python scripts/generate_docs.py \
  --directory ./src \
  --format markdown \
  --model gemini-2.0-flash-exp \
  --output docs/api/

# Result: Complete API documentation at fraction of the cost
```

### Example 5: Hybrid Workflow (Best of Both Worlds)

```bash
# Use Gemini for broad analysis (2M context, cheap)
python scripts/analyze_codebase.py \
  --model gemini-2.5-pro \
  --output analysis.md

# Use Claude 4.5 for precise refactoring (better code quality)
python scripts/refactor_code.py \
  --context analysis.md \
  --model claude-sonnet-4-5-20250929 \
  --file src/core.py
```

---

## 📚 Recipes Library

Recipes are pre-built prompts and workflows optimized for Claude 4.5 and Gemini 2.5.

### Available Recipes

| Recipe | Description | Best Model | Time Saved |
|--------|-------------|------------|------------|
| `refactor_function` | Improve code quality, readability, and structure | Claude 4.5 Sonnet | ~30 min |
| `add_error_handling` | Add comprehensive try/catch and validation | Claude 4.5 Sonnet | ~20 min |
| `generate_unit_tests` | Create test cases with high coverage | Claude 4.5 Sonnet | ~45 min |
| `write_docstrings` | Generate comprehensive documentation | Gemini 2.0 Flash | ~25 min |
| `optimize_performance` | Identify and fix performance bottlenecks | Claude Opus 4 | ~40 min |
| `security_audit` | Find security vulnerabilities and suggest fixes | Claude 4.5 Sonnet | ~60 min |
| `add_type_hints` | Add Python type annotations throughout | Gemini 2.0 Flash | ~20 min |
| `migrate_to_async` | Convert synchronous code to async/await | Claude 4.5 Sonnet | ~50 min |
| `analyze_architecture` | Repository-wide architectural analysis | Gemini 2.5 Pro | ~35 min |
| `dependency_audit` | Analyze and optimize dependencies | Gemini 2.5 Pro | ~30 min |

### Using a Recipe

```bash
# List all available recipes
python scripts/recipe.py --list

# Run a recipe with Claude 4.5 Sonnet
python scripts/recipe.py \
  --name refactor_function \
  --file src/utils/parser.py \
  --model claude-sonnet-4-5-20250929

# Run a recipe with Gemini 2.5 Pro
python scripts/recipe.py \
  --name analyze_architecture \
  --path . \
  --model gemini-2.5-pro

# Customize recipe parameters
python scripts/recipe.py \
  --name generate_unit_tests \
  --file src/calculator.py \
  --coverage-target 95 \
  --include-integration-tests
```

### Creating Custom Recipes

Create your own recipes for team-specific patterns:

```bash
# Start from a template
python scripts/recipe.py --create my_custom_recipe

# Edit the generated file
# recipes/my_custom_recipe.yaml
```

See [docs/CREATING_RECIPES.md](docs/CREATING_RECIPES.md) for the complete guide.

---

## 🧠 Managing Context Windows

### Understanding Context Limits

| Model | Context Window | Tokens per File* | Recommended Usage |
|-------|----------------|------------------|-------------------|
| Claude 4.5 Sonnet | 200K tokens | ~50 files | Large features, complex modules |
| Claude Opus 4 | 200K tokens | ~50 files | Deep architectural analysis |
| Gemini 2.5 Pro | 2M tokens | ~500 files | **Entire repositories** |
| Gemini 2.0 Flash | 1M tokens | ~250 files | Fast repository scans |

*Assuming ~4K tokens per file (varies by file size and language)

### Smart Context Gathering

The `context_gatherer.py` script intelligently limits context:

```bash
# For Claude 4.5 (200K limit) - targeted context
python scripts/context_gatherer.py \
  --path ./src \
  --query "authentication and session management" \
  --max-tokens 150000 \
  --exclude "tests,migrations,node_modules" \
  --output context.txt

# For Gemini 2.5 (2M limit) - entire repository
python scripts/context_gatherer.py \
  --path . \
  --query "entire codebase structure" \
  --max-tokens 1800000 \
  --model gemini-2.5-pro \
  --output full_context.txt
```

### Model Selection Strategy

```bash
# Use Claude 4.5 for: Precision tasks, security, complex refactoring
--model claude-sonnet-4-5-20250929

# Use Gemini 2.5 for: Large repos, architecture analysis, cost efficiency
--model gemini-2.5-pro

# Use Gemini 2.0 Flash for: Documentation, fast iteration, high volume
--model gemini-2.0-flash-exp
```

### Best Practices

1. **Use targeted queries** - Be specific: "error handling in payment module" vs. "errors"
2. **Exclude irrelevant paths** - Use `.agentic-ignore` file (like `.gitignore`)
3. **Choose the right model** - Claude for precision, Gemini for breadth
4. **Chunk large operations** - Break 1000-line refactors into 200-line chunks
5. **Monitor token usage** - Use `--verbose` flag to see token counts

### Example `.agentic-ignore`

```
# Don't include in context
node_modules/
venv/
*.pyc
*.log
tests/fixtures/
migrations/
.git/
dist/
build/
__pycache__/
.pytest_cache/
```

---

## 🆚 Claude 4.5 vs Gemini 2.5: When to Use What

### Task-Based Model Selection

| Task | Best Model | Why |
|------|------------|-----|
| **Code refactoring** | Claude 4.5 Sonnet | Superior code reasoning, follows instructions precisely |
| **Large codebase analysis** | Gemini 2.5 Pro | 2M context window, sees entire repositories |
| **Security audits** | Claude 4.5 Sonnet | Better at identifying subtle vulnerabilities |
| **Fast documentation** | Gemini 2.0 Flash | 75x cheaper, fast, good enough quality |
| **Complex architecture** | Claude Opus 4 | Best reasoning for system design decisions |
| **Cost-sensitive workflows** | Gemini 2.0 Flash | Ultra-low cost for high-volume tasks |
| **Test generation** | Claude 4.5 Sonnet | More thorough edge case coverage |
| **Dependency analysis** | Gemini 2.5 Pro | Can analyze entire dependency trees at once |

### Cost Comparison (October 2025)

| Model | 100K Input + 10K Output | Typical Refactor | Full Repo Analysis |
|-------|------------------------|------------------|-------------------|
| Claude 4.5 Sonnet | $0.45 | $0.60 | $3.50 |
| Claude Opus 4 | $2.25 | $3.00 | $17.50 |
| Gemini 2.5 Pro | $0.175 | $0.25 | $1.20 |
| Gemini 2.0 Flash | $0.0105 | $0.015 | $0.08 |

**💡 Pro Tip:** Use Gemini 2.5 for exploration and broad analysis (cheap, massive context), then Claude 4.5 for precise implementation (reliable, high quality).

### Hybrid Workflow Example

```bash
# Phase 1: Broad analysis with Gemini 2.5 (entire repo, cheap)
python scripts/analyze_codebase.py \
  --model gemini-2.5-pro \
  --path . \
  --output analysis.md
# Cost: ~$1.20

# Phase 2: Targeted refactoring with Claude 4.5 (precision)
python scripts/refactor_code.py \
  --context analysis.md \
  --model claude-sonnet-4-5-20250929 \
  --file src/core.py
# Cost: ~$0.60

# Total: $1.80 (vs $3.50 if using only Claude)
# Result: Best quality at lower cost
```

---

## 📚 Documentation

### For Users
- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup with troubleshooting
- **[Configuration Guide](docs/CONFIGURATION.md)** - Advanced `.env` options
- **[Recipe Catalog](docs/RECIPES.md)** - Complete list with examples
- **[Workflow Guide](docs/WORKFLOWS.md)** - Build custom automation chains
- **[Best Practices](docs/BEST_PRACTICES.md)** - Tips for effective AI-assisted coding
- **[Model Selection Guide](docs/MODEL_SELECTION.md)** - Choose the right LLM for each task
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[FAQ](docs/FAQ.md)** - Frequently asked questions

### For Developers
- **[Development Guide](docs/DEVELOPMENT.md)** - Contributing to the toolkit
- **[Architecture](docs/ARCHITECTURE.md)** - How the toolkit works internally
- **[API Reference](docs/API.md)** - Python API documentation
- **[Creating Recipes](docs/CREATING_RECIPES.md)** - Build custom recipes

### Tutorials
- **[Tutorial 1: Your First AI Refactoring](docs/tutorials/01-first-refactor.md)**
- **[Tutorial 2: Building a Custom Workflow](docs/tutorials/02-custom-workflow.md)**
- **[Tutorial 3: Advanced Context Management](docs/tutorials/03-context-management.md)**
- **[Tutorial 4: Cost Optimization Strategies](docs/tutorials/04-cost-optimization.md)**

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Primary Language** | Python 3.9+ |
| **Scripting** | Bash/Shell Scripting |
| **LLM APIs** | Anthropic Claude 4 API, Google Gemini 2 API |
| **Documentation** | Markdown |
| **Configuration** | YAML, .env |
| **Core Dependencies** | anthropic>=0.40.0, google-generativeai>=0.8.0, python-dotenv, pyyaml |

---

## 🤝 Contributing

We love contributions! Whether you're adding new recipes, improving scripts, or enhancing documentation, your help is welcome.

### Ways to Contribute
- 🐛 Report bugs via [GitHub Issues](https://github.com/JTCruzado/agentic-developer-toolkit/issues)
- 💡 Suggest recipes in [Discussions](https://github.com/JTCruzado/agentic-developer-toolkit/discussions)
- 📝 Improve documentation
- 🔧 Submit pull requests
- 🎯 Share recipes you've created

### Quick Start for Contributors

```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/agentic-developer-toolkit.git
cd agentic-developer-toolkit

# Create feature branch
git checkout -b feature/my-new-recipe

# Make changes, commit, and push
git commit -m "feat: add recipe for API client generation"
git push origin feature/my-new-recipe
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Support

### Getting Help
- 📖 **Documentation** - Start with [docs/](docs/)
- 💬 **Discussions** - Ask questions in [GitHub Discussions](https://github.com/JTCruzado/agentic-developer-toolkit/discussions)
- 🐛 **Bug Reports** - File issues at [GitHub Issues](https://github.com/JTCruzado/agentic-developer-toolkit/issues)
- 🔑 **API Key Issues** - See [Configuration Guide](docs/CONFIGURATION.md)

### Show Your Support
- ⭐ Star this repository
- 📢 Share with other developers
- 🐛 Report bugs you find
- 💡 Suggest new recipes
- 🎓 Contribute tutorials

---

## 🗺️ Roadmap

**Q4 2025**
- [x] Claude 4.5 Sonnet support
- [x] Gemini 2.5 Pro support
- [ ] Advanced cost tracking and budgeting
- [ ] VS Code extension for one-click recipes
- [ ] Docker containerized workflows

**Q1 2026**
- [ ] Support for Claude Opus 4.1
- [ ] Multi-model parallel execution
- [ ] Recipe marketplace
- [ ] Team collaboration features
- [ ] Custom model fine-tuning guides

**Q2 2026**
- [ ] GUI for non-technical users
- [ ] Integration with popular IDEs (JetBrains, Sublime)
- [ ] Automated test suite for recipes
- [ ] Enterprise features (SSO, audit logs)

Vote on features in [Discussions](https://github.com/JTCruzado/agentic-developer-toolkit/discussions)!

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/JTCruzado/agentic-developer-toolkit?style=social)
![GitHub forks](https://img.shields.io/github/forks/JTCruzado/agentic-developer-toolkit?style=social)
![GitHub issues](https://img.shields.io/github/issues/JTCruzado/agentic-developer-toolkit)
![Last commit](https://img.shields.io/github/last-commit/JTCruzado/agentic-developer-toolkit)

---

<div align="center">



**Powered by Claude 4.5 Sonnet & Gemini 2.5 Pro**

[⬆ Back to Top](#agentic-developer-toolkit)

</div>
