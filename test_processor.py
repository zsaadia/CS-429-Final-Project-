import unittest
import json
from processor import app

class TestProcessor(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_add_documents(self):
        # Test adding documents
        documents = [
            "This is the first document",
            "This document is the second document",
            "And this is the third one",
            "Is this the first document?"
        ]
        response = self.app.post('/add_documents', json={'documents': documents})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Documents added successfully')
        print("\nAdd Documents Test:")
        print("Status Code:", response.status_code)
        print("Response Data:", data)

    def test_process_query(self):
        # Add documents
        documents = [
            "This is the first document",
            "This document is the second document",
            "And this is the third one",
            "Is this the first document?",
        ]
        self.app.post('/add_documents', json={'documents': documents})

        # Test processing queries
        queries = ["document", "second document", "third", "this"]
        for query in queries:
            response = self.app.post('/query', json={'query': query})
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            print("\nProcess Query Test:")
            print("Query:", query)
            print("Status Code:", response.status_code)
            print("Response Data:", data)

    def test_empty_query(self):
        # Test query with empty query
        response = self.app.post('/query', json={'query': ' '})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        print("\nEmpty Query Test:")
        print("Status Code:", response.status_code)
        print("Response Data:", data)

    def test_missing_query_key(self):
    # Test query with missing 'query' key
        response = self.app.post('/query', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Query key is missing in JSON data')
        print("\nMissing Query Key Test:")
        print("Status Code:", response.status_code)
        print("Response Data:", data)

if __name__ == '__main__':
    unittest.main()

