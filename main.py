import sqlite3
import pandas as pd

# Create a database in memory (it disappears when you close Python)
conn = sqlite3.connect(':memory:')

# Create a tiny mock table
mock_data = pd.DataFrame({
    'agency_id': [1, 1, 2],
    'agency': ['NYPD', 'NYPD', 'FDNY'],
    'agency_name': ['Police', 'Police', 'Fire'],
    'created_date': ['2023-01-01', '2023-01-15', '2023-01-10'],
    'closed_date': ['2023-01-02', '2023-01-18', '2023-01-11'],
    'status': ['Closed', 'Closed', 'Closed']
})

mock_data.to_sql('service_requests', conn, index=False)