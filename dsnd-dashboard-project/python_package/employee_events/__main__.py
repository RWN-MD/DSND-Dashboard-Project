import sys
from .query_base import QueryBase
from .employee import Employee
from .team import Team

def display_help():
    print("Usage: python -m employee_events [command] [options]")
    print("Commands:")
    print("  query_base: Test QueryBase functionality.")
    print("  employee: Test Employee functionality.")
    print("  team: Test Team functionality.")

def main():
    if len(sys.argv) < 2:
        display_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "query_base":
        qb = QueryBase()
        print("Testing QueryBase:")
        print(qb.names())
    elif command == "employee":
        employee = Employee()
        print("Testing Employee:")
        print(employee.names())
    elif command == "team":
        team = Team()
        print("Testing Team:")
        print(team.names())
    else:
        print(f"Unknown command: {command}")
        display_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
