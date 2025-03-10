#!/usr/bin/python3
<<<<<<< HEAD
"""
landing page for api
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def app_status():
    """
    Simply returns the state of the api.
    """
    return(jsonify(status="OK"))


@app_views.route('/stats')
def app_get_count():
    """
    Returns statistics about the number of objects available
    """
    tojson = {}
    for cls in storage.available_classes:
        string = str(cls).lower()
        if string[-1] is 'y':
            string = string[0:-1] + "ies"
        else:
            string += "s"
        tojson.update({string: storage.count(cls)})
    return(jsonify(tojson))
=======
"""API index views module"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from models import storage
from flask import jsonify, request


@app_views.route('/status')
def status():
    """
    Returns json response as the status
    Returns:
        JSON: json object
    """
    status = {
        "status": "OK"
    }
    return jsonify(status)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
>>>>>>> 2368f9ffd2d3f82b254b446318791803e05f35fd
