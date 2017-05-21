from datetime import datetime
import json

from flask import (jsonify, abort, request, make_response)
from .. import threat
from common import mongo

@threat.route('/rank-list/',methods=['GET'])
def ranklist():

    top_country = mongo.get_top_country(10)
    top_srcIP = mongo.get_top_srcIP(10,"20151101")
    top_destag = mongo.get_top_destag(10)
    top_protocol = mongo.get_top_protocol(10,"20151101")

    return jsonify({
        "top_country": top_country,
        "top_srcIP": top_srcIP,
        "top_destag": top_destag,
        "top_protocol": top_protocol
    })

@threat.route('/rank-list/top-country/',methods=['GET'])
def top_country_rank():
    top_country = mongo.get_top_country(10)
    return jsonify({
        "top_protocol": top_country
    })

@threat.route('/rank-list/top-protocol/',methods=['GET'])
def top_protocol_rank():
    top_protocol = mongo.get_top_protocol(10,"20151101")
    return jsonify({
        "top_protocol": top_protocol
    })

@threat.route('/rank-list/top-desti/',methods=['GET'])
def top_destination_rank():
    top_destag = mongo.get_top_destag(10)
    return jsonify({
        "top_destag": top_destag
    })

@threat.route('/rank-list/top-attackers/',methods=['GET'])
def top_source_rank():
    top_srcIP = mongo.get_top_srcIP(10,"20151101")
    return jsonify({
        "top_srcIP": top_srcIP
    })
