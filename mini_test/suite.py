class Suite(object):
    def __init__(self):
        return None

    def run(self, **kwargs):
        for m in dir(self.tests_module):
            if m.startswith('Test'):
                print "\nTesting %s\n" % m
                test = getattr(self.tests_module, m)()
                test.do_tests(**kwargs)
