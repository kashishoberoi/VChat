import sqlite3 as lite

def connect_group():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS groups (groupId INTEGER PRIMARY KEY, groupName text)")
    conn.commit()
    conn.close()

def insert_group(groupId,groupName):
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO groups VALUES (?,?)",(groupId,groupName))
    conn.commit()
    conn.close()
def check_insert_group(groupName):
    if search_group(groupName=groupName) == []:
        groupid = len(view_group())+1
        insert_group(groupid,groupName)
        return groupid
    else:
        return(search_groupid(groupName=groupName)[0])

def view_group():
    conn=lite.connect("groupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM groups")
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def search_group(groupId=-1,groupName=""):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT groupName FROM groups WHERE groupId=? OR groupName=?", (groupId,groupName))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def search_groupid(groupId=-1,groupName=""):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("SELECT groupId FROM groups WHERE groupId=? OR groupName=?", (groupId,groupName))
    rows=cur.fetchall()
    print(rows)
    conn.close()
    return rows

def delete_group(groupId):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM groups WHERE groupId=?",(groupId))
    conn.commit()
    conn.close()

def update_group(groupId,groupName):
    conn=lite.connect("GroupChat.db")
    cur=conn.cursor()
    cur.execute("UPDATE groups SET groupName=? WHERE groupId=?",(groupName,groupId))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # connect_group()
    # insert_group(113,"Test Group")
    # view_group()
    # update_group(113,"Renamed")
    # view_group()
    # search_group(113)
    # view_group()
    # delete_group(113)
    view_group()