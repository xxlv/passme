import unittest


from adapters import github
class TestGithub(unittest.TestCase):

    def setUp(self):
        self.adapter=github.Github()


    def tearDown(self):
        pass


    def test_authenticity_token_found(self):
        sess=self.adapter.initSession()
        self.assertEqual(len(sess.get('authenticity_token')),88)
