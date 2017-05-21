from datetime import datetime
import json

from flask import (jsonify, abort, request, make_response)
from .. import threat
from common import mongo

@threat.route('/feed/', methods=['GET'])
def get_feed():
    """
    this method is to get FeedData for frontdest

    """
    return jsonify(dict({
                "result": mongo.get_hpfeed(),
                "code": 200
                }))
