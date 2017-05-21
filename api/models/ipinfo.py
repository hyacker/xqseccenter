#!/usr/bin/env python
#coding:utf-8

from mongoengine import *
from datetime import datetime

connect('xqseccenter')

class IpaddrInfo(Document):
    city = StringField()
    location = StringField()
    country = StringField()
    region = StringField()
    hostname = StringField()
    ipaddr = StringField()
    org = StringField()
    postal = StringField()

class DesipInfo(Document):
    ipaddr = StringField()
    tag = StringField()
    protocol = StringField()
    location = StringField()
    country = StringField()
        
