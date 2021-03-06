from flask import Flask, request, render_template

from buider import PreBuilder

app = Flask(__name__)
PreBuilder(app)

@app.route('/')
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
