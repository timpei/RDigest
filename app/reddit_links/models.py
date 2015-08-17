# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from .. import db

import datetime

# Define a User model
class RedditLink(db.Model):

    __tablename__ = 'reddit_link'

    id = db.Column(db.String(20), primary_key=True)

    url = db.Column(db.String(250))
    title = db.Column(db.String(250))
    score = db.Column(db.Integer)
    downs = db.Column(db.Integer)
    ups = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    created_utc = db.Column(db.DateTime)
    author = db.Column(db.String(80))
    domain = db.Column(db.String(80))
    banned_by = db.Column(db.String(80))
    selftext_html = db.Column(db.String(250))
    selftext = db.Column(db.String(250))
    link_flair_text = db.Column(db.String(100))
    subreddit = db.Column(db.String(80))
    gilded = db.Column(db.Integer)
    over_18 = db.Column(db.Boolean)
    num_comments = db.Column(db.Integer)
    thumbnail = db.Column(db.String(250))
    subreddit_id = db.Column(db.String(20))
    is_self = db.Column(db.Boolean)
    permalink = db.Column(db.String(250))


    # New instance instantiation procedure
    def __init__(self, *args, **kwargs):
        self.id              = kwargs['id']
        self.url             = kwargs['url']
        self.title           = kwargs['title']
        self.score           = kwargs['score']
        self.downs           = kwargs['downs']
        self.ups             = kwargs['ups']
        self.created         = datetime.datetime.fromtimestamp(kwargs['created'])
        self.created_utc     = datetime.datetime.utcfromtimestamp(kwargs['created_utc'])
        self.author          = kwargs['author']
        self.domain          = kwargs['domain']
        self.banned_by       = kwargs['banned_by']
        self.selftext_html   = kwargs['selftext_html']
        self.selftext        = kwargs['selftext']
        self.link_flair_text = kwargs['link_flair_text']
        self.subreddit       = kwargs['subreddit']
        self.gilded          = kwargs['gilded']
        self.over_18         = kwargs['over_18']
        self.num_comments    = kwargs['num_comments']
        self.thumbnail       = kwargs['thumbnail']
        self.subreddit_id    = kwargs['subreddit_id']
        self.is_self         = kwargs['is_self']
        self.permalink       = kwargs['permalink']

    def __repr__(self):
        return '<RLink %r>' % (self.permalink)   