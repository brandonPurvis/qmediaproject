from datetime import datetime, timedelta
import random

from flask import render_template, jsonify

from main import app, db, ytapi
from main import load_channel_list
from models import ChannelModel


CHANNEL_IDS = load_channel_list()
LOAD_TIME = datetime.now()
REFRESH_TIME_DELTA = timedelta(hours=3)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info/<channel_id>')
def info(channel_id):
    channel = ChannelModel.get_channel(channel_id)
    return render_template('channel_info.html', channel=channel)

@app.route('/channels/')
def get_channels():
    global LOAD_TIME
    global CHANNEL_IDS
    if (datetime.now() - LOAD_TIME > REFRESH_TIME_DELTA):
        CHANNEL_IDS = load_channel_list()
        LOAD_TIME = datetime.now()
    channels = [ChannelModel.get_channel(channel_id) for channel_id in CHANNEL_IDS]
    channels = sorted(
        channels,
        key=lambda x: datetime.strptime(x.last_video['publishedAt'], "%Y-%m-%dT%H:%M:%S.000Z"),
        reverse=True
    )
    channels = [channel.dict for channel in channels]
    return jsonify(channels)


@app.route('/channel/playlist/<channel_id>')
def get_channel_playlist(channel_id):
    channel = ChannelModel.get_channel(channel_id)
    playlist = channel.get_playlist()
    return playlist


@app.route('/random/playlist/')
def get_random_playlist():
    random_channel_id = random.choice(CHANNEL_IDS)
    channel = ChannelModel.get_channel(random_channel_id)
    playlist = channel.get_playlist()
    return playlist


@app.route('/channel/videos/<channel_id>')
def get_channel_videos(channel_id):
    channel = ChannelModel.get_channel(channel_id)
    videos = channel.get_videos()
    return jsonify(videos)


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