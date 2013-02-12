import random
import mini_test

class TestSequenceFunctions(mini_test.Tester):

    def __init__(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10), "Sequence doesn't lose elements")

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3),
                          "Immutable Sequence")

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq, 'Element is in choice')

    def test_sample(self):
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq, 'Element is in sample')

if __name__ == '__main__':
    t = TestSequenceFunctions()
    t.do_tests(verbose=True)
