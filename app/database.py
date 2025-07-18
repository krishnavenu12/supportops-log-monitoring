# app/database.py
import sqlite3

DB_FILE = "logs.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            severity TEXT,
            service TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(log):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO logs (timestamp, severity, service, message)
        VALUES (?, ?, ?, ?)
    ''', (log["timestamp"], log["severity"], log["service"], log["message"]))
    conn.commit()
    conn.close()

def fetch_all_logs():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT timestamp, severity, service, message FROM logs ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    return [
        {"timestamp": row[0], "severity": row[1], "serv
