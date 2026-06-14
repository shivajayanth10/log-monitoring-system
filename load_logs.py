from log_parser import parse_logs
from database import create_database, insert_log

# Create database and table
create_database()

# Read logs from sample.log
logs = parse_logs("sample.log")

# Insert each log into database
for log in logs:
    insert_log(
        log["timestamp"],
        log["level"],
        log["message"]
    )

print("Logs loaded successfully!")