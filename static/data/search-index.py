from pymongo import MongoClient
from pymongo.operations import IndexModel

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Choose the database and collection where you want to create the text index
db = client['king-bachman']
collection = db['king-bachman']

# Create the text index on the fields you want to search
index_fields = [
    ('volumeInfo.title', 'text'),
    ('volumeInfo.authors', 'text'),
    ('volumeInfo.description', 'text'),
    ('searchInfo.textSnippet', 'text'),
    ('volumeInfo.subtitle', 'text'),
    ('volumeInfo.industryIdentifiers.identifier', 'text'),  # This will index both ISBN_10 and ISBN_13
]
collection.create_indexes([IndexModel(fields, name='_text_index') for fields in index_fields])
