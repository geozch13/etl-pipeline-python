"""
Load step of the ETL pipeline.

Creates SQLite table (if not exists) and inserts data
incrementally while avoiding duplicates.
"""

import sqlite3
from datetime import datetime
from extract import get_data
from config import DB_NAME

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# create table if it does not exist
c.execute(
    '''
        CREATE TABLE IF NOT EXISTS output
        (userId INT,
        id INT PRIMARY KEY, 
        title VARCHAR(50),
        created_at TEXT
        )
    '''
)

# get last inserted id to support incremental loading
last_id = c.execute("SELECT MAX(id) FROM output").fetchone()[0]
if last_id is None:
    last_id = 0
    
now = datetime.now()

# fetch next batch starting from last_id
data = get_data(last_id)

if not data:
    print("No data to insert. Exiting")
    exit()
    
print("Inserting into DB...")

try:
    for item in data:
        # use INSERT OR IGNORE to avoid duplicate primary key errors
        c.execute(
            "INSERT OR IGNORE INTO output(userId, id, title, created_at) VALUES (?, ?, ?, ?)",
            (item['userId'], item['id'], item['title'], now.isoformat())
        )

    conn.commit()
    print("Insert complete")
    
except Exception as e:
    print("DB error:", e)

finally:
    conn.close()