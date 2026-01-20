"""
SQL Project: Data Job Market Analysis

Author: Klauberta Morina
Description:
This script documents and explains the SQL queries used
to analyze data-related job postings, salaries, and skills.

The SQL files are located in the queries/ folder.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
QUERIES_DIR = PROJECT_ROOT / "queries"


def list_sql_files():
    """List all SQL analysis files in the project."""
    if not QUERIES_DIR.exists():
        print("❌ Queries directory not found.")
        return

    sql_files = sorted(QUERIES_DIR.glob("*.sql"))

    print("📊 SQL Analysis Files:\n")
    for file in sql_files:
        print(f"- {file.name}")


def describe_analysis():
    """High-level description of the analysis steps."""
    print("\n🔍 Analysis Overview:\n")
    print("1. Identify top-paying data jobs")
    print("2. Analyze skills required for top-paying roles")
    print("3. Determine most in-demand technical skills")
    print("4. Compare salary vs skill demand")
    print("5. Identify optimal skills for career growth")


if __name__ == "__main__":
    print("🚀 SQL Project: Data Job Analysis\n")
    describe_analysis()
    list_sql_files()
