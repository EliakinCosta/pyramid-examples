import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.matchdict['first'] = 'First'
        request.matchdict['last'] = 'Last'
        inst = TutorialViews(request)
        response = inst.home()
        self.assertEqual('First', response['first'])
        self.assertEqual('Last', response['last'])


class TutorialFunctionalTests(unittest.TestCase):

    def setUp(self):
        from tutorial import  main
        app = main({})
        from webtest import TestApp

        self.test_app = TestApp(app)

    def test_home(self):
        response = self.test_app.get('/howdy/First/Last', status=200)
        self.assertIn(b'First', response.body)
        self.assertIn(b'Last', response.body)
