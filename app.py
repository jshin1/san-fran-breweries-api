from flask import Flask, jsonify
from breweries import san_fran_breweries

app = Flask(__name__)

@app.route('/breweries', methods=['GET'])
def get_breweries():
    response = jsonify(san_fran_breweries)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
