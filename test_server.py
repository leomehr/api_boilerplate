import unittest
import requests

URL = 'http://127.0.0.1:8000'

class TestServer(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(requests.get(URL + '/hello').json(), {'msg': 'Hello! 👋', 'ok': True})

    def test_msg(self):
        self.assertEqual(requests.get(URL + '/msg').status_code, 404)
        self.assertEqual(requests.get(URL + '/msg/hello').json(), {'msg': 'Hello! 👋', 'ok': True})
        self.assertEqual(requests.get(URL + '/msg/none').json(), {'msg': '', 'ok': False})

    def test_msgs(self):
        self.assertEqual(requests.get(URL + '/msgs?limit=0').json(), {})
        self.assertEqual(requests.get(URL + '/msgs?limit=1').json(), {'hello': 'Hello! 👋'})
        self.assertEqual(requests.get(URL + '/msgs').json(), {'hello': 'Hello! 👋'})

    def test_update_hello(self):
        self.assertEqual(requests.put(URL + '/update_hello?new_hello=Hi!').json(), {'ok': True})
        self.assertEqual(requests.get(URL + '/hello').json(), {'msg': 'Hi!', 'ok': True})

    def test_new_greeting(self):
        self.assertEqual(requests.get(URL + '/msg/test').json(), {'msg': '', 'ok': False})
        self.assertEqual(requests.post(URL + '/new_greeting', json={'name': 'test', 'msg': 'Yes!'}).json(), {'ok': True})
        self.assertEqual(requests.get(URL + '/msg/test').json(), {'msg': 'Yes!', 'ok': True})
        self.assertEqual(requests.post(URL + '/new_greeting', json={'name': 'test', 'msg': 'Yes!'}).json(), {'ok': False})

if __name__ == '__main__':
    unittest.main()
