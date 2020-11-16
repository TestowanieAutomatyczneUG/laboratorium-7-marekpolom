import unittest

from sample.zad_1 import IsPangram

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


if __name__ == '__main__':
    unittest.main()
