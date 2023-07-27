from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import json
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

@app.route('/api/v1.0/authors')
def get_authors_data():
    with open('static/data/charts/author_dates.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

def get_authors_and_books():
    authors = {}  # Dictionary to store authors and their books
    for book in collection.find():
        book_id = str(book['_id'])
        book_title = book['volumeInfo']['title']

        # Check if 'authors' key exists before accessing it
        if 'authors' in book['volumeInfo']:
            book_authors = book['volumeInfo']['authors']
            for author in book_authors:
                if author not in authors:
                    authors[author] = []
                authors[author].append({'id': book_id, 'title': book_title})

    return authors



def prepare_data_for_cytoscape(authors_data):
    nodes = []
    edges = []
    for author, books in authors_data.items():
        # Create the central node for each author
        nodes.append({'data': {'id': author, 'label': author, 'type': 'author'}})

        for book in books:
            book_id = book['id']
            book_title = book['title']
            book_image = None  # Default value for the image URL

            # Check if 'volumeInfo' key exists before accessing 'imageLinks'
            if 'volumeInfo' in book:
                volume_info = book['volumeInfo']
                # Check if 'imageLinks' key exists before accessing 'smallThumbnail'
                if 'imageLinks' in volume_info and 'smallThumbnail' in volume_info['imageLinks']:
                    book_image = volume_info['imageLinks']['smallThumbnail']

            # Calculate aspect ratio (width / height)
            aspect_ratio = book.get('aspectRatio', 1.0)

            image_width = 100  # Set a default width for the node
            image_height = image_width / aspect_ratio  # Calculate height based on aspect ratio

            nodes.append({
                'data': {
                    'id': book_id,
                    'label': book_title,
                    'image': book_image,
                    'type': 'book',
                    'width': image_width,
                    'height': image_height
                }
            })
            edges.append({'data': {'source': author, 'target': book_id}})

    return nodes, edges




@app.route('/network')
def network():
    # Step 1: Get authors and books data from MongoDB
    authors_data = get_authors_and_books()

    # Step 2: Prepare data for Cytoscape.js
    nodes, edges = prepare_data_for_cytoscape(authors_data)

    # Debugging: Print the data to the console
    print("Nodes:", nodes)
    print("Edges:", edges)

    return render_template('network.html', nodes=nodes, edges=edges)



@app.route('/book-search', methods=['POST'])
def book_search():
    query = request.form.get('search_query')
    if query:
        # Use the MongoDB text index to perform the book search
        search_results = collection.find(
            {'$text': {'$search': query}},
            {'score': {'$meta': 'textScore'}}
        ).sort([('score', {'$meta': 'textScore'})])

        return render_template('book-search.html', search_results=search_results)

    return render_template('book-search.html')

@app.route('/book/<book_id>')
def book_review(book_id):
    # Find the book by its _id field in MongoDB
    book_data = collection.find_one({'_id': ObjectId(book_id)})

    if book_data:
        # Pass the book data to the template
        return render_template('book-review.html', book=book_data)
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.teardown_appcontext
def close_connection(exception):
    client.close()

if __name__ == '__main__':
    app.run(debug=True)
