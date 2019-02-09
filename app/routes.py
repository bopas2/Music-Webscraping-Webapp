from app import app
from .scrape_test import scrape_stuff
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tommy'}
    return render_template('index.html', title='Home', user=user)

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def band_entry_post():
    text = request.form['text']
    return scrape_stuff(text)

