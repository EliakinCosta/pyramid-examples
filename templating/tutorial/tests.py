import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import hello

        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual('Hello View', response['name'])


class TutorialFunctionalTests(unittest.TestCase):

    def setUp(self):
        from tutorial import  main
        app = main({})
        from webtest import TestApp

        self.test_app = TestApp(app)

    def test_home(self):
        response = self.test_app.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', response.body)

    def test_hello(self):
        response = self.test_app.get('/howdy', status=200)
        self.assertIn(b'<h1>Hi Hello View', response.body)
