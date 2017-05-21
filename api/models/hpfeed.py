#!/usr/bin/env python
#coding:utf-8

from mongoengine import *
from datetime import datetime

connect('xqseccenter')


class Feed(Document):
    ident = StringField()
    timestamp = DateTimeField()
    payload = ListField(DictField())
    channel = StringField()

class FeedData(Document):
    src_ipinfo = ListField(DictField())
    des_ipinfo = ListField(DictField())
    protocol = StringField()
    country = StringField()
    timestamp = DateTimeField()

    def get_dict_info(self):
        return {
            "country": self.country,
            "protocol": self.protocol,
            "source": self.src_ipinfo,
            "destination": self.des_ipinfo,
            "timestamp": self.timestamp
        }
