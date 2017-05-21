#!/usr/bin/env python
#coding:utf-8

from mongoengine import *
from datetime import datetime

connect('xqseccenter')

class RankList(Document):
    top_country = ListField(DictField())
    top_srcIP = ListField(DictField())
    top_destag = ListField(DictField())
    top_protocol = ListField(DictField())


    def get_dict_info(self):
        return {
            "top_country": self.top_country,
            "top_srcIP": self.top_srcIP,
            "top_destag": self.top_destag,
            "top_protocol": self.top_protocol,
        }
