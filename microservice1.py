import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/zipcode', methods=['GET'])
def get_zipcode():
    city = request.args.get('city')
    state = request.args.get('state')
    api_key = "bufw3kh2x6b3xupe"
    # api_url = "https://api.example.com/zipcode?city={}&key={}".format(city, api_key)
    api_url = f"https://www.zipwise.com/webservices/citysearch.php?key={api_key}&format=json&string={city}&state={state}"
    #check address: http://127.0.0.1:8000/zipcode?city=Sunnyvale&state=CA
    response = requests.get(api_url)
    # if response.status_code == 200:
    zipcode = response.json()
    return jsonify({'zipcode': zipcode})
    # else:
        # return jsonify({'error': 'Error when calling the zipcode API'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port = 8000)


