from employee_events.sql_execution import QueryMixin, query
import pandas as pd

# QueryBase inherits from QueryMixin (the mixin)
class QueryBase(QueryMixin):

    # Subclasses set this to their table name
    name = ""

    def names(self):
        return []

    def event_counts(self, id):
        # QUERY 1 — sum positive/negative events per date
        sql = f"""
            SELECT event_date AS date,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date
        """
        return self.pandas_query(sql)

    def notes(self, id):
        # QUERY 2 — return notes for this employee or team
        sql = f"""
            SELECT note_date, note
            FROM notes
            JOIN {self.name}
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        return self.pandas_query(sql)