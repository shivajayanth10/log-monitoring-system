import re

def parse_logs(filepath):
    logs = []

    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)"

    with open(filepath, "r") as file:
        for line in file:
            match = re.match(pattern, line)

            if match:
                timestamp = match.group(1)
                level = match.group(2)
                message = match.group(3)

                logs.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })

    return logs