# CS 302 Tech Stack Survey - Django Hello World

This repository contains a simple "Hello World" application built with **Python** and **Django**, styled with **Bootstrap 5**. It was created to demonstrate a specific tech stack for the Module 03.02 assignment.

## Tech Stack
* **Backend Language:** Python 3
* **Framework:** Django 5.0
* **Templating:** Django Template Language (DTL)
* **UI Framework:** Bootstrap 5 (via CDN)
* **Testing:** Django `SimpleTestCase`

## How to Run (GitHub Codespaces)

1.  **Install Dependencies:**
    Open the terminal and run:
    ```bash
    pip install django
    ```

2.  **Start the Server:**
    Run the following command to start the development server on port 8000:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    *When the notification appears in the bottom right corner, click **"Open in Browser"** to view the app.*

3.  **Run Tests:**
    To verify the application with the automated test suite:
    ```bash
    python manage.py test
    ```

## Project Structure
* **`techstack/`**: Main project configuration (`settings.py`, `urls.py`).
* **`hello/`**: The application logic.
    * `views.py`: Handles the request and passes context data (Controller).
    * `templates/hello/index.html`: The HTML file styled with Bootstrap (View).
    * `tests.py`: Contains the unit tests to verify the route and content.
