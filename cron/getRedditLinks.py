# Import flask and template operators
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os, inspect, sys, json, urllib2
import datetime

cmd_folder = os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0])
sys.path.append(cmd_folder+'/../')


from app.reddit_links.models import RedditLink

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

url = "http://www.reddit.com/r/news/top.json?limit=100"
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

try:
	links = json.loads(urllib2.urlopen(url).read())

	new = 0

	for link in links['data']['children']:
		rl = RedditLink(**link['data'])
		if (RedditLink.query.get(rl.id)):
			db.session.merge(rl)
		else:
			new += 1
			db.session.add(rl)

	db.session.commit()


	print "[%s] %d links found, %d new" % (time, len(links['data']['children']), new)

except urllib2.HTTPError: 

	print "[%s] request rejected" % time
