import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

import datetime
import random

from apiclient.discovery import build


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['YOUTUBE_DATA_API_KEY'] = 'AIzaSyDPRG9co3-DkVg-ek58XZD3YSbkmCi08X0'
db = SQLAlchemy(app)
ytapi = build('youtube', 'v3', developerKey=app.config['YOUTUBE_DATA_API_KEY'])

from models import ChannelModel

FILTERS = [
    {
        'name': 'Show All',
        'term': '',
    },
    {
        'name': 'Transgender',
        'term': 'trans',
    },
    {
        'name': 'Gay',
        'term': 'gay',
    },
    {
        'name': 'Crossdresser',
        'term': 'crossdress',
    },
    {
        'name': 'Genderfluid',
        'term': 'genderfluid',
    },
    {
        'name': 'Bisexual',
        'term': 'bisexual',
    },
    {
        'name': 'Pansexual',
        'term': 'pan',
    },
    {
        'name': 'Asexual',
        'term': 'asexual',
    },
    {
        'name': 'Genderqueer',
        'term': 'genderqueer',
    },
    {
        'name': 'Queer',
        'term': 'queer'
    }
]


def load_channel_list():
    source_channel = ChannelModel.get_channel(SOURCE_CHANNEL_ID)
    featured_channel_ids = source_channel.get_subscriptions()
    return [sub['snippet']['resourceId']['channelId'] for sub in featured_channel_ids]

SOURCE_CHANNEL_ID = 'UCjYn4RyjCCMJX67Rck4sq5A'
CHANNEL_IDS = load_channel_list()
LOAD_TIME = datetime.datetime.now()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channels/')
def get_channels():
    global LOAD_TIME
    global CHANNEL_IDS
    if (datetime.datetime.now() - LOAD_TIME > datetime.timedelta(hours=3)):
        CHANNEL_IDS = load_channel_list()
        LOAD_TIME = datetime.datetime.now()
    channels = [ChannelModel.get_channel(channel_id).dict for channel_id in CHANNEL_IDS]
    return jsonify(channels)

@app.route('/channel/videos/<channel_id>')
def get_channel_videos(channel_id):
    pass

@app.route('/random/channel/')
def get_random_channel():
    random_channel_id = random.choice(CHANNEL_IDS)
    channel = ChannelModel.get_channel(random_channel_id).dict
    return jsonify(channel)

@app.route('/random/playlist/')
def get_random_playlist():
    random_channel_id = random.choice(CHANNEL_IDS)
    channel = ChannelModel.get_channel(random_channel_id)
    playlist = channel.get_playlist()
    return playlist

@app.route('/filters/')
def get_filters():
    return jsonify(FILTERS)

@app.route('/channel/playlist/<channel_id>')
def get_channel_playlist(channel_id):
    playlist = ChannelModel.get_channel(channel_id).get_playlist()
    return playlist
    