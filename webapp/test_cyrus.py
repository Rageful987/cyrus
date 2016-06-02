import unittest
from cyrus import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def test_hello(self):
        response = self.test_app.get('/', content_type='html/test')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
