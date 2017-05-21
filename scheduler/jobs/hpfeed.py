#coding=UTF-8
from datetime import datetime
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
import config
import pymongo


db_conn = pymongo.MongoClient("mongodb://localhost:27017/")
xqseccenter_db = db_conn.xqseccenter

#db_conn = pymongo.MongoClient(config['testing'].MONGODB_DATABASE_URI)
#xqseccenter_db = getattr(db_conn,config['testing'].MONGODB_DBNAME)

params_data = {'api_key':config.REQ_API_KEY,'limit':'1000'}

def task_run():
    res = requests.get(url=config.FEED_URL,params=params_data)
    for dic in res.json()['data']:
        hpfeed_insert(dic)

def hpfeed_insert(HpFeed):
    xqseccenter_db.hpfeedtest.insert(dict(ident=HpFeed['ident'],timestamp=HpFeed['timestamp'],payload=HpFeed['payload'],channel=HpFeed['channel']))
