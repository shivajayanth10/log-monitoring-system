import sqlite3

def get_statistics():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total_logs = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE level='INFO'")
    info_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE level='WARNING'")
    warning_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE level='ERROR'")
    error_count = cursor.fetchone()[0]

    conn.close()

    return {
        "total_logs": total_logs,
        "info_count": info_count,
        "warning_count": warning_count,
        "error_count": error_count
    }