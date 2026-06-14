from log_parser import parse_logs
from database import create_database, insert_log

create_database()

logs = parse_logs("uploads/sample.log")

for log in logs:
    insert_log(
        log["timestamp"],
        log["level"],
        log["message"]
    )