import socket
import os
import userDatabase as User
import user_groupDatabase as UG
import groupDatabase as Group
import threading

def Client(conn, clientaddr):
    data = conn.recv(4096).decode().split(',')
    data = [x.split('=') for x in data]
    if(data[0]=='CreatUser'):
        userid = len(User.view_user()) + 1
        username = data[1][1]
        password = data[2][1]
        User.insert_user(userId=userid, userName=username, password=password)
        conn.sendto('ToLogin'.encode(),clientaddr)
    elif(data[0] == 'AuthUser'):
        username = data[1][1]
        password = data[2][1]
        UDetails = User.search_user(userName=username, password=password)
        if len(UDetails) == 1:
            userid = UDetails[0][0]
            if len(UG.search_usergroup(userId=userid)) == 0:
                conn.sendto(('GroupAuthPage,'+username).encode(),clientaddr)
            else:
                usergroups = UG.user_view(userid)
                for i in range(len(usergroups)):
                    usergroups[i] = Group.search_group(groupId=usergroups[i])
                usergroups = [str(x) for x in usergroups]
                conn.sendto(('GroupPage,'+username+',' +(','.join(usergroups))).encode(),clientaddr)
        else:
            conn.sendto('ToLoginAuth'.encode(),clientaddr)
    elif(data[0] == 'AddGroup'):
        userid  = (User.search_user_id(userName= data[1][1]))[0]
        groupid = Group.check_insert_group(groupName=data[2][1])
        chathistory = UG.check(userid,groupid)
        conn.sendto('GotGroup,'+username+','+data[2][0]+ ',' + chathistory)
    elif(data[0] == 'ChatMessage'):
        userid  = (User.search_user_id(userName= data[1][1]))[0]
        groupid = Group.check_insert_group(groupName=data[2][1])
        message = data[1][1] + ': ' + data[3][1]
        UG.Update_chat_by_groupid(groupid,message)



        

if __name__ == '__main__':
    sock = socket.socket()
    User.connect_user()
    UG.connect_usergroup()
    Group.connect_group()
    # host = socket.gethostbyname(socket.gethostname())
    # port = 5792
    print(('192.168.0.105', 5792))
    sock.bind(('192.168.0.105', 5792))

    sock.listen(5)

    while True:
        conn, clientaddr = sock.accept()
        print("Connected to -> ", clientaddr)
        threading._start_new_thread(Client,(conn,clientaddr))