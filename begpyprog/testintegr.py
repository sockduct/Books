import unittest
import integr
from BadInput import BadInput

class TestIntegr(unittest.TestCase):
    def setup(self):
        # setup is called *before* each test is run
        # if I need to adjust to a well known state
        # before starting
        pass
        
    def teardown(self):
        # teardown is called *after* the each test
        # is run
        pass
        
    def test_basic(self):
        # any method beginning with "test" is a test
        results = integr.parse('1,3,4')
        self.assertEquals(results, [1,3,4])

    def test_spaces(self):
        results = integr.parse('1, 3, 4')
        self.assertEquals(results, [1,3,4])

    def test_bad(self):
        self.assertRaises(BadInput, integr.parse, 'abcd')

    def test_bad2(self):
        try:
            integr.parse('abcd')
            self.fail('Parsed bad input')
        except BadInput:
            pass

    # Python 2.7+
    def test_bad3(self):
        with self.assertRaises(BadInput):
            integr.parse('abcd')

if __name__ == '__main__':
    unittest.main()

