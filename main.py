import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from apiclient.discovery import build


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['YOUTUBE_DATA_API_KEY'] = os.environ["YTUBE_DATA_KEY"]
app.config['YOUTUBE_SOURCE_CHANNEL_ID'] = os.environ["YTUBE_SOURCE_CHANNEL"]
db = SQLAlchemy(app)
ytapi = build('youtube', 'v3', developerKey=app.config['YOUTUBE_DATA_API_KEY'])


from models import ChannelModel

def load_channel_list():
    source_channel = ChannelModel.get_channel(app.config['YOUTUBE_SOURCE_CHANNEL_ID'])
    featured_channel_ids = source_channel.get_subscriptions()
    return [sub['snippet']['resourceId']['channelId'] for sub in featured_channel_ids]

from views import *


if __name__ == '__main__':
    app.run()