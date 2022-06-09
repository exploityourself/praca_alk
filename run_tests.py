import unittest
from tests.login_test import LogInTest
from tests.logout_test import LogOutTest
from tests.add_to_cart_test import AddToCartTest
from tests.delete_from_cart_test import DeleteFromCartTest
from tests.place_order_test import PlaceOrderTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
logout_test = unittest.TestLoader().loadTestsFromTestCase(LogOutTest)
add_to_cart_test = unittest.TestLoader().loadTestsFromTestCase(AddToCartTest)
delete_from_cart_test = unittest.TestLoader().loadTestsFromTestCase(DeleteFromCartTest)
place_order_test = unittest.TestLoader().loadTestsFromTestCase(PlaceOrderTest)


tests_for_run = [
    login_test,
    logout_test,
    add_to_cart_test,
    delete_from_cart_test,
    place_order_test,
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)
