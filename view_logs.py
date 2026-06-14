import sqlite3

PER_PAGE = 5


def get_all_logs(search="", page=1):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    offset = (page - 1) * PER_PAGE

    if search:
        cursor.execute(
            """
            SELECT timestamp, level, message
            FROM logs
            WHERE level LIKE ? OR message LIKE ?
            LIMIT ? OFFSET ?
            """,
            (
                f"%{search}%",
                f"%{search}%",
                PER_PAGE,
                offset
            )
        )
    else:
        cursor.execute(
            """
            SELECT timestamp, level, message
            FROM logs
            LIMIT ? OFFSET ?
            """,
            (
                PER_PAGE,
                offset
            )
        )

    rows = cursor.fetchall()

    conn.close()

    return rows