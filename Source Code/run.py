from flask import Flask, render_template, jsonify
from flask_cors import CORS
from SP import predict_prices, date_to_int
from Twitter import search_twitter
import collections
import base64

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

KNOWN_COMPANIES = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOG': 'Google',
    'FB': 'Facebook',
    'COF': 'Capital One',
    'ATVI': 'Activision'
}

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

@app.route('/predict/<string:symbol>/<string:date>', methods=['GET'])
def predict(symbol, date):
    predicted_price, (xs, ys) = predict_prices(symbol, date_to_int(date))
    tweet = ''
    sentiment = 'Unknown'
    a = ['year', 'price']
    xs = flatten(xs.tolist())
    ys = list(map(float, ys))
    merged = [(xs[i], ys[i]) for i in range(0, len(xs))]
    merged.insert(0, a)
    if symbol.upper() in KNOWN_COMPANIES:
        sentiment, tweet = search_twitter(KNOWN_COMPANIES[symbol.upper()])
    else:
        sentiment, tweet = search_twitter(symbol)
    return jsonify({'price': predicted_price, 'xs': xs, 'ys': ys, 'tweet': tweet, 'sentiment': sentiment, 'merged': merged})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")
