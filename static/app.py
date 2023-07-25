from flask import Flask, request, jsonify
import numpy as np
import sqlalchemy
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
from pymongo import MongoClient

#################################################
# Database Setup
#################################################
client = MongoClient('mongodb://localhost:27017/')
db = client['king-bachman']
collection = db['king-bachman']

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    return (
        f"Welcome to the King-Bachman API!<br/>"
        f"Available Routes:<br/>"
        f"...."
    )

@app.route('/author')
def author_review():
    return render_template('author.html')

@app.route('/book/<book_id>')
def book_review(book_id):


@app.teardown_appcontext
def close_connection(exception):
    client.close()

if __name__ == '__main__':
    app.run(debug=True)