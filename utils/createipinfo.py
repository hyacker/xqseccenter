import os
import sys
import requests
import json
import geoip2.database
import datetime
import pprint
import pymongo

db_conn = pymongo.MongoClient("mongodb://localhost:27017/")
xqseccenter_db = db_conn.xqseccenter

def get_url_ip_info(at_ip):

    url = "http://ipinfo.io/"+at_ip+"/json"
    ipinfo = requests.get(url)
    dict_ipinfo = ipinfo.json()
    return dict_ipinfo


if __name__ == '__main__':

    try:
        for item in xqseccenter_db.hpfeed.find():
            res = get_url_ip_info(item["payload"]["remote"][0])
            xqseccenter_db.ipaddrinfo.insert(dict(location=res['loc'],city=res['city'],country=res['country'],region=res['region'],hostname=res['hostname'],ipaddr=res['ip']))
            if not item["payload"]["public_ip"]:
                continue
            else:
                res_des = get_url_ip_info(item["payload"]["public_ip"])
                xqseccenter_db.ipaddrinfo.insert(dict(location=res_des['loc'],city=res_des['city'],country=res_des['country'],region=res_des['region'],hostname=res_des['hostname'],ipaddr=res_des['ip']))
    except (KeyError,ValueError):
        pass
