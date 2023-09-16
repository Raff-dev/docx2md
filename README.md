# DOCX to Markdown Pre-Commit Hook

## Overview

**Purpose**: To provide Git diff and GitHub preview capabilities for DOCX files by automatically converting them into Markdown format.

**Technology**: This pre-commit hook uses Python, GitPython, and pypandoc.

---

## Features

- **Automatic Conversion**: Seamlessly creates a copy of or modified DOCX files to Markdown during `git commit`.
- **GitHub Preview**: View changes directly on GitHub via the generated Markdown files.

---

## Getting Started

### Prerequisites

- Python 3.x
- Git
- Pre-commit package

### Installation

1. **Navigate to your project's root directory and install pre-commit**
    ```
    pip install pre-commit
    ```

2. **Create a `.pre-commit-config.yaml` file in your repository with the following content**
    ```yaml
    repos:
    -   repo: https://github.com/Raff-dev/docx2md
        rev: 1.0.0 # Replace with the latest release tag
        hooks:
        -   id: docx2md
            verbose: true
    ```

3. **Run pre-commit install to set up the git hook scripts**
    ```
    pre-commit install
    ```

---

## How It Works

Upon executing `git commit`, the pre-commit hook:

1. Identifies DOCX files that are staged for commit.
2. Converts each DOCX file to a Markdown file using html formatting.
3. Adds the Markdown files to the commit automatically.

---

## Contributing

Feel free to open issues and pull requests. Your contributions are welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

For more information, please contact the maintainers.
