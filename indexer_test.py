import unittest
from indexer import Indexer

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