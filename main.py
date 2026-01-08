import sqlite3
import pandas as pd

import sqlite3
import pandas as pd
import os

def run_analysis_suite(db_path, queries_folder):
    # 1. Connect once
    conn = sqlite3.connect(db_path)
    
    # 2. Get all .sql files from the folder
    query_files = [f for f in os.listdir(queries_folder) if f.endswith('.sql')]
    
    print(f"🚀 Running {len(query_files)} analyses...\n")

    for file_name in query_files:
        # Construct full path
        file_path = os.path.join(queries_folder, file_name)
        
        # Read the SQL
        with open(file_path, 'r') as f:
            query = f.read()
        
        # Run and Print
        print(f"📊 REPORT: {file_name.upper().replace('_', ' ')}")
        print("-" * 30)
        try:
            df = pd.read_sql(query, conn)
            print(df)
        except Exception as e:
            print(f"❌ Error running {file_name}: {e}")
        print("\n" + "="*50 + "\n")

    conn.close()

# Usage
if __name__ == "__main__":
    run_analysis_suite('agency_performance.db', 'queries')