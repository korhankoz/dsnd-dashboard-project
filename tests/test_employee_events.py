import pytest
from employee_events import Employee, Team

def test_employee_names_returns_list():
    e = Employee()
    result = e.names()
    assert isinstance(result, list)
    assert len(result) > 0

def test_employee_event_counts_returns_dataframe():
    import pandas as pd
    e = Employee()
    first_id = e.names()[0][1]
    df = e.event_counts(first_id)
    assert isinstance(df, pd.DataFrame)

def test_team_names_returns_list():
    t = Team()
    result = t.names()
    assert isinstance(result, list)
    assert len(result) > 0

def test_team_event_counts_returns_dataframe():
    import pandas as pd
    t = Team()
    first_id = t.names()[0][1]
    df = t.event_counts(first_id)
    assert isinstance(df, pd.DataFrame)