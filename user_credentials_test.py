import unittest
# import pyperclip
from user import User
from credentials import Credential

class TestUser(unittest.TestCase):
    # The above 👆 is a test class that defines test cases for the user class behavior.

    # Args:
    # unittest.TestCase: it helps in creating test cases

    def setUp(self):
        # '''
        # Function for creating a user acc before each test
        # '''

        self.new_user = User("Belinda", "Ntinyari", "pass254")

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

class TestCredential(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credential("Bel", "twitter", "bel254", "passcheck" )

    def test_credentials_instance(self):
        self.assertEqual(self.new_credentials.user_name, "Bel")
        self.assertEqual(self.new_credentials.site_name, "twitter")
        self.assertEqual(self.new_credentials.account_name, "bel254")
        self.assertEqual(self.new_credentials.password, "passcheck")

    def test_save_credential(self):
        self.new_credentials.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        self.new_credentials.save_credential()
        new_test_credential = Credential("Myles", "instagram", "mine", "pamine")
        new_test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
        Credential.credential_list = []
        
    def test_find_credential_by_name(self):
        self.new_credentials.save_credential()
        new_test_credential = Credential("Myles", "instagram", "mine", "pamine")
        new_test_credential.save_credential()

        found_credential = Credential.find_by_name("instagram")
        self.assertEqual(found_credential.account_name, new_test_credential.site_name)

    def test_display_all_credentials(self):
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)








if __name__ == '__main__':
    unittest.main()