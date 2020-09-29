import unittest
from Solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_simplifyPart(self):
        self.assertEqual(self.sol.simplifyPart("(1+2)"), "3")
        self.assertEqual(self.sol.simplifyPart("(-9+11+1-5)"), "-2")

    def test_calculate(self):
        self.assertEqual(self.sol.calculate("1 + 1"), 2)
        self.assertEqual(self.sol.calculate("2-1 + 2"), 3)
        self.assertEqual(self.sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

if __name__ == "__main__":
    unittest.main()
