# ShopTest-AI

## E-Commerce Test Automation Framework

A Python-based test automation framework built to validate e-commerce application functionality through UI automation and API testing.

The project demonstrates practical software testing skills, reusable automation architecture, test reporting, and continuous integration using GitHub Actions.

## Technology Stack

- **Language:** Python
- **UI Automation:** Playwright
- **Test Framework:** Pytest
- **API Testing:** Requests
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Pytest HTML Reports
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions

## Project Features

- Automated UI testing using Playwright.
- API testing using Python Requests.
- Page Object Model architecture.
- Reusable Pytest fixtures.
- Data-driven and parametrized testing.
- Positive and negative test scenarios.
- API response validation and response-time checks.
- Automated HTML test reports.
- Logging and failure screenshots.
- Continuous test execution using GitHub Actions.

## Applications Under Test

**UI Testing:** [SauceDemo](https://www.saucedemo.com/)

**API Testing:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Project Structure

```text
ShopTest-AI/
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test_data/
│   ├── login_data.py
│   └── api_data.py
│
├── tests/
│   ├── ui/
│   └── api/
│
├── utils/
│   ├── api_helpers.py
│   └── logger.py
│
├── reports/
├── logs/
├── docs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/dhruvi19work-pandas/ShopTest-AI.git
```

### 2. Navigate to the project

```bash
cd ShopTest-AI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright Chromium

```bash
playwright install chromium
```

### 7. Configure environment variables

Create a `.env` file using `.env.example` as a reference.

## Running Tests

**Run the complete test suite:**

```bash
python -m pytest -v
```

**Run UI tests:**

```bash
python -m pytest tests/ui/ -v
```

**Run API tests:**

```bash
python -m pytest tests/api/ -v
```

**Generate an HTML report:**

```bash
python -m pytest -v --html=reports/full_report.html --self-contained-html
```

## Test Execution Results

The framework has successfully executed **29 automated tests** in the latest full test run.

- Passed: 29
- Failed: 0

## Continuous Integration

GitHub Actions is configured to automatically execute the UI automation test suite on pushes and pull requests to the main branch.

## Project Goals

- Strengthen practical UI and API automation skills.
- Build reusable and maintainable test automation components.
- Apply real-world software testing practices.
- Understand test execution and reporting.
- Gain hands-on experience with CI/CD pipelines.

## Project Status

**Core automation framework implemented.**

Further improvements and advanced testing features may be added as the project evolves.