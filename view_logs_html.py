import sqlite3

def get_all_logs(search=""):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    if search:
        cursor.execute(
            """
            SELECT timestamp, level, message
            FROM logs
            WHERE level LIKE ? OR message LIKE ?
            """,
            (f"%{search}%", f"%{search}%")
        )

    else:
        cursor.execute(
            "SELECT timestamp, level, message FROM logs"
        )

    rows = cursor.fetchall()

    conn.close()

    return rows