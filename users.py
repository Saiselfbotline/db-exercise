import sqlite3


class User:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    def createTable(self):
        self.cursor.execute("""CREATE TABLE users (mid VARCHAR UNIQUE)""")
        self.db.commit()

    def list(self):
        # btw result in tuple
        self.cursor.execute("SELECT * FROM users")
        return [user[0] for user in self.cursor.fetchall()]

    def add(self, mid):
        try:
            self.cursor.execute("INSERT INTO users (mid) VALUES (?)", (mid,))
            self.db.commit()
            print(f"Success, add {mid} to user")
        except Exception:
            print(f"{mid}, already in users")

    def delete(self, mid):
        try:
            self.cursor.execute("DELETE FROM users WHERE mid=?", (mid,))
            self.db.commit()
            print(f"Success, delete {mid} from users")
        except Exception as e:
            print(f"{mid}, not in users")
