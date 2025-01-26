# UV Project Create and Setup VS Code

```bash
uv version

uv help

uv init --package explore-uv
```

This command sets up a project structured for packaging, placing your code inside a `src` directory, aligning with best practices for Python project structures.

```bash
cd first_program

code .
```

Use `code .` on terminal or open the directory **first_program** in VSCode

Now Create **Virtual environment**:

```bash
uv venv
```

Activate **virtual environment**
1. For macOS use
```bash
source .venv/bin/activate
````
2. For Windows use
```bash
.venv\Scripts\activate
```

Select Recommended Python Interpreter (./.venv/bin/python) created by **virtual envirnoment** in VSCode

```bash
uv run first-program
```