"""
Pipeline entry point.

Allows optional batch size via CLI argument
and triggers the ETL process.
"""

import sys, os

# allow overriding batch size via CLI argument
if len(sys.argv) > 1:
    batch_size = int(sys.argv[1])
    os.environ["BATCH_SIZE"] = str(batch_size)
    print(f"Batch size: {batch_size}")

# execute the load step (which triggers extract as well)
os.system("python load_db.py")