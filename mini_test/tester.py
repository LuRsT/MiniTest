# -*- coding: utf-8 -*-

from termcolor import colored
import inspect


class Tester(object):
    successes = 0
    fails     = 0
    log       = {}
    long_log  = {}

    def __init__(self):
        return None

    def do_tests(self, **kwargs):
        """ This will run every method inside the class

        This is used to run the tests from the class inherited by this one,
        hopefully the tests will start with "test", we'll run all of those
        """
        # Reset log
        self.log = {}
        self.long_log = {}

        for name in dir(self):
            if name.startswith('test'):
                self.actual_test = name
                getattr(self, name)()

        if 'verbose' in kwargs.keys() and kwargs['verbose'] is True:
            for test_name in self.log.keys():
                print test_name + ":\n"
                print self.log[test_name]

            print 'Errors:'
            for test_name in self.long_log.keys():
                print test_name + ":"
                print self.long_log[test_name]

            print '#' * 20

        print 'From %d tests:' % (self.successes + self.fails)
        print '  Passed: ' + colored('%d' % self.successes, 'green')
        print '  Failed: ' + colored('%d' % self.fails, 'red')

    def is_(self, logic, result, name=None):
        """ Alias to assertEqual

        This should be the most used method
        """
        return self.assertEqual(logic, result, name)

    def assertEqual(self, first_value, second_value, name=None):
        if name is None:
            name = self.funcname()

        if first_value == second_value:
            return self._success(name)
        else:
            return self._fail(name)

    def assertTrue(self, test, name=None):
        if name is None:
            name = self.funcname()

        if test is True:
            return self._success(name)
        else:
            return self._fail(name)

    def assertRaises(self, exception, method, args=None, name=None):
        if name is None:
            name = self.funcname()

        try:
            method(args)
            return self._fail(name)
        except exception:
            return self._success(name)
            pass
        except:
            return self._fail(name)

    def _success(self, name=None):
        self.successes += 1
        self._log('●', 'green', name)

    def _fail(self, name):
        self.fails += 1
        self._log('○', 'red', name)
        self._long_log(name, 'red')

    def _log(self, result, color, name=None):
        if name is None:
            log_str = colored('%s' % result, color)
        else:
            log_str = colored('%s: %s\n' % (result, name), color)

        try:
            self.log[self.actual_test] += log_str
        except KeyError:
            self.log[self.actual_test] = log_str

    def _long_log(self, name, color):
        log_str = colored('%s failed' % name, color)

        try:
            self.long_log[self.actual_test] += log_str
        except KeyError:
            self.long_log[self.actual_test] = log_str

    def funcname(self):
        """ Returns function name """
        return inspect.stack()[1][3]
