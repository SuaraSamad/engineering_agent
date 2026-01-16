# Engineering Team Crew

An AI-powered engineering team built with [CrewAI](https://crewai.com) that automates the full software development lifecycle. This multi-agent system takes high-level requirements and produces a complete solution including design documentation, backend code, frontend UI, and unit tests.

## 🚀 Features

- **Automated Software Development**: From requirements to working code in one command
- **Multi-Agent Collaboration**: Four specialized AI agents work together sequentially
- **Complete Solution**: Generates design docs, backend code, Gradio UI, and unit tests
- **Self-Contained Output**: All generated files are ready to run independently
- **Modern Tech Stack**: Uses OpenAI GPT-4o, Gradio for UI, and Python

## 🏗️ Architecture

The Engineering Team consists of four specialized AI agents that collaborate sequentially:

### Agents

1. **Engineering Lead** (`engineering_lead`)
   - **Role**: Creates detailed design specifications from high-level requirements
   - **Output**: Design document in markdown format
   - **LLM**: GPT-4o

2. **Backend Engineer** (`backend_engineer`)
   - **Role**: Implements the design as a Python module
   - **Output**: Complete, self-contained Python module
   - **LLM**: GPT-4o

3. **Frontend Engineer** (`frontend_engineer`)
   - **Role**: Creates a Gradio UI to demonstrate the backend
   - **Output**: Gradio application (`app.py`)
   - **LLM**: GPT-4o

4. **Test Engineer** (`test_engineer`)
   - **Role**: Writes comprehensive unit tests for the backend
   - **Output**: Unit test module (`test_*.py`)
   - **LLM**: GPT-4o

### Workflow

```
Requirements → Design → Code → Frontend → Tests
     ↓           ↓        ↓        ↓        ↓
  Input    Design Doc  Module   Gradio   Tests
```

## 📋 Prerequisites

- Python >=3.10 and <3.14
- [UV](https://docs.astral.sh/uv/) package manager
- OpenAI API key

## 🔧 Installation

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd engineering_team
   ```

3. **Install dependencies**:
   ```bash
   cd engineering_team
   uv pip install -e .
   ```

   Or use CrewAI's install command:
   ```bash
   crewai install
   ```

4. **Set up environment variables**:
   
   Create a `.env` file in the `engineering_team` directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## ⚙️ Configuration

### Customizing Requirements

Edit `src/engineering_team/main.py` to change the requirements and module details:

```python
requirements = """
Your requirements here...
"""

module_name = "your_module.py"
class_name = "YourClass"
```

### Customizing Agents

Modify `src/engineering_team/config/agents.yaml` to:
- Change agent roles, goals, or backstories
- Switch LLM models (currently all use `gpt-4o`)
- Adjust agent behavior

### Customizing Tasks

Modify `src/engineering_team/config/tasks.yaml` to:
- Change task descriptions
- Adjust expected outputs
- Modify task dependencies

### Customizing Crew Behavior

Edit `src/engineering_team/crew.py` to:
- Add custom tools
- Change process type (sequential/hierarchical)
- Modify agent configurations

## 🎯 Usage

### Running the Crew

From the `engineering_team` directory, run:

```bash
crewai run
```

This will:
1. Create the `output/` directory if it doesn't exist
2. Execute all agents sequentially
3. Generate all output files in the `output/` directory

### Output Files

After running, you'll find in the `output/` directory:

- `{module_name}_design.md` - Design documentation
- `{module_name}` - Backend Python module (e.g., `accounts.py`)
- `app.py` - Gradio web interface
- `test_{module_name}` - Unit tests (e.g., `test_accounts.py`)

### Running the Generated Application

1. **Navigate to the output directory**:
   ```bash
   cd output
   ```

2. **Run the Gradio app**:
   ```bash
   uv run python app.py
   ```

   Or if you have Gradio installed globally:
   ```bash
   python app.py
   ```

3. **Access the UI**:
   - The app will start a local server (usually at `http://127.0.0.1:7860`)
   - Open the URL in your browser to interact with the application

### Running Tests

From the `output/` directory:

```bash
uv run python -m pytest test_accounts.py
```

Or using Python's unittest:

```bash
uv run python test_accounts.py
```

## 📁 Project Structure

```
engineering_team/
├── src/
│   └── engineering_team/
│       ├── __init__.py
│       ├── main.py              # Main entry point with requirements
│       ├── crew.py               # Crew configuration
│       ├── config/
│       │   ├── agents.yaml       # Agent definitions
│       │   └── tasks.yaml        # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py    # Custom tools (if needed)
├── output/                       # Generated files (created at runtime)
│   ├── {module_name}_design.md
│   ├── {module_name}
│   ├── app.py
│   └── test_{module_name}
├── knowledge/                    # Knowledge base (optional)
│   └── user_preference.txt
├── tests/                        # Project tests
├── pyproject.toml                # Project configuration
├── uv.lock                       # Dependency lock file
└── README.md                     # This file
```

## 🎨 Example

The default example generates a trading simulation account management system:

- **Module**: `accounts.py` with `Account` class
- **Features**: Account creation, deposits, withdrawals, share trading
- **UI**: Gradio interface for all operations
- **Tests**: Comprehensive unit tests

## 🔄 Customization Workflow

1. **Define your requirements** in `main.py`
2. **Configure agents** in `config/agents.yaml` (if needed)
3. **Configure tasks** in `config/tasks.yaml` (if needed)
4. **Run the crew**: `crewai run`
5. **Review and test** the generated code in `output/`
6. **Iterate** by modifying requirements and running again

## 🛠️ Development

### Adding Custom Tools

1. Create your tool in `src/engineering_team/tools/custom_tool.py`
2. Import and use it in `crew.py`:

```python
from engineering_team.tools.custom_tool import MyCustomTool

@agent
def my_agent(self) -> Agent:
    return Agent(
        config=self.agents_config['my_agent'],
        tools=[MyCustomTool()],
        verbose=True,
    )
```

### Project Scripts

The project includes several scripts defined in `pyproject.toml`:

- `run_crew` - Run the crew (same as `crewai run`)
- `engineering_team` - Alias for running the crew
- `train`, `replay`, `test` - Additional crew operations

## 📦 Dependencies

- `crewai[tools]==1.8.0` - CrewAI framework with tools
- OpenAI API access (via `openai` package, included with CrewAI)
- Gradio (for generated frontend apps)

## 🐛 Troubleshooting

### Module Not Found Error

If you encounter `ModuleNotFoundError: No module named 'engineering_team'`:

```bash
cd engineering_team
uv pip install -e .
```

### API Key Issues

Ensure your `.env` file contains:
```
OPENAI_API_KEY=your_actual_key_here
```

### Gradio Version Issues

The generated `app.py` uses modern Gradio API (compatible with Gradio 6.3.0+). If you encounter issues, ensure Gradio is installed:

```bash
uv pip install gradio
```

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/crewAIInc/crewAI)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)
- [Gradio Documentation](https://www.gradio.app/docs/)

## 📝 License

[Add your license here]

## 🤝 Contributing

[Add contribution guidelines here]

## 🙏 Acknowledgments

Built with [CrewAI](https://crewai.com) - A framework for orchestrating role-playing, autonomous AI agents.

---

**Note**: This project uses OpenAI's GPT-4o model. Ensure you have sufficient API credits and are aware of usage costs.
