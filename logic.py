import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE music (
                         music_id INTIGER PRIMARY KEY,
                         genre_id INTIGER 
                         )''')
            conn.execute('''CREATE TABLE genre (
                         genre_id INTIGER PRIMARY KEY,
                         music_id INTIGER,
                         name TEXT
                        )''')

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)  
    manager.create_tables()      