# Data Science Dashboard Project

This project is a data science dashboard built using Python, FastAPI, and SQLite. It allows users to view and analyze data for employees and teams, featuring dynamic visualizations and tables.

## 1. Project Overview

The dashboard is designed to meet the following criteria:
- **Python Package**: A well-structured Python package connects to a SQLite database.
- **Object-Oriented Programming**: Classes and inheritance are used to ensure modularity.
- **Dynamic Dashboard**: Displays visualizations and tables based on user selections.
- **GitHub Repository**: Includes organized code, automated testing, and documentation.

---

## 2. Install the Requirements

To set up the project environment, install the required Python dependencies using the following command:

```bash 
pip install -r requirements.txt
```

---

## 3. Running the Project

Run the project by executing the `dashboard.py` file located in the `report` directory:

```bash
python report/dashboard.py
```

---

## 4. Accessing the Dashboard

After starting the project, open your browser and navigate to:

```bash
http://127.0.0.1:8000
```

### Features on the Dashboard:

- **Landing Page**: 
    - Select between "Employee" and "Team" dashboards.
    - View a dropdown of entities to choose from.
- **Dynamic Reports**: 
    - Visualizations:
        - Line Chart: Cumulative events over time.
        - Bar Chart: Recruitment risk scores.
    - Notes Table:
        - Displays additional notes tied to the selected entity.

---

## 5. Testing the Project

To ensure functionality, run the project's test suite using the following command:

```bash
pytest
```

### Tests Overview:

- **Database Tests**:
    - Verify that `employee_events.db` exists.
    - Ensure required tables (`employee`, `team`, `employee_events`) are present.
- **Functional Tests**:
    - Validate visualizations and table rendering.
    - Check routing and redirection for reports.

---

## 6. Features of the Project

### Python Package
- Located in `python-package/employee_events`.
- Connects to the `employee_events.db` SQLite database.
- Executes SQL queries to dynamically fetch data.

### Object-Oriented Programming
- Uses inheritance to reduce redundancy.
- Includes mixin classes for shared functionality.
- Maintains modular and extensible code.

### Dashboard Development
- Built with **FastAPI**:
    - Dynamic routing for Employee and Team reports.
    - Handles forms for filtering and data selection.
- Visualizations:
    - Line and Bar Charts rendered with Matplotlib.
- Notes Table:
    - Displays notes relevant to the selected entity.

### GitHub Repository
- Clean and organized structure.
- Automated testing using GitHub Actions.
- Includes all necessary files while excluding unnecessary ones.

---

## 7. Directory Structure

The project is organized as follows:


