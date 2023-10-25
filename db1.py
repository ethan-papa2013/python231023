# db1.py

import sqlite3

#연결객체(일단은 메모리에 저장)
con = sqlite3.connect(":memory:")
#커서 객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("""CREATE TABLE IF not exists PhoneBook
    (id integer primary key autoincrement, name text, phoneNum text);
    """)

#1건 입력
cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES ('전우치','010-222');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("INSERT INTO PhoneBook (name, phoneNum) VALUES (?, ?);", (name, phoneNumber))

#다중으로 행을 입력
datalist = (("박문수","010-333"), ("김길동","010-567"))
cur.executemany("INSERT INTO PhoneBook (name, phoneNum) VALUES (?, ?);", (datalist))

#검색
cur.execute("SELECT * from PhoneBook;")
# for row in cur:
#     print(row)

print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())
cur.execute("SELECT * from PhoneBook;")
print("---fetchall()---")
print(cur.fetchall())

