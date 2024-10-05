# Movie Plot Search API

This project is a Flask-based web service that allows users to search for movies based on plot descriptions. The system uses the `SentenceTransformer` model to encode the user's search query and compares it to pre-stored movie plot embeddings in a MongoDB database. The result is a list of the top 5 most similar movies based on the input query.

## Features

- **Search by Plot:** Allows users to search for movies by describing their plot.
- **AI-Powered:** Uses the `all-mpnet-base-v2` model from `SentenceTransformer` to generate embeddings for both the user query and movie plots.
- **MongoDB Integration:** Stores movie data including plot embeddings in MongoDB.
- **Cosine Similarity:** Measures the similarity between the user's query and movie plots using cosine similarity.
- **CORS Support:** Enables cross-origin resource sharing for frontend applications.

## Prerequisites

Ensure that you have the following tools installed:

- Python 3.8 or later
- MongoDB
- Pip (Python package manager)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OldAlexhub/moviespy.git
   cd movie-plot-search
   ```
