import pymongo
import sys
import os
from bson import ObjectId, son
import datetime
import pprint
from common.mongo import xqseccenter_db


# get loc x and y
def ip_loc(str_loc):
    l = str_loc.index(',')
    loc = list()
    x = ""
    y = ""
    for i in range(l):
        x +=str_loc[i]
    for i in range(l+1,len(str_loc)):
        y +=str_loc[i]
    loc.append(x)
    loc.append(y)
    return loc

def get_hpfeed():
    hpfeed = list()

    try:
        for item in xqseccenter_db.hpfeed.find({"timestamp":{'$gte': datetime.datetime.now() - datetime.timedelta(days=450)}}):

            s_info = get_ip_info(item["payload"]["remote"][0])

            if not s_info:
                country = "NoC"
                source = "Nosource"
            else:
                country = s_info["country"]
                source = {
                    "ip": item["payload"]["remote"][0],
                    "port": item["payload"]["remote"][1],
                    "lon": ip_loc(s_info["location"])[0],
                    "lat": ip_loc(s_info["location"])[1]
                }

            if not item["payload"]["public_ip"]:
                destination = "Nodestination"
            else:

                d_info = get_ip_info(item["payload"]["public_ip"])
                if not d_info:
                    continue
                else:
                    if not get_des_tag(item["payload"]["public_ip"]):
                        destination = {
                            "ip_tag": "NoTag",
                            "port": get_des_port(item["payload"]["data_type"]),
                            "lon":ip_loc(d_info["location"])[0],
                            "lat":ip_loc(d_info["location"])[1]
                        }
                    else:
                        destination = {
                            "ip_tag": get_des_tag(item["payload"]["public_ip"]),
                            "port": get_des_port(item["payload"]["data_type"]),
                            "lon":ip_loc(d_info["location"])[0],
                            "lat":ip_loc(d_info["location"])[1]
                        }

            hpfeed.append({"source": source,
                                "destination": destination,
                                "protocol":item["payload"]["data_type"],
                                "country":country,
                                "timestamp":str(item["timestamp"])})
    except ():
        pass
    return hpfeed

def _top(collecion, fields, top=10, tsgt="20151101", **kwargs):

    if isinstance(fields, basestring):
        fields = [fields,]

    match_query = dict([ (field, {'$ne': None}) for field in fields ])

    for name, value in kwargs.items():
        if name.startswith('ne__'):
            match_query[name[4:]] = {'$ne': value}
        elif name.startswith('gt__'):
            match_query[name[4:]] = {'$gt': value}
        elif name.startswith('lt__'):
            match_query[name[4:]] = {'$lt': value}
        elif name.startswith('gte__'):
            match_query[name[5:]] = {'$gte': value}
        elif name.startswith('lte__'):
            match_query[name[5:]] = {'$lte': value}
        else:
            match_query[name] = value

    match_query['timestamp'] = {
            '$gte':datetime.datetime.now() - datetime.timedelta(days=730)
    }

    query = [
        {
            '$match': match_query
        },
        {
            '$group': {
                '_id': dict( [(field, '${}'.format(field)) for field in fields] ),
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': son.SON([('count', -1)])
        }
    ]

    result_list = list(collecion.aggregate(query))[:top]

    return result_list

def _top_for_ipinfo(collecion, fields, top=10, **kwargs):

    if isinstance(fields, basestring):
        fields = [fields,]

    match_query = dict([ (field, {'$ne': None}) for field in fields ])

    for name, value in kwargs.items():
        if name.startswith('ne__'):
            match_query[name[4:]] = {'$ne': value}
        elif name.startswith('gt__'):
            match_query[name[4:]] = {'$gt': value}
        elif name.startswith('lt__'):
            match_query[name[4:]] = {'$lt': value}
        elif name.startswith('gte__'):
            match_query[name[5:]] = {'$gte': value}
        elif name.startswith('lte__'):
            match_query[name[5:]] = {'$lte': value}
        else:
            match_query[name] = value


    query = [

        {
            '$group': {
                '_id': dict( [(field, '${}'.format(field)) for field in fields] ),
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': son.SON([('count', -1)])
        }
    ]

    result_list = list(collecion.aggregate(query))[:top]
    return result_list

def get_ip_info(at_ip):
    return xqseccenter_db.ipaddrinfo.find_one({"ipaddr": at_ip})

def get_des_tag(at_ip):
    temp = xqseccenter_db.desipinfo.find_one({"ipaddr": at_ip})
    if not temp:
        result = "NoTagFound"
    else:
        result = temp["tag"]

    return result

def get_des_port(protocol):
    temp = xqseccenter_db.protoport.find_one({"protocol": protocol})
    if not temp:
        result = "NoProFound"
    else:
        result = temp["port"]

    return result

def get_top_country(top):
    result = list()
    result_list = _top_for_ipinfo(xqseccenter_db.ipaddrinfo,"country",top)
    for item in result_list:
        result.append({
            "count":item["count"],
            "country":item["_id"]["country"]
        })

    return result

def get_top_srcIP(top,tsgt):
    result = list()
    result_list = _top(xqseccenter_db.session,"source_ip",top,tsgt)
    for item in result_list:
        result.append({
            "count":item["count"],
            "source_ip":item["_id"]["source_ip"]
        })

    return result

def get_top_destag(top):
    result = list()
    result_list = _top_for_ipinfo(xqseccenter_db.desipinfo,"tag",top)
    for item in result_list:
        result.append({
            "count":item["count"],
            "tag":item["_id"]["tag"]
        })

    return result

def get_top_protocol(top,tsgt):
    result = list()
    result_list = _top(xqseccenter_db.session,"protocol",top,tsgt)
    for item in result_list:
        result.append({
            "count":item["count"],
            "protocol":item["_id"]["protocol"]
        })

    return result
