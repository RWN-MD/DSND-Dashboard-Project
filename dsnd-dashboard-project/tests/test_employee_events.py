import pytest
from pathlib import Path
from sqlite3 import connect

# Using pathlib, create a project_root variable set to the absolute path for the root of this project
project_root = Path(__file__).resolve().parent.parent

# Apply the pytest fixture decorator to a `db_path` function
@pytest.fixture
def db_path():
    """
    Fixture that returns the absolute path to the employee_events.db file.
    """
    # Using the `project_root` variable, return a pathlib object for the `employee_events.db` file
    return project_root / "python_package" / "employee_events" / "employee_events.db"

# Define a function called `test_db_exists`
def test_db_exists(db_path):
    """
    Test that the SQLite database file exists.
    """
    # Using the pathlib `.is_file` method, assert that the SQLite database file exists
    # at the location passed to the test_db_exists function
    assert db_path.is_file(), f"Database file not found at {db_path}"

@pytest.fixture
def db_conn(db_path):
    """
    Fixture that provides a database connection.
    """
    # Use sqlite3.connect to establish a connection to the database
    return connect(db_path)

@pytest.fixture
def table_names(db_conn):
    """
    Fixture that retrieves a list of table names from the database.
    """
    # Execute a query to retrieve table names and fetch the results
    name_tuples = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    # Extract table names from the query results
    return [x[0] for x in name_tuples]

# Define a test function called `test_employee_table_exists`
def test_employee_table_exists(table_names):
    """
    Test that the 'employee' table exists in the database.
    """
    # Assert that the string 'employee' is in the table_names list
    assert 'employee' in table_names, "'employee' table does not exist in the database"

# Define a test function called `test_team_table_exists`
def test_team_table_exists(table_names):
    """
    Test that the 'team' table exists in the database.
    """
    # Assert that the string 'team' is in the table_names list
    assert 'team' in table_names, "'team' table does not exist in the database"

# Define a test function called `test_employee_events_table_exists`
def test_employee_events_table_exists(table_names):
    """
    Test that the 'employee_events' table exists in the database.
    """
    # Assert that the string 'employee_events' is in the table_names list
    assert 'employee_events' in table_names, "'employee_events' table does not exist in the database"
