from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__, )
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/home": {"origins": "http://127.0.0.1:5000"}})


@app.route("/home")
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def home():
    return render_template('dashboard.html')


@app.route("/commentary")
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def commentary():
    return render_template('commentary.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
