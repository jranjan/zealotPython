import unittest
from vsa_service import VsaServiceTestCase


class VsaSingleClusterTestCase(VsaServiceTestCase):

    def test_01_create_cluster(self):
        print("VsaSingleClusterTestCase: test_01_create_cluster")

    def test_02_exapnd_cluster(self):
        print("VsaSingleClusterTestCase: test_02_exapnd_cluster")

    def test_03_shrink_cluster(self):
        print("VsaSingleClusterTestCase: test_03_shrink_cluster")

    def test_04_delete_cluster(self):
        print("VsaSingleClusterTestCase: test_04_delete_cluster")


def get_happy_qual_sutie():
    hq = unittest.TestSuite()
    hq.addTest(VsaSingleClusterTestCase('test_01_create_cluster'))
    hq.addTest(VsaSingleClusterTestCase('test_02_exapnd_cluster'))
    hq.addTest(VsaSingleClusterTestCase('test_03_shrink_cluster'))
    hq.addTest(VsaSingleClusterTestCase('test_04_delete_cluster'))
    return hq
