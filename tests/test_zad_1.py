import unittest

from sample.zad_1 import IsPangram
from parameterized import parameterized

class TestZad1(unittest.TestCase):
    def setUp(self):
        self.tmp = IsPangram()

    def test_from_file(self):
        fileTest = open("data/zad_1_test_data")

        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split("|")
                inp, result = data[0], data[1].strip("\n")
                self.assertEqual(self.tmp.pangram(inp), result)

        fileTest.close()

    @parameterized.expand([
        ("Pack my box with five dozen liquor jugs", 'To pangram'),
        ("Jived fox nymph grabs quick waltz.", 'To pangram'),
        ("How vexingly quick daft zebras jump!", 'To pangram'),
        ("Pack", 'To nie pangram'),
        ("quick waltz.", 'To nie pangram'),
    ])
    def test_is_pangram(self, inp, exp):
        self.assertEqual(self.tmp.pangram(inp), exp)


if __name__ == '__main__':
    unittest.main()
