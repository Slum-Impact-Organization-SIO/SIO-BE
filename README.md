# SIO-BE Backend

This repository contains the Python backend API for SIO. It is built using **FastAPI** and is configured with an automated continuous integration (CI) pipeline via **GitHub Actions** and pre-commit hooks.

## Table of Contents

- [Project Structure](#project-structure)
- [Local Development Setup](#local-development-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting up Git Hooks (Pre-commit)](#setting-up-git-hooks-pre-commit)
  - [Running the Development Server](#running-the-development-server)
- [Verification and Quality Checks](#verification-and-quality-checks)
  - [Running Tests](#running-tests)
  - [Linting and Formatting](#linting-and-formatting)
  - [Static Type Checking](#static-type-checking)
- [CI/CD Pipeline](#cicd-pipeline)

---

## Project Structure

```text
SIO-BE/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI configuration
├── app/
│   ├── __init__.py
│   └── main.py                # FastAPI entrypoint and endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py           # pytest test suite
├── .gitignore                 # Git ignore file for Python
├── .pre-commit-config.yaml    # Pre-commit git hooks configuration
├── pyproject.toml             # Ruff (linter/formatter) and mypy settings
├── README.md                  # This file
└── requirements.txt           # Project dependencies
```

---

## Local Development Setup

### Prerequisites

- **Python 3.12** or higher installed on your local machine.

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd SIO-BE
   ```

2. **Create a virtual environment**:
   - On Windows:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Setting up Git Hooks (Pre-commit)

We use `pre-commit` to automatically run code formatters, linters, and type checkers before each git commit.

1. **Install the git hook scripts**:
   ```bash
   pre-commit install
   ```

2. **(Optional) Run hooks against all files manually**:
   ```bash
   pre-commit run --all-files
   ```

Now, every time you run `git commit`, the hooks defined in [.pre-commit-config.yaml](.pre-commit-config.yaml) will run automatically. If any checks fail, the commit is aborted so you can fix the issues.

### Running the Development Server

Start the FastAPI application locally with auto-reload:
```bash
uvicorn app.main:app --reload
```
Once started, the API will be available at:
- **API Root**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive OpenAPI Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Redoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Verification and Quality Checks

To ensure code quality, you can run these commands locally. They align with the checks run in the CI pipeline and pre-commit hooks.

### Running Tests

Execute the unit tests using `pytest`:
```bash
pytest -v
```

### Linting and Formatting

We use **Ruff** for fast linting and formatting.

- To check code style and linting issues:
  ```bash
  ruff check .
  ```
- To verify formatting:
  ```bash
  ruff format --check .
  ```
- To automatically fix format and lint issues:
  ```bash
  ruff format .
  ruff check --fix .
  ```

### Static Type Checking

We use **mypy** to verify type hints in the application logic:
```bash
mypy app
```

## Branching & Contribution Rules

To maintain codebase stability, ensure all tests pass, and track history cleanly, please adhere to the following rules:

* **No direct pushes:** Never push code directly to the `main`, `master`, `dev`, or `staging` branches.
* **Use feature/change branches:** Create a dedicated branch for your work (e.g., `feature/add-auth` or `bugfix/fix-login-error`).
* **Submit a Pull Request:** Open a PR targeting the appropriate branch to merge your changes. The CI pipeline must pass successfully, and code reviews should be completed before merge.

---

## CI/CD Pipeline

The GitHub Actions configuration file is located in [.github/workflows/ci.yml](.github/workflows/ci.yml). 

It automatically runs on:
- Every push to the `master` or `main` branches.
- Every Pull Request targeting `master` or `main`.

### Jobs Performed:
1. **Checkout Code**: Retrieves the repository files.
2. **Setup Python**: Installs Python 3.12 with pip caching enabled.
3. **Install Dependencies**: Installs the contents of `requirements.txt`.
4. **Lint and Format Check**: Assures that the code satisfies formatting conventions using Ruff.
5. **Type Safety**: Verifies strict typing correctness with mypy.
6. **Unit Tests**: Runs `pytest` to execute all tests under the `tests/` directory.
