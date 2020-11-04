import sqlite3

# version check
# print(sqlite3.version)

# SQLite DB 연결
conn = sqlite3.connect("database/test.db")

print("[START] 기본 쿼리 실행")
# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL 쿼리 실행
cur.execute("SELECT * FROM customer")

# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
    print(row)

# Connection 닫기
conn.close()

print()
print("[START] ? placeholder 쿼리 실행")
conn = sqlite3.connect("database/test.db")

cur = conn.cursor()
sql = "SELECT * FROM customer WHERE category=? and region=?"
cur.execute(sql, (1, 'SEA'))
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()

print()
print("[START] Named placeholder 쿼리 실행")
conn = sqlite3.connect("database/test.db")

cur = conn.cursor()
sql = "SELECT * FROM customer WHERE id= :Id"
cur.execute(sql, {"Id": 1})
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
