from flask import Flask, render_template
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
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/author')
def author_review():
    return render_template('author.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/book/<book_id>')
def book_review(book_id):
    return "Book Review Page - Work in Progress"

@app.teardown_appcontext
def close_connection(exception):
    client.close()



if __name__ == '__main__':
    app.run(debug=True)
