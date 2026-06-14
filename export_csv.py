import sqlite3
import csv

def export_logs():

    conn = sqlite3.connect("logs.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT timestamp, level, message
        FROM logs
        """
    )

    rows = cursor.fetchall()

    conn.close()

    with open("logs_export.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Timestamp", "Level", "Message"]
        )

        writer.writerows(rows)