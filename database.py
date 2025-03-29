import sqlite3

class Database:
    def __init__(self, db_name="quiz.db"):
        self.db_name = db_name

    def create_connection(self):
        """Kreira konekciju sa bazom podataka."""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Greška pri povezivanju sa bazom: {e}")
            return None

    def create_database(self):
        """Kreira tabelu za pitanja ako već ne postoji."""
        conn = self.create_connection()
        if conn is None:
            return  
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question_text TEXT NOT NULL,
                    option_1 TEXT NOT NULL,
                    option_2 TEXT NOT NULL,
                    option_3 TEXT NOT NULL,
                    option_4 TEXT NOT NULL,
                    correct_option INTEGER NOT NULL,
                    chapter TEXT NOT NULL,
                    subchapter TEXT
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Greška pri kreiranju tabele: {e}")
        finally:
            conn.close()

    def add_question(self, question_data):
        """Dodaje novo pitanje u bazu."""
        conn = self.create_connection()
        if conn is None:
            return  

        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO questions (question_text, option_1, option_2, option_3, option_4, correct_option, chapter, subchapter)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', question_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Greška pri dodavanju pitanja: {e}")
        finally:
            conn.close()
