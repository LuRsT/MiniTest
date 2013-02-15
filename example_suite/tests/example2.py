import mini_test


class TestBasic(mini_test.Tester):
    def __init__(self):
        return None

    def test_addition(self):
        self.assertEqual(1+1, 2)

    def test_subtraction(self):
        self.assertEqual(1-1, 1)
        self.assertEqual(5-1, 4)
