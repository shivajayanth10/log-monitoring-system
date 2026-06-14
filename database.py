import sqlite3

def create_database():
    conn = sqlite3.connect("logs.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        level TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(timestamp, level, message):
    conn = sqlite3.connect("logs.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs(timestamp, level, message)
        VALUES(?,?,?)
        """,
        (timestamp, level, message)
    )

    conn.commit()
    conn.close()