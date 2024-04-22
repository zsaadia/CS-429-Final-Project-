import requests

# Function to add documents to the Flask application
def add_documents(documents):
    url = 'http://127.0.0.1:5000/add_documents'
    response = requests.post(url, json={'documents': documents})
    return response

# Function to make queries to the Flask application
def process_query(query):
    url = 'http://127.0.0.1:5000/query'
    response = requests.post(url, json={'query': query})
    return response

# Add documents to the Flask application
documents = [
    "This is the first document",
    "This document is the second document",
    "And this is the third one",
    "Is this the first document?"
]
add_documents_response = add_documents(documents)
print("Documents added successfully")

# Make queries to the Flask application
queries = ["document", "second document", "third", "this"]
for query in queries:
    response = process_query(query)
    print("Query:", query)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, "-", response.text)