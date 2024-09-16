# IDS706 Mini Project
![CICD Status](https://github.com/YitaoS/ids706_individual_project1/actions/workflows/cd.yml/badge.svg)
![Install](https://github.com/YitaoS/ids706_individual_project1/actions/workflows/install.yml/badge.svg)
![Format](https://github.com/YitaoS/ids706_individual_project1/actions/workflows/format.yml/badge.svg)
![Lint](https://github.com/YitaoS/ids706_individual_project1/actions/workflows/lint.yml/badge.svg)
![Test](https://github.com/YitaoS/ids706_individual_project1/actions/workflows/test.yml/badge.svg)

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (if using DevContainer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YitaoS/ids706_mini_project2.git
   cd ids706_mini_project2
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

   This will upgrade `pip` and install the necessary dependencies for development.

3. **Optional: Build the development environment using DevContainer**:
   - Open the project in Visual Studio Code.
   - Run **Reopen in Container** from the Command Palette (`Ctrl + Shift + P` or `Cmd + Shift + P`).

### Usage

- **Run the main script**:
  ```bash
  make run
  ```

- **Run tests**:
  ```bash
  make test
  ```

- **Format the code** using `black`:
  ```bash
  make format
  ```

- **Lint the code** using `flake8`:
  ```bash
  make lint
  ```

- **Deploy reports and images**:
  ```bash
  make deploy
  ```

### Additional Commands

- **Check code formatting** (without applying changes):
  ```bash
  make check-format
  ```

- **Clean up `.pyc` files and `__pycache__` directories**:
  ```bash
  make clean
  ```

- **Run the full CI process (linting, testing, and formatting check)**:
  ```bash
  make ci
  ```

### CI/CD Status
Continuous Integration (CI) checks are automatically run using GitHub Actions. You can view the current status by looking at the badge at the top of this file.

### Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Ensure your changes pass the linting and test suites before submission.
