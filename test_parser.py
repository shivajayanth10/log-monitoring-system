from log_parser import parse_logs

logs = parse_logs("uploads/sample.log")

for log in logs:
    print(log)