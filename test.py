from app import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

class test(TestBase):
    def test_one(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)