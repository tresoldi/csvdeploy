#!/usr/bin/env python3
# pylint: disable=no-self-use

"""
test_csvdeploy
==============

Tests for the `csvdeploy` package.
"""

# Import Python libraries
from pathlib import Path
import unittest

# Import the library itself
import csvdeploy


class TestCSVDeploy(unittest.TestCase):
    """
    Suite of tests for the package.
    """

    def test_dummy(self):
        assert 1 == 1


if __name__ == "__main__":
    # Explicitly creating and running a test suite allows to profile it
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCSVDeploy)
    unittest.TextTestRunner(verbosity=2).run(suite)
