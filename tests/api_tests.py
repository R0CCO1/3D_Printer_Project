import unittest
import api
import json

class TestCRUDAPI(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_no_job(self):
        results = self.app.get('/get_jobs')
        result = json.loads(results.data)
        self.assertEqual([], result)

    def test_one_job(self):
        results=self.app.get('/get_jobs')
        result=json.loads(results.data)
        self.assertEqual([{'filename': 'ball.text',
                        'details': {'printer': 'gutenberg', 'starttime': '10:10', 'endtime': '12:10', 'status': 'Success'}}],result)


