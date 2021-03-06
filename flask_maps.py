"""
Flask web server for the Eugene Map application. Uses
Leaflet for mapping data.
"""

import flask
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

# Own modules
from maps import POI

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

# The points of interest from our POI file
POIs = POI( CONFIG.poi )

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    flask.g.poi = POIs.points
    return flask.render_template('maps.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404


#################
#
# Set up to run from cgi-bin script,
# from gunicorn, or stand-alone.
#
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)
if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
