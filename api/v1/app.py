#!/usr/bin/python3
"""
Module to register blueprints and run the flask server
in preparation for api calls
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import engine
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_flask(exception):
    """
    Remove the database, exit and save file
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return (jsonify(error="Not found"), 404)

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port)
