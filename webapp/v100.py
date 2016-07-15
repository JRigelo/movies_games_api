
VERSION_STR = 'v1.0.0'

import base64
import requests
import numpy as np
from error import Error
from flask import Blueprint, request, jsonify
import autocomplete as autocomp

blueprint = Blueprint(VERSION_STR, __name__)


@blueprint.route('/autocomplete', methods=['GET'])
def autocomplete():
    '''
    Easy autocomplete
    Use this endpoint to give you a bunch of autocompleted string from
    a short query string.
    ---
    tags:
     - v1.0.0

    responses:
     200:
       description: Returns a dictionary with one key 'response' and a value with a list of strings that autocomplete the query
     default:
       description: Unexpected error
       schema:
         $ref: '#/definitions/Error'

    parameters:
     - name: q
       in: query
       description: The query partial string thing
       required: true
       type: string

    consumes:
     - multipart/form-data
     - application/x-www-form-urlencoded
    '''

    names = {'The Theory of Everything': '1273464343', 'Truman Show': '0573469341', 'Matrix': '0070004343', 'Inception': '0275468343',
            'Futurama': '0078714343', 'Battlestar Galactica': '0073464343', 'Breaking Bad': '0056764123', 'How to train your Dragon': '0073064300',
            'Into the Wild': '0078764343', 'Lock, Stock and Two Smoking Barrels': '0012464123', 'Cloud Atlas': '0012464300'}
    comp = autocomp.MyCompleter(names)

    search_terms = request.args['q']
    results_list = comp.complete(search_terms)
    results_dict = {'results': results_list}
    return jsonify(results_dict)

@blueprint.route('/make_recommendation', methods=['GET'])
def make_recommendation():
    '''
    Make recommendation
    Take a list of items the user likes and a list of items the user doesn't like, and return
    a list of recommended items for that user.
    ---
    tags:
     - v1.0.0

    responses:
     200:
       description: Returns a dictionary with one key 'response' and a value with a list of tuples, each with info about one recommended item
     default:
       description: Unexpected error
       schema:
         $ref: '#/definitions/Error'

    parameters:
     - name: postive_ids
       in: query
       description: A list of item IDs that the user likes
       required: true
       type: array
       item:
          type: string
     - name: negative_ids
       in: query
       description: A list of item IDs the user dislikes
       required: true
       type: array
       item:
          type: string

    consumes:
     - multipart/form-data
     - application/x-www-form-urlencoded
    '''
    url1 = 'http://ecx.images-amazon.com/images/I/4182SKAN99L._SY300_.jpg'
    url2 = 'http://ecx.images-amazon.com/images/I/41ch9L5Vi7L._SY300_.jpg'
    url3 = 'http://ecx.images-amazon.com/images/I/51RMW3K3N9L._SY300_.jpg'
    am1 = 'https://www.amazon.com/dp/0439339960'
    am2 = 'https://www.amazon.com/dp/0439339970'
    am2 = 'https://www.amazon.com/dp/0439339980'
    d = {'results': [(url1, am1),
       (url2, am1),(url3, am1)]}
    return jsonify(d)

@blueprint.route('/games_samples', methods=['GET'])
def games_samples():
    '''
    Image samples for games
    Request a list of tuples with games image urls and correspondent IDs.
    ---
    tags:
     - v1.0.0

    responses:
     200:
       description: Request a list of tuples with games image urls and correspondent IDs.
     default:
       description: Unexpected error
       schema:
         $ref: '#/definitions/Error'


    consumes:
     - multipart/form-data
     - application/x-www-form-urlencoded
    '''
    url1 = 'http://ecx.images-amazon.com/images/I/4182SKAN99L._SY300_.jpg'
    url2 = 'http://ecx.images-amazon.com/images/I/41ch9L5Vi7L._SY300_.jpg'
    url3 = 'http://ecx.images-amazon.com/images/I/51RMW3K3N9L._SY300_.jpg'
    Id1 = '000924824'
    Id2 = '0001348134'
    Id3 = '00024824723'
    d = {'results': [(url1, Id1),
       (url2, Id2),(url3, Id3)]}
    return jsonify(d)






from app import app
app.register_blueprint(blueprint, url_prefix='/'+VERSION_STR)
