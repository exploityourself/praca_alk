import unittest
from tests.login_test import LogInTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LogInTest)

tests_for_run = [
    login_test,
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)
