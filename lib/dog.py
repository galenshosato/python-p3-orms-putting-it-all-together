import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
        """

        CURSOR.execute(sql)
    
    def save(self):
        pass