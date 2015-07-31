# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

from app.reddit_links.models import RedditLink

# Define the blueprint: 'reddit_link', set its url prefix: app.url/reddit_link
reddit_link = Blueprint('reddit_link', __name__, url_prefix='/api/reddit_link')