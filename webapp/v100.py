
VERSION_STR = 'v1.0.0'

import base64
import requests
import numpy as np
from error import Error
from flask import Blueprint, request, jsonify
import autocomplete as autocomp
import sys
import os
import cPickle as pickle
import random
from src.recommender import *

movies = pickle.load( open( "../../data/movies_input.p", "rb" ))
comp = autocomp.MyCompleter(movies)


blueprint = Blueprint(VERSION_STR, __name__)

def games_input():
    games = pickle.load( open( "../../data/games_input.p", "rb" ))
    return random.sample(games, 10)

def recom_(postive_ids, negative_ids):
    # Loading trainning model
    t_model_m_g = load_input_data('../../data/model_m_g')
    t_model_m = load_input_data('../../data/model_m')
    t_model_g = load_input_data('../../data/model_g')

    #make recommendation
    user = 'user'
    pos_rate = [5]*len(postive_ids)
    neg_rate = [1]*len(negative_ids)

    postive_ids.extend(negative_ids)
    pos_rate.extend(neg_rate)

    recom = recommender_process(user, postive_ids, pos_rate,
                                t_model_m_g, t_model_m, t_model_g)
    print "Hi, we are here!"
    print 'recom', recom
    return recom





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
    '''names = {'The Theory of Everything': '1273464343', 'Truman Show': '0573469341', 'Matrix': '0070004343', 'Inception': '0275468343',
            'Futurama': '0078714343', 'Battlestar Galactica': '0073464343', 'Breaking Bad': '0056764123', 'How to train your Dragon': '0073064300',
            'Into the Wild': '0078764343', 'Lock, Stock and Two Smoking Barrels': '0012464123', 'Cloud Atlas': '0012464300'}
    '''
    search_terms = request.args['q']
    results_list = comp.complete(search_terms)
    results = jsonify({'results': results_list})
    results.headers.add('Access-Control-Allow-Origin', '*')
    return results

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
    postive_ids = request.args['postive_ids'].split(',');
    negative_ids = request.args['negative_ids'].split(',')
    recom = recom_(postive_ids, negative_ids)
#    recom = get_results(recom)

    d = jsonify({'results': recom})
    d.headers.add('Access-Control-Allow-Origin', '*')
    return d


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

    rand_games = games_input()
    d = jsonify({'results': rand_games})
    d.headers.add('Access-Control-Allow-Origin', '*')
    return d



from app import app
app.register_blueprint(blueprint, url_prefix='/'+VERSION_STR)
