import subprocess,re,os
from time import strftime, localtime

from line import LineClient, LineGroup, LineContact, LineAPI

try:
    client = LineClient('fakhrighost22@gmail.com', 'adianeh123')
    print client.authToken
except:
    print "Login Failed"


while True:
    op_list = []
    timeSeen = []
    appendSeen = []
    dataResult = []
    #setpoint
    userList = []
    timelist =[]
    contacts = []
    recheckData = []
    #cancelAll
    myListMember = []
    
    #memberKick
    memberKick = []
    memberNameKick = []
    #getFriend list @
    listFriend = []
    myfriend = ['udb418f8ee4a2fdb5897e0b5267c3050f']

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]

        if message.text is not None:
            msg = message.text
            
            if 'setpoint' in msg :
                    proc=subprocess.Popen("echo '' > Output.txt", shell=True, stdout=subprocess.PIPE, )
                    receiver.sendMessage('Exploit Was Fuck3e$!')          
            # setpoint
            if 'check' == msg.lower():
                with open('Output.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        if arg[1] == receiver.id :
                            userList.append(arg[0])
                            timelist.append(arg[2])
                    uL = list(set(userList))
                    # print uL
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(strftime("%H:%M:%S", localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass

                    contactId = client._getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + '['+timeSeen[v]+']')
                        pass
                    # # print len(recheckData)
                    tukang = "whos fucked by 3xplo1d\n~"
                    grp = '\n~ '.join(str(f) for f in dataResult)
                    receiver.sendMessage("%s %s" % (tukang, grp))

            # contoh chat            
            if 'vinn -version' in msg.lower():
                receiver.sendMessage('v0.1b')

            if 'vinn -halo' in msg.lower():
                receiver.sendMessage('halo juga fucker')

            if 'test' in msg.lower():
                receiver.sendMessage('refresh...')

            if 'vinn -myid' in msg.lower():
                receiver.sendMessage(sender.id)

            if 'vinn -help' in msg.lower():
                receiver.sendMessage('COMMAND LIST!!\n\n\n[]setpoint\n[]check\n\n\nUse vinn first and then\n-version\n-halo\n-myid\n-bye\n\n\nExamples: vinn -help')
            
            if 'vinn -bye' == msg:
                if sender.id in myfriend:
                   receiver.sendMessage('Bye afuk3er')
                   client._leaveGroup(receiver.id)

            user_whitelist=['udb418f8ee4a2fdb5897e0b5267c3050f']
            if "kill " in message.text:
                if sender.id in myfriend:
                    group = client.getContactOrRoomOrGroupById(receiver.id)
                    if group is not None:
                             kick_name = message.text.replace('kill ','')
                             for member in group.members:
                                 if member.id not in user_whitelist and member.id != sender.id and kick_name in member.name:
                                     print "Berhasi kick dari %s => %s (%s)" % (group.name, member.name, member.id)
                                     try:
                                         client._kickoutFromGroup(receiver.id, [member.id])
                                     except Exception, e:
                                         print "ERROR : " + str(e)
                    receiver.sendMessage('fucker was fucked!')

            if 'cancel' in msg:
                if sender.id in myfriend:
                     thisgroup = client._getGroups([receiver.id])
                     totalInvitor = thisgroup[0].invitee
                     if totalInvitor is not None:
                        for xx in range(len(totalInvitor)):
                            myListMember.append(totalInvitor[xx].mid)
                            pass
                     client._cancelGroupInvitation(receiver.id,myListMember)
                     pass
                     receiver.sendMessage('Was cancelled ')
           


            if msg == 'go':
                if sender.id in myfriend:
                      receiver.sendMessage("Oke :D")
                      idgroup = receiver.id
                      thisgroup = client._getGroups([idgroup])
                      if len(thisgroup) > 0:
                          totalMember = thisgroup[0].members
                          for x in range(len(totalMember)):
                              if totalMember[x].mid != sender.id :
                                  client._kickoutFromGroup(0,receiver.id,[totalMember[x].mid])
                              pass

             #Auto Join
            idgroupa = client._getGroupIdsInvited()
            if client._getGroupIdsInvited():
                client._acceptGroupInvitation(idgroupa[0])
            else:
               print 'kosong'

