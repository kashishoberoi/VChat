import sqlite3 as lite

def connect_user():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (userId INTEGER, userName text, password text,PRIMARY KEY(userId,userName))")
    conn.commit()
    conn.close()

def insert_user(userId,userName,password):
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?)",(userId,userName,password))
    conn.commit()
    conn.close()
    view_user()

def view_user():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def search_user(userName="",password=""):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE userName=? AND password=?", (userName,password))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def search_user_id(userName=""):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT  userId FROM users WHERE userName=?", (userName))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

if __name__ == "__main__":
    connect_user()
    # insert_user(113,"Kashish","Oberoi")
    # search_user(113)
    # view_user()
    # # view()
    view_user()