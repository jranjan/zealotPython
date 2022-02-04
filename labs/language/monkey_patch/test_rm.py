#!/usr/playbooks/env python
# -*- coding: utf-8 -*-

from myrm import rm

import mock
import unittest


class RmTestCase(unittest.TestCase):
    @mock.patch('myrm.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
