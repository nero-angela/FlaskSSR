from flask import Flask, request, render_template

from util.builder import PreBuilder
from util.filter import Filter

app = Flask(__name__)
PreBuilder(app)
Filter(app)


@app.route('/')
def home():
    return render_template('page/main/page_main.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
