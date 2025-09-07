import sqlite3
import os
from datetime import datetime

DATABASE_PATH = 'saferide.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create hazards table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hazards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            description TEXT,
            distance INTEGER DEFAULT 0
        )
    ''')
    
    # Create alerts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hazard_id INTEGER,
            timestamp TEXT NOT NULL,
            message TEXT NOT NULL,
            FOREIGN KEY (hazard_id) REFERENCES hazards (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def seed_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert example hazards
    hazards = [
        ('blackspot', -1.2864, 36.8172, 'Accident prone area', 500),
        ('bump', -1.2921, 36.8219, 'Speed bump ahead', 200),
        ('school_zone', -1.2950, 36.8250, 'School zone - slow down', 300),
        ('sharp_bend', -1.2980, 36.8280, 'Sharp bend ahead', 400),
        ('traffic_congestion', -1.3010, 36.8310, 'Heavy traffic zone', 600),
    ]
    
    cursor.executemany('INSERT INTO hazards (type, lat, lng, description, distance) VALUES (?, ?, ?, ?, ?)', hazards)
    
    conn.commit()
    conn.close()

def get_nearby_hazards(lat, lng, radius=1000):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simple distance calculation (approximate)
    cursor.execute('''
        SELECT *, 
               (lat - ?) * (lat - ?) + (lng - ?) * (lng - ?) as distance_squared
        FROM hazards
        WHERE distance_squared < ? * ?
        ORDER BY distance_squared
    ''', (lat, lat, lng, lng, radius, radius))
    
    hazards = cursor.fetchall()
    conn.close()
    return hazards

def add_alert(hazard_id, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    timestamp = datetime.now().isoformat()
    cursor.execute('INSERT INTO alerts (hazard_id, timestamp, message) VALUES (?, ?, ?)', (hazard_id, timestamp, message))
    
    conn.commit()
    conn.close()

def get_recent_alerts(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM alerts ORDER BY timestamp DESC LIMIT ?', (limit,))
    alerts = cursor.fetchall()
    conn.close()
    return alerts

def get_all_hazards():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM hazards')
    hazards = cursor.fetchall()
    conn.close()
    return hazards

def add_hazard(type_, lat, lng, description, distance):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO hazards (type, lat, lng, description, distance) VALUES (?, ?, ?, ?, ?)', (type_, lat, lng, description, distance))
    
    conn.commit()
    conn.close()

def update_hazard(id, type_, lat, lng, description, distance):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('UPDATE hazards SET type = ?, lat = ?, lng = ?, description = ?, distance = ? WHERE id = ?', (type_, lat, lng, description, distance, id))
    
    conn.commit()
    conn.close()

def delete_hazard(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM hazards WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    seed_data()
    print("Database initialized and seeded.")