from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Path to the database file
db_path = Path(__file__).parent.resolve() / "employee_events.db"

# MIXIN class — this is your rubric's "mixin class"
class QueryMixin:
    
    def pandas_query(self, sql_query):
        """Run a query, return a pandas DataFrame."""
        with connect(db_path) as conn:
            return pd.read_sql(sql_query, conn)

    def query(self, sql_query):
        """Run a query, return a list of tuples."""
        with connect(db_path) as conn:
            cursor = conn.cursor()
            result = cursor.execute(sql_query).fetchall()
            return result

# Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """
    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    return run_query