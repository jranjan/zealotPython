import unittest
from vsacloud import vsa_service as hlmvsa
from vsacloud import vsalm_single_cluster as vsalm_singlecluster


if '__main__' == __name__:
    suite1 = hlmvsa.get_happy_qual_sutie()
    suite2 = vsalm_singlecluster.get_happy_qual_sutie()
    all_tests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(all_tests)

