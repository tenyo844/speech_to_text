import sqlite3
from flask import Flask

app = Flask(__name__)


# データベースの初期化
def init_db():
  try:
    conn = sqlite3.connect('data/database.db')
    return conn.cursor()
  except sqlite3.Error as e:
    print("Database connection error:", e)
    return None

# ユーザー登録
def register_user(email, password):
  try:
    c = init_db()

    if c:
      sql = 'INSERT INTO USERS (email,password) VALUES (?,?)'
      c.execute(sql, (email, password))
      c.connection.commit()
      c.connection.close()
      return True, None
    else:
      return False, "Database connection error"
  except sqlite3.Error as e:
    return False, "Database error: " + str(e)