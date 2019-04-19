from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import base64
from SP import predict_prices, date_to_int
from Twitter import search_twitter

app = Flask(__name__)
CORS(app)

KNOWN_COMPANIES = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOG': 'Google',
    'FB': 'Facebook',
    'COF': 'Capital One',
    'ATVI': 'Activision'
}


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/predict/<string:symbol>/<string:date>', methods=['GET'])
def predict(symbol, date):
    predicted_price, (xs, ys) = predict_prices(symbol, date_to_int(date))
    tweet = ''
    sentiment = 'Unknown'
    if symbol.upper() in KNOWN_COMPANIES:
        sentiment, tweet = search_twitter(KNOWN_COMPANIES[symbol.upper()])
    else:
        sentiment, tweet = search_twitter(symbol)
    return jsonify({'price': predicted_price, 'xs': xs.tolist(), 'ys': ys, 'tweet': tweet, 'sentiment': sentiment})


@app.route('/register/<string:username>', methods=['POST'])
def register(username):
    if request.method == 'POST':
        # f = request.files['face_image']
        # print('face_images/' + request.args.get('username') + '.jpg')
        # f.save('face_images/'+request.args.get('username')+'.jpg')
        content = request.get_json()
        img_data = content['img'].split('base64,')[1]
        with open('face_images/'+username+'.png', 'wb') as fh:
            fh.write(base64.b64decode(img_data))
        return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
