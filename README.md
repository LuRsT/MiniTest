MiniTest
========

Minimalistic Python Test Framework

#### ALERT: Done for education purposes only ATM, use at your own risk

## Requirements

termcolor

## How to use?

It's very similar to Python's unittest, create a class that inherits from `Tester`, create various methods to test anything, note that to test something, 

Check the `example.py` file

### Mini example:

    import mini_test

    class new_test(mini_test.Tester):
        def test_sum(self):
            self.assertEqual(1 + 1, 2)

    if __name__ == '__main__':
        t = new_test()
        t.do_tests()

## Roadmap

* ~~Suites~~
