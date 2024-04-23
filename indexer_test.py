import unittest
from indexer import Indexer

class TestIndexer(unittest.TestCase):
    def setUp(self):
        # Initialize the indexer
        self.indexer = Indexer()

        # Add sample documents to the indexer
        self.indexer.add_document(1, "The quick brown fox jumps over the lazy dog")
        self.indexer.add_document(2, "A brown fox is quick and jumps over a lazy dog")
        self.indexer.add_document(3, "The lazy cat sleeps all day")
        self.indexer.add_document(4, "A quick cat jumps over a lazy dog")

        # Build the index
        self.indexer.build_index()

    def test_search_queries(self):
        # Sample queries and expected results
        queries = ["brown fox", "lazy cat", "quick cat", "sleeps all day", "fox jumps", "quick lazy", "dog lazy"]
        expected_results = [
            [(1, 0.8962, 0.4481), (2, 0.7918, 0.3959)],
            [(3, 1.0000, 0.5000)],
            [(4, 0.6671, 0.3336)],
            [(3, 0.7918, 0.3959)],
            [(1, 0.8962, 0.4481), (2, 0.7918, 0.3959)],
            [(2, 0.6728, 0.3364), (1, 0.6053, 0.3026)],
            [(1, 0.7071, 0.3536), (2, 0.6325, 0.3162)]
        ]

        # Perform searches and verify results
        for query, expected_result in zip(queries, expected_results):
            with self.subTest(query=query):
                results = self.indexer.search(query)
                self.assertEqual(len(results), len(expected_result))
                for i, (doc_id, cosine_sim, tfidf_score) in enumerate(results):
                    self.assertEqual(doc_id, expected_result[i][0])
                    self.assertAlmostEqual(cosine_sim, expected_result[i][1], places=4)
                    self.assertAlmostEqual(tfidf_score, expected_result[i][2], places=4)

if __name__ == '__main__':
    unittest.main()