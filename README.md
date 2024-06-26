# PyShiny E2E Testing with Playwright

<a href="https://www.appsilon.com/"><img src="images/appsilon_logo.png" width="200"></a>

This project demonstrates end-to-end (E2E) testing of a [PyShiny](https://shiny.posit.co/py/) application using [Playwright](https://playwright.dev/python/). It aims to provide a practical example of how to automate testing for a Python-based web app, covering UI interactions and verifying functionality.

![App Screenshot](images/app_screenshot.png)

## Features

- Demonstrates usage of Playwright with PyShiny.
- Shows how to test easily available UI components like radio buttons.
- And how to test components that require javascript to interact with, like sliders.
- Includes examples of parameterized tests.

## Getting Started

### Prerequisites

- Python 3.10+
- Poetry for dependency management

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Appsilon/pyshiny-e2e-playwright.git
cd pyshiny-e2e-playwright
```

2. **Install dependencies using Poetry:**

```bash
poetry install
poetry run playwright install
```

These commands will create a virtual environment and install all required dependencies.

### Running the Application

To start the PyShiny app:

```bash
poetry run shiny run app.py
```

Ensure the app is running at `http://localhost:8000` (or your configured port).

### Running Tests

To execute the E2E tests with Playwright:

```bash
poetry run pytest
```

Make sure your app is running before executing the tests as they require the app to be accessible.

## Contact

Appsilon | [appsilon.com](https://appsilon.com)
