# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Import the database object from the main app module
from app import db
from app.reddit_links.models import RedditLink

import urllib2
import json

# Define the blueprint: 'reddit_link', set its url prefix: app.url/reddit_link
reddit_link = Blueprint('reddit_link', __name__, url_prefix='/api/reddit_link')

@reddit_link.route('/get_links/', methods=['GET'])
def getLinks():
	url = "http://www.reddit.com/r/news/hot.json?limit=100"
	links = json.loads(urllib2.urlopen(url).read())

	for link in links['data']['children']:
		rl = RedditLink(**link['data'])
		if (RedditLink.query.get(rl.id)):
			db.session.merge(rl)
		else:
			db.session.add(rl)

	db.session.commit()


	return jsonify(**links)