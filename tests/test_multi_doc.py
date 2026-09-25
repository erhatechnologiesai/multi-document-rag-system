import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestMultiDocRAG(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_list_docs(self):
        res = self.client.get("/documents")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["total"], 4)

    def test_cross_doc_query(self):
        res = self.client.post("/query", json={"question": "What is the policy on vacation days?", "filter_type": "all"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("hr_policy.md", res.json()["answer"])

if __name__ == "__main__":
    unittest.main()
