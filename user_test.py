import unittest
import pyperclip
import user from User


class TestUser(unittest.TestCase):
    # The above 👆 is a test class that defines test cases for the user class behavior.

    # Args:
    # unittest.TestCase: it helps in creating test cases

    def setUp(self):
        # '''
        # Function for creating a user acc before each test
        # '''

        self.new_user = User("Belinda", "Ntinyari", "pass254")

    def tearDown(self):
        User.user_list = []

    def test_init(self):
        # '''
        # Test done to check if creation of new user was successfully done
        # '''

        self.assertEqual(self.new_user.first_name, "Belinda")
        self.assertEqual(self.new_user.last_name, "Ntinyari")
        self.assertEqual(self.new_user.password, "pass254")

    def test_save_user(self):
        # '''
        # making sure the object is initialized properly
        # '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)