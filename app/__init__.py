# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_pyfile('../config.py')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
from app.reddit_links.controllers import reddit_link as reddit_link_module

app.register_blueprint(reddit_link_module)

# Build the database:
db.create_all()

# Set the route and accepted methods
@app.route('/', methods=['GET'])
def signin():
    return render_template("index.html")