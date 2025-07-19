import sqlite3

class Tables:
    def __init__(self):
        self.__basename = 'customers.db'
        self.__prepare(self.__basename)
        
    def __prepare(self, dbname):
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS person(ip TEXT, visittime TEXT, user_agent TEXT )""")
        conn.commit()
        conn.close()
        
    def add_info(self, ip, times, au):
        conn = sqlite3.connect(self.__basename)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO person (ip, visittime, user_agent) VALUES (?, ?, ?)', (ip, times, au))
        conn.commit()
        conn.close
            
