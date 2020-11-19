import sqlite3

conn = sqlite3.connect("../../database/test.db")
# Auto commit 사용시
# conn = sqlite3.connect("database/test.db", isolation_level=None)

cur = conn.cursor()
sql = "INSERT INTO customer(name, category, region) VALUES (?, ?, ?)"
cur.execute(sql, ("홍길동", 1, "서울"))
conn.commit()

conn.close()
