#create app route
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/")
def index():
    return "Welcome to API version 1.0 by Atnlie"

@app.route("/countries", methods=['GET', 'POST'])
def get_countries():
    try:
        if request.method == "GET":
            print(request.args)
            return make_response(jsonify({
            'data': countries,
            'code': 200, 
            'error': ''
            }), 200)
        elif request.method == "POST":
            body = request.get_json()
            country = {
                "id": _find_next_id(),
                "name": body["name"],
                "capital": body["capital"],
                "area": body["area"]
            }
            countries.append(country)
            
            return make_response(jsonify({
                'message': "Create country successfully",
                'code': 200, 
                'error': ''
            }), 200)
    except Exception as e:
        return make_response(jsonify({
            'data': [],
            'code': 500, 
            'error': f'Something went wrong because {e}'
        }), 500)

@app.route("/countries/<id>", methods=['DELETE'])
def remove_country(id):
    try:
        for index, country in enumerate(countries):
            if country["id"] == int(id):
                countries.pop(index)
                return make_response(jsonify({
                    'message': "Delete country successfully",
                    'code': 200, 
                    'error': ''
                }), 200)
        return make_response(jsonify({
            'message': "Country not found",
            'code': 404, 
            'error': ''
        }), 404)
    except Exception as e:
        return make_response(jsonify({
            'data': [],
            'code': 500, 
            'error': f'Something went wrong because {e}'
        }), 500)

app.run()


