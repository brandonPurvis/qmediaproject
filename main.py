import youtube_api
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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
        'term': 'bi',
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

CHANNEL_IDS = [
    'UCXwXB7a3cq9AERiWF4-dK9g',
    'UCC_S5oOAJp0iaF4fDT3QS0g',
    'UCzhIKG1HTg5LFywIloswtdg',
    'UCHAv1g2JODsrkUKfHh1nAwQ',
    'UCTcTyyKBldse-dVm4oK3Q-A',
    'UC6dFzH8Xu3lNf1-TUdwmHdg',
    'UCxFWzKZa74SyAqpJyVlG5Ew',
    'UCB1uhE6_aIKQlPW4S0uS3XA',
    'UCTr21rc3wtfuy1uBmI5unQw',
    'UCZeJuSF6Kbk-iIY41do3HhA',
    'UCW0CJrqEdfAi2eCvBsOYiyw',
    'UCaKSM3W89n3Xg0wvNuDWfaw',
    'UCjYn4RyjCCMJX67Rck4sq5A',
    'UCamaea05bOJ0q42F9iyaFMA',
    'UCeNgRHpH7OHZetYjC5JZXGw',
    'UCXX0iCrVQnlNvGW4gKEhHdA',
    'UCO5I_cqWWo56i2ehlHwmKHQ',
    'UCNEd4in0ykBsJF5DZNhvtlw',
    'UCaWf6VC6vmZcGdI_I0XYeRw',
    'UCn5Ulxbz0p8sH3OPqTLIaNg',
    'UCsg53sunTbA9d8ksMaXEAzQ',
    'UC7XFgbOyFBoGxssEwGvkKig',
    'UCT-UG5N5QWq80fKJrue77ag',
    'UCf0CRezZYOUcvqrdMmozowQ',
    'UCysJoxOdm866XPG-1rm2-vw',
    'UCT9lRRTBWIqMIfVgSyfsg7Q',
    'UCLwrLrQPNKsMr9p1035cizA',
    'UCUJvkFRoXA3qOUkogplkEXg',
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channels/')
def get_channels():
    channels = [youtube_api.get_channel(channel_id).add_tags(FILTERS[1:]).dict() for channel_id in CHANNEL_IDS]
    return jsonify(channels)

@app.route('/filters/')
def get_filters():
    return jsonify(FILTERS)

@app.route('/channel/playlist/<channel_id>')
def get_channel_playlist(channel_id):
    print(channel_id)
    playlist = youtube_api.get_channel_playlist(channel_id)
    return playlist