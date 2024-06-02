import unittest

class TestFileFail(unittest.TestCase):

    def test_fail(self):
        self.fail("This is a failed test")