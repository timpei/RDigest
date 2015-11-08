# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import Triangle
from flask.ext.triangle import Triangle

# Define the WSGI application object
app = Flask(__name__)
Triangle(app)

# Configurations
app.config.from_pyfile('../config.py')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
from reddit_links.controllers import reddit_link as reddit_link_module
from reddit_links.controllers import links as links_module

app.register_blueprint(reddit_link_module)
app.register_blueprint(links_module)

# Build the database:
db.create_all()

# Set the route and accepted methods
@app.route('/', methods=['GET'])
def signin():
	return render_template("index.html")