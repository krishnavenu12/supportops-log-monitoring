import sqlite3

DB_NAME = "logs.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                severity TEXT NOT NULL,
                service TEXT NOT NULL,
                message TEXT NOT NULL
            );
        """)
        conn.commit()

def fetch_logs():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT * FROM logs").fetchall()

def add_log(timestamp, severity, service, message):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO logs (timestamp, severity, service, message)
            VALUES (?, ?, ?, ?)
        """, (timestamp, severity, service, message))
        conn.commit()

def delete_log(log_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM logs WHERE id = ?", (log_id,))
        conn.commit()

def update_log(log_id, timestamp, severity, service, message):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            UPDATE logs
            SET timestamp = ?, severity = ?, service = ?, message = ?
            WHERE id = ?
        """, (timestamp, severity, service, message, log_id))
        conn.commit()
