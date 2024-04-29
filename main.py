from flask import Flask, request, jsonify, make_response
from helper import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    response = make_response(jsonify({
        'status': 'Success!',
        'message': 'Welcome to ML-45 Machine Learning Model Deployment Demo!'
    }))
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'

    return response.json

@app.route('/classify', methods=['POST'])
def classify():
    try:
        json_response = request.get_json()
        classification_result, percentage = classification(json_response["payload"])
       
        response_data = {
            'status': 'Success!',
            'message': classification_result,
            'percentage': str("{}%".format(round(percentage)))
        }
        response = make_response(jsonify(response_data))
        response.status_code = 200
        response.headers['Content-Type'] = 'application/json'
        
        return response
    except Exception as e:
        response = make_response(jsonify({
            'status': 'Error',
            'message': str(e)
        }))
        response.status_code = 500
        response.headers['Content-Type'] = 'application/json'

        return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)