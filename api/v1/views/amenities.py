<<<<<<< HEAD
#!/usr/bin/python3
'''Contains the amenities view for the API.'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """Retrieves the list of all Amenity objects"""
    objs = storage.all(Amenity)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def single_amenities(amenity_id):
    """Retrieves a Amenity object"""
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenities(amenity_id):
    """Returns an empty dictionary with the status code 200"""
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)

    obj.delete()
    storage.save()
=======

bjects that handles all default RestFul API actions for Amenities"""
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@swag_from('documentation/amenity/all_amenities.yml')
def get_amenities():
    """
    Retrieves a list of all amenities
    """
    all_amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in all_amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_amenity.yml', methods=['GET'])
def get_amenity(amenity_id):
    """ Retrieves an amenity """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete_amenity.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Deletes an amenity  Object
    """

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    storage.delete(amenity)
    storage.save()

>>>>>>> 2368f9ffd2d3f82b254b446318791803e05f35fd
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
<<<<<<< HEAD
def post_amenity():
    """Returns the new Amenity with the status code 201"""
    new_amenity = request.get_json()
    if not new_amenity:
        abort(400, "Not a JSON")
    if 'name' not in new_amenity:
        abort(400, "Missing name")

    obj = Amenity(**new_amenity)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """Returns the Amenity object with the status code 200"""
    obj = storage.get(Amenity, amenity_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for k, v in req.items():
        if k not in ['id', 'created_at', 'update_at']:
            setattr(obj, k, v)

    storage.save()
    return make_response(jsonify(obj.to_dict()), 200)
=======
@swag_from('documentation/amenity/post_amenity.yml', methods=['POST'])
def post_amenity():
    """
    Creates an amenity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Amenity(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put_amenity.yml', methods=['PUT'])
def put_amenity(amenity_id):
    """
    Updates an amenity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(amenity, key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)
>>>>>>> 2368f9ffd2d3f82b254b446318791803e05f35fd
