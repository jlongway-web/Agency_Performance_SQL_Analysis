import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create/Connect to a local demo database
conn = sqlite3.connect('agency_performance.db')

# 1. Mock Agencies Table
agencies_data = pd.DataFrame({
    'agency_id': [1, 2, 3, 4],
    'agency': ['NYPD', 'FDNY', 'DOT', 'DSNY'],
    'agency_name': ['Police Department', 'Fire Department', 'Dept of Transportation', 'Dept of Sanitation']
})
agencies_data.to_sql('agencies', conn, if_exists='replace', index=False)

# 2. Mock Service Requests (generating 50 rows of fake history)
np.random.seed(42)
start_date = datetime(2023, 1, 1)
rows = []
for i in range(50):
    created = start_date + timedelta(days=np.random.randint(0, 365))
    # Closed date is 1-10 days after created
    closed = created + timedelta(days=np.random.randint(1, 11))
    rows.append({
        'agency_id': np.random.choice([1, 2, 3, 4]),
        'created_date': created.strftime('%Y-%m-%d'),
        'closed_date': closed.strftime('%Y-%m-%d'),
        'status': 'Closed'
    })

service_requests = pd.DataFrame(rows)
service_requests.to_sql('service_requests', conn, if_exists='replace', index=False)

print("Mock database 'agency_performance.db' created successfully!")