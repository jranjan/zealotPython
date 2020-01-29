import unittest


class VsaMultipleClusterTestCase(unittest.TestCase):

    def setUp(self):
        print("VsaMultipleClusterTestCase: setup")

    def tearDown(self):
        print("VsaMultipleClusterTestCase: tearDown")

    @classmethod
    def setUpClass(cls):
        print("VsaMultipleClusterTestCase: setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("VsaMultipleClusterTestCase: tearDownClass")

    def runTest(self):
        print("VsaMultipleClusterTestCase: runTest")
