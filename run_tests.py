import unittest
from tests.log_in_test import LogInTest

# Pobierz testy, które chcesz uruchomić
login_test = unittest.TestLoader().loadTestsFromTestCase(LogInTest)

# Lista testów do uruchomienia
tests_for_run = [
    login_test,
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)
