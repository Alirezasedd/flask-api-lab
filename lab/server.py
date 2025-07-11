# Import the Flask class from the flask module
from flask import Flask, request, jsonify, make_response

from flask import Flask, make_response
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"


from flask import Flask

app = Flask(__name__)

@app.route("/no_content")
def no_content():
    """
    return 'No content found' with a status of 204

    Returns:
        string: No content found
        status code: 204
    """
    return {"message": "No content found"}, 204

from flask import make_response  # Add this to your import line

@app.route("/exp")
def index_explicit():
    """
    return 'Hello world' message with a status of 200

    Returns:
        string: Hello world
        status code: 200
    """
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp

@app.route("/name_search")
def name_search():
    """
    Search for a person based on the 'q' query parameter
    """
    query = request.args.get("q")

    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    return {"message": "Person not found"}, 404


@app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

from uuid import UUID  # Ensure this is imported at the top

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person, 200
    return {"message": "person not found"}, 404


@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message": f"Person with ID {id} deleted"}, 200
    return {"message": "person not found"}, 404


@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json

    if not new_person:
        return {"message": "Invalid input parameter"}, 422

    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404


@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500


@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")
