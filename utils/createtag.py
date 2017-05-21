import pymongo
import sys
import os
from bson import ObjectId, son
import datetime
import string

sys.path.append(os.path.split(os.path.realpath(__file__))[0]+"/../../")
#from config import config

db_conn = pymongo.MongoClient("mongodb://localhost:27017/")
xqseccenter_db = db_conn.xqseccenter

def createtag():
    try:
        with open('../doc/destination_iptag.txt','r') as fd:
            for line in fd:
                if not line or line == '\n':
                    continue
                xqseccenter_db.desipinfo.insert(dict(ipaddr=string.split(line,sep=None, maxsplit=-1)[0],tag=string.split(line,sep=None, maxsplit=-1)[1]))
    except IndexError:
        pass
def create_des_port():
    try:
        with open('../doc/des_protocol_to_port','r') as fd:
            for line in fd:
                if not line or line == '\n':
                    continue
                xqseccenter_db.protoport.insert(dict(port=string.split(line,sep=":", maxsplit=-1)[0],protocol=string.split(line,sep=":", maxsplit=-1)[1],tcpip=string.split(line,sep=":", maxsplit=-1)[2][:-1]))
    except IndexError:
        pass



if __name__ == '__main__':
#    createtag()
    create_des_port()
