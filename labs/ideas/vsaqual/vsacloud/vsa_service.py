import unittest


class VsaServiceTestCase(unittest.TestCase):

    def setUp(self):
        print("VsaServiceTestCase: setup")

    def tearDown(self):
        print("VsaServiceTestCase: tearDown")

    @classmethod
    def setUpClass(cls):
        print("VsaServiceTestCase: setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("VsaServiceTestCase: tearDownClass")

    def test_00_publish_pre_deployment_report(self):
        print("VsaServiceTestCase: test_00_publish_pre_deployment_report")

    def test_01_deploy(self):
        print("VsaServiceTestCase: test_01_deploy")

    def test_02_service_public_playbooks(self):
        print("VsaServiceTestCase: test_02_run_public_playbook")

    def test_03_upgrade(self):
        print("VsaServiceTestCase: test_03_upgrade")

    def test_04_playbook_idempotency(self):
        print("VsaServiceTestCase: test_04_playbook_idempotency")

    def test_05_cmc_public_playbook(self):
        print("VsaServiceTestCase: test_05_cmc_public_playbook")

    def test_06_cmc_upgrade(self):
        print("VsaServiceTestCase: test_06_cmc_upgrade")


def get_happy_qual_sutie():
    hq = unittest.TestSuite()
    hq.addTest(VsaServiceTestCase('test_00_publish_pre_deployment_report'))
    hq.addTest(VsaServiceTestCase('test_01_deploy'))
    hq.addTest(VsaServiceTestCase('test_02_service_public_playbooks'))
    hq.addTest(VsaServiceTestCase('test_03_upgrade'))
    hq.addTest(VsaServiceTestCase('test_04_playbook_idempotency'))
    hq.addTest(VsaServiceTestCase('test_05_cmc_public_playbook'))
    hq.addTest(VsaServiceTestCase('test_06_cmc_upgrade'))
    return hq

