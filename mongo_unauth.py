# coding=utf-8
# mongodb unanth

import pymongo,sys
import json


banner = '''

  __  __                           _    _                   _   _     
 |  \/  |                         | |  | |                 | | | |    
 | \  / | ___  _ __   __ _  ___   | |  | |_ __   __ _ _   _| |_| |__  
 | |\/| |/ _ \| '_ \ / _` |/ _ \  | |  | | '_ \ / _` | | | | __| '_ \ 
 | |  | | (_) | | | | (_| | (_) | | |__| | | | | (_| | |_| | |_| | | |
 |_|  |_|\___/|_| |_|\__, |\___/   \____/|_| |_|\__,_|\__,_|\__|_| |_|
                      __/ |                                           
                     |___/                                            
                    mongo 数据库未授权批量检测
                      
                       python by jas502n
'''

print banner

def database_mongo(ip):
    try:
        port = 27017
        client = pymongo.MongoClient(ip , port)
        dbs = client.database_names()
        for db in dbs:
            mydb = client[db]
            cols = mydb.collection_names()
            for col in cols:
                book = mydb[col]
                print '___________________________________________________________________________________________________\n'
                info ='DB:' + db + '----'+'Collections:' + col
                if len(db) != 0 or len(col) != 0:
                    print "[+] Successful Mongodb Unauthorized Exit!  %s:%s" % (ip,str(port))
                    print
                    print '>>>>>' 
                    print info

                cont = str(book.find_one())
                print cont.decode('unicode_escape')
                print 'Number:'+str(book.find().count())
                client.close()
                

    except Exception as e:
        print
        # print "[+] %s No Mongodb Unauthorized Exit !" % ip



if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("\n[+] Usage: python %s ip.txt\n" % sys.argv[0]) 
    else:
        filename = sys.argv[1]
        file = open("%s"% filename).readlines()
        for i in file:
            ip = i.split('\n')[0]
            # print ip
            database_mongo(ip) 

