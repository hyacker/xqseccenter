#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


#source data request url
FEED_URL = 'http://mhn.ics0day.org/api/feed/'
SESSION_URL = 'http://mhn.ics0day.org/api/session/'
TOP_ATTACKERS_URL = 'http://mhn.ics0day.org/api/top_attackers/'
REQ_API_KEY = 'eabf58e12536416888bef183142894e9'


class Config:
    #mongodb config
    MONGODB_DATABASE_URI = "mongodb://localhost:27017/"
    MONGODB_DBNAME = "xqseccenter"

    #source data request url
    FEED_URL = 'http://mhn.ics0day.org/api/feed/'
    SESSION_URL = 'http://mhn.ics0day.org/api/session/'
    TOP_ATTACKERS_URL = 'http://mhn.ics0day.org/api/top_attackers/'
    REQ_API_KEY = 'eabf58e12536416888bef183142894e9'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
