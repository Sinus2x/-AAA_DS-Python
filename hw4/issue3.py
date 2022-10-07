import unittest
from ohe import fit_transform


class OneHotEncodeTest(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(TypeError, fit_transform)

    def test_usual_case(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertSequenceEqual(fit_transform(cities), expected)

    def test_one_city(self):
        self.assertIsInstance(fit_transform('Moscow'), list)

    def test_dublicate(self):
        exp = [
            ('Moscow', [1]),
            ('Moscow', [1])
        ]
        self.assertSequenceEqual(fit_transform('Moscow', 'Moscow'), exp)


if __name__ == '__main__':
    log_file = 'result_issue3.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)