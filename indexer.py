import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.inverted_index = {}
        self.documents = []

    def add_document(self, doc_id, text):
        self.documents.append(text)
        doc_index = len(self.documents) - 1
        for term in set(text.split()):
            if term not in self.inverted_index:
                self.inverted_index[term] = []
            self.inverted_index[term].append((doc_id, doc_index))

    def build_index(self):
        tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        self.tfidf_matrix = tfidf_matrix

    def save_index(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.inverted_index, self.tfidf_matrix), file)

    def load_index(self, filename):
        with open(filename, 'rb') as file:
            self.inverted_index, self.tfidf_matrix = pickle.load(file)

    def search(self, query, k=5):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        # Retrieve TF-IDF scores for the query
        query_tfidf_scores = query_vector.toarray().flatten()
        doc_scores = [(doc_id, cosine_score, tfidf_score) for doc_id, (cosine_score, tfidf_score) in enumerate(zip(cosine_similarities, query_tfidf_scores))]
        doc_scores.sort(key=lambda x: x[1], reverse=True)
        return doc_scores[:k]

# Initialize the indexer
indexer = Indexer()

# Add some documents to the indexer
indexer.add_document(1, "This is the first document")
indexer.add_document(2, "This document is the second document")
indexer.add_document(3, "And this is the third one")
indexer.add_document(4, "Is this the first document?")

# Build the index
indexer.build_index()

# Perform searches
queries = ["document", "second document", "third", "this"]
for query in queries:
    results = indexer.search(query)
    print(f"Search results for query '{query}':")
    for doc_id, cosine_sim, tfidf_score in results:
        print(f"Document ID: {doc_id+1}, Cosine Similarity: {cosine_sim:.4f}, TF-IDF Score: {tfidf_score:.4f}")

# Print TF-IDF matrix
print("\nTF-IDF Matrix:")
print(indexer.tfidf_matrix.toarray())