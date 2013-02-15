import mini_test
import tests
from .tests import *


class ExampleSuite(mini_test.Suite):

    def __init__(self):
        self.tests_module = tests
        return None
