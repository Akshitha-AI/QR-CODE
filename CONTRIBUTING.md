# Contributing to QR Code Generator

Thank you for your interest in contributing to the QR Code Generator project! This document provides guidelines and instructions for contributing to our project.

## Code of Conduct

Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive community.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (optional, for containerized development)
- Git

### Setting Up Your Development Environment

1. **Clone the repository:**
   ```bash
   git clone https://gitlab.com/surakanti-akshitha/qr-code.git
   cd qr-code
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```

## Development Workflow

### Branch Naming Convention

- `feature/description` - for new features
- `bugfix/description` - for bug fixes
- `docs/description` - for documentation updates
- `refactor/description` - for code refactoring
- `test/description` - for test improvements

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): subject

body

footer
```

**Types:** feat, fix, docs, style, refactor, test, chore, ci

**Example:**
```
feat(qr-generation): add support for batch processing

- Add batch endpoint to handle multiple QR codes
- Implement queue system for large batches
- Add progress tracking

Closes #42
```

### Creating a Pull Request

1. Create a new branch from `main`
2. Make your changes
3. Ensure all tests pass: `pytest`
4. Ensure code quality checks pass: `ruff check .`, `mypy src/`
5. Push your branch and create a merge request
6. Wait for CI/CD pipeline to pass
7. Request review from maintainers

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_qr_generator.py
```

### Writing Tests

- Place test files in the `tests/` directory
- Name test files as `test_*.py`
- Follow the AAA pattern: Arrange, Act, Assert
- Aim for 80%+ code coverage

## Code Quality

### Code Style

We use [Ruff](https://astral.sh/ruff/) for linting and formatting.

```bash
# Check code style
ruff check src/

# Format code
ruff format src/
```

### Type Checking

We use [Mypy](https://www.mypy-lang.org/) for static type analysis.

```bash
mypy src/
```

### Security Scanning

```bash
# Run Bandit for security issues
bandit -r src/

# Check dependencies for vulnerabilities
pip-audit
```

## Documentation

- Update the [USER_MANUAL.md](USER_MANUAL.md) for user-facing changes
- Update the [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) for API changes
- Update the [CHANGELOG.md](CHANGELOG.md) for notable changes
- Add docstrings to all functions and classes (Google-style)

## Performance Considerations

- Profile code before optimizing
- Consider memory usage for large QR code batches
- Document any performance-critical sections

## Reporting Issues

Before creating an issue, please:

1. Check if the issue already exists
2. Provide a minimal reproducible example
3. Include environment details (OS, Python version, etc.)
4. Include error messages and logs

## License

By contributing to this project, you agree that your contributions will be licensed under the [AGPL-3.0 License](LICENSE).

## Recognition

We recognize and appreciate all contributors! Your efforts help make this project better.

## Questions?

- Open an issue for questions
- Check existing documentation in the `docs/` directory
- Review the [API Documentation](docs/API_DOCUMENTATION.md)

---

**Happy contributing!** 🎉
