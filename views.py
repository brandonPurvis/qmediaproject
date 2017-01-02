import datetime
import random

from flask import render_template, jsonify

from main import app, db, ytapi
from main import load_channel_list
from models import ChannelModel


CHANNEL_IDS = load_channel_list()
LOAD_TIME = datetime.datetime.now()
REFRESH_TIME_DELTA = datetime.timedelta(hours=3)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/channels/')
def get_channels():
    global LOAD_TIME
    global CHANNEL_IDS
    if (datetime.datetime.now() - LOAD_TIME > REFRESH_TIME_DELTA):
        CHANNEL_IDS = load_channel_list()
        LOAD_TIME = datetime.datetime.now()
    channels = [ChannelModel.get_channel(channel_id).dict for channel_id in CHANNEL_IDS]
    return jsonify(channels)


@app.route('/channel/playlist/<channel_id>')
def get_channel_playlist(channel_id):
    playlist = ChannelModel.get_channel(channel_id).get_playlist()
    return playlist


@app.route('/random/playlist/')
def get_random_playlist():
    random_channel_id = random.choice(CHANNEL_IDS)
    channel = ChannelModel.get_channel(random_channel_id)
    playlist = channel.get_playlist()
    return playlist


@app.route('/filters/')
def get_filters():
    FILTERS = [
        {'name': 'Show All', 'term': ''},
        {'name': 'Transgender', 'term': 'trans'},
        {'name': 'Gay', 'term': 'gay'},
        {'name': 'Crossdresser', 'term': 'crossdress'},
        {'name': 'Genderfluid', 'term': 'genderfluid'},
        {'name': 'Bisexual', 'term': 'bisexual'},
        {'name': 'Pansexual', 'term': 'pan'},
        {'name': 'Asexual', 'term': 'asexual'},
        {'name': 'Genderqueer', 'term': 'genderqueer'},
        {'name': 'Queer', 'term': 'queer'}
    ]
    return jsonify(FILTERS)