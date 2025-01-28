import sqlite3

# Path to your database
db_path = "C:\\Users\\russe\\dsnd-dashboard-project\\python_package\\employee_events\\employee_events.db"

def explore_database(db_path):
    """
    Explore the schema and data of the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # List all tables
        print("Tables in the database:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f" - {table[0]}")

        print("\nSchemas and Sample Data:")

        # Get schema and data for each table
        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")

            # Schema of the table
            print("Schema:")
            cursor.execute(f"PRAGMA table_info({table_name});")
            schema = cursor.fetchall()
            for column in schema:
                print(f" - {column[1]} ({column[2]})")

            # Sample data
            print("Sample Data:")
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print(" - No data in this table.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

# Call the function
if __name__ == "__main__":
    explore_database(db_path)
