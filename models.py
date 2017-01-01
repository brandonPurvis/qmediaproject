from datetime import datetime
from lib.youtube_api import YOUTUBE
from main import db


class ChannelModel(db.Model):
	channel_id = db.Column(db.String(200), primary_key=True)
	name = db.Column(db.String(200))
	image = db.Column(db.String(500))
	desc = db.Column(db.Text())
	birth = db.Column(db.DateTime())

	@classmethod
	def load_channel(cls, channel_id):
		print("Loading {}".format(channel_id))
		search_response = YOUTUBE.channels().list(
			part='snippet',
			id=channel_id,
		).execute()
		found = search_response.get('items')
		if found:
			found = found[0]
			name = found['snippet']['title']
			image = found['snippet']['thumbnails']['high']['url']
			description = found['snippet']['description']
			channel_id = found['id']
			return cls(name, image, description, channel_id)
		return None

	@classmethod
	def get_channel(cls, channel_id):
		found = cls.query.filter_by(channel_id=channel_id).first()
		if not found:
			found = cls.load_channel(channel_id)
		return found

	def __init__(self, name, image, desc, channel_id):
		self.name = name
		self.image = image
		self.desc = desc
		self.channel_id = channel_id
		self.birth = datetime.now()
		self.save()

	def save(self):
		db.session.add(self)
		db.session.commit()

	@property
	def tags(self):
		return []

	@property
	def link(self):
		return 'http://www.youtube.com/channel/{}'.format(self.channel_id)

	@property
	def dict(self):
		return {
			'name': self.name,
			'image': self.image,
			'desc': self.desc,
			'link': self.link,
			'channel_id': self.channel_id,
			'tags': self.tags,
		}

	def get_subscriptions(self):
		subscriptions = YOUTUBE.subscriptions().list(
			part='snippet',
			channelId=self.channel_id,
			maxResults=10,
			pageToken=pageToken,
		).execute()
		items = subscriptions['items']
		nextPageToken = subscriptions.get('nextPageToken')
		while nextPageToken:
			subscriptions = YOUTUBE.subscriptions().list(
				part='snippet',
				channelId=self.channel_id,
				maxResults=10,
				pageToken=nextPageToken,
			).execute()
			next_items = subscriptions['items']
			nextPageToken = subscriptions.get('nextPageToken')
			items += next_items
		return items

	def get_playlist(self):
		channel_resources = YOUTUBE.channels().list(
			part='ContentDetails',
			id=self.channel_id,
		).execute()
		playlist_id = channel_resources['items'][0]['contentDetails']['relatedPlaylists']['uploads']
		playlist_response = YOUTUBE.playlists().list(
			part='player',
			id=playlist_id,
		).execute()
		playlist_player = playlist_response['items'][0]['player']['embedHtml']
		return playlist_player


	def __str__(self):
		return "Channel {}".format(self.name)

	def __repr__(self):
		return '{}'.format(self.dict)
