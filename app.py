from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
from bson import json_util  
import pymongo
import os
import ast

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)
db = client['test']
collection = db['movies']
movies = pd.DataFrame(list(collection.find()))
movies['plot_embedding'] = movies['plot_embedding'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = SentenceTransformer('all-mpnet-base-v2')

@app.route("/", methods=['GET'])
def home():
    return "Welcome World"

@app.route('/search', methods=['POST'])
def get_movies():
    try:
        # Retrieve the JSON data sent by the client
        data = request.get_json()
        userQuery = [data.get('search')]
        if not userQuery:
            raise ValueError("No search query provided.")
        
        # Compute embedding for the user's query
        userQuery_embedding = model.encode(userQuery)
        similarities = cosine_similarity(userQuery_embedding, np.vstack(movies['plot_embedding'].values))
        
        # Get top 5 most similar movies
        top_n = 5
        top_indices = np.argsort(similarities[0])[::-1][:top_n]
        
        # Get the top movie details and ensure ObjectId is converted to string
        top_movies = movies.iloc[top_indices].to_dict(orient='records')
        for movie in top_movies:
            movie['_id'] = str(movie['_id'])  # Convert ObjectId to string
        
        return jsonify(top_movies), 200
    
    except Exception as e:
        # Return the error message with a 400 status code
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))