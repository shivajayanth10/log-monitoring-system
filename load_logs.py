from log_parser import parse_logs
from database import create_database, insert_log

def load_logs_from_file(filename):
    # Create database and table
    create_database()

    # Read logs from file
    logs = parse_logs(filename)

    # Insert each log into database
    for log in logs:
        insert_log(
            log["timestamp"],
            log["level"],
            log["message"]
        )

    print("Logs loaded successfully!")