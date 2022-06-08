import unittest
from tests.login_test import LogInTest
from tests.add_to_cart_test import AddToCartTest
from tests.delete_from_cart_test import DeleteFromCartTest
from tests.place_order_test import PlaceOrderTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
add_to_card_test = unittest.TestLoader().loadTestsFromTestCase(AddToCartTest)
delete_from_card_test = unittest.TestLoader().loadTestsFromTestCase(DeleteFromCartTest)
place_order_test = unittest.TestLoader().loadTestsFromTestCase(PlaceOrderTest)


tests_for_run = [
    login_test,
    add_to_card_test,
    delete_from_card_test
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    # Uruchom testy
    unittest.main()