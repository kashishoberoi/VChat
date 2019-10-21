import sqlite3 as lite

def connect_usergroup():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usergroupchat (userId INTEGER,groupId INTEGER, chatHistory text, PRIMARY KEY(userId,groupId))")
    conn.commit()
    conn.close()

def insert_usergroup(userId, groupId):
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO usergroupchat VALUES (?,?,?)",(userId, groupId, ""))
    conn.commit()
    conn.close()

def check(userId, grouptId):
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM usergroupchat WHERE groupId=? AND userId=?",(grouptId,userId))
    rows=cur.fetchall()
    if rows == []:
        insert_usergroup(userId,grouptId)
        conn.close()
        return ""
    else:
        cur.execute("SELECT chatHistory FROM usergroupchat WHERE groupId=? AND userId=?",(grouptId,userId))
        rows = cur.fetchall()
        conn.close()
        return (rows)[0]

def view_usergroup():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM usergroupchat")
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def Users_by_Groupid(groupId):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT userId FROM usergroupchat WHERE groupId=?", (str(groupId)))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return [x[0] for x in rows]

def user_view(userId):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT groupid FROM usergroupchat WHERE userId=?", (userId))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def search_usergroup(userId=-1,groupId=-1):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM usergroupchat WHERE userId=? OR groupId=?", (userId,groupId))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def delete_usergroup(userId,groupId):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM usergroupchat WHERE userId=? AND groupId=?",(userId,groupId))
    conn.commit()
    conn.close()
def getchathistory(userId,groupId):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT chatHistory FROM usergroupchat WHERE groupId=? AND userId=?",(groupId,userId))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows[0][0]

def update_usergroup(groupId,message):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    users = Users_by_Groupid(groupId)
    for userId in users:
        chathistory = getchathistory(userId,groupId) + ":;:;:"  + message
        cur.execute("UPDATE usergroupchat SET chatHistory=? WHERE groupId=? AND userId=?",(chathistory,groupId,userId))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_usergroup()
    insert_usergroup(113,512,"Test Group")
    view_usergroup()
    update_usergroup(113,512,"Renamed")
    view_usergroup()
    search_usergroup(113,512)
    view_usergroup()
    delete_usergroup(113,512)
    view_usergroup()