import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def get_random_wine(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute('SELECT fixed_acidity, alcohol, quality FROM red_wine ORDER BY RANDOM() LIMIT 1')
        wine = cursor.fetchone()
        conn.close()
        return wine

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)