import unittest
import pyperclip
from credentials import Credential



class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential class behavior
    '''
    
    def setUp(self):
        '''
        This method should run before each test case
        '''
        self.new_credentials = Credential()

    def tearDown(self):
        '''
        This method clears the credential_list after every test to ensure that there is no error
        '''
        Credential.credential_list = []

    def test_init(self):
        self.assertEqual(self.new_credentials.username, "Bel")
        self.assertEqual(self.new_credentials.site_name, "twitter")
        self.assertEqual(self.new_credentials.account_name, "bel254")
        self.assertEqual(self.new_credentials.password, "passcheck")

    def test_save_credential(self):
        '''
        Method that tests if the new credentials created are saved
        '''
        self.new_credentials.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        Method for saving several credentials to credential_list
        '''
        self.new_credentials.save_credential()
        new_test_credential = Credential()
        new_test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
        self.new_credentials.save_credential()
        new_test_credential = Credential()
        new_test_credential.save_credential()
        # bel_test_credentials = Credential("Myles", "instagram", "mine", "pamine")
        # bel_test_credentials.save_credential()

        self.new_credentials.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)
        
    def test_find_credential_by_name(self):
        '''
        Method for checking  credentials and display information
        '''
        self.new_credentials.save_credential()
        new_test_credential = Credential()
        new_test_credential.save_credential()

        found_credential = Credential.find_by_name("instagram")
        self.assertEqual(found_credential.site_name, new_test_credential.site_name)

    def test_credential_exist(self):
        self.new_credentials.save_credential()
        new_test_credential = Credential()
        new_test_credential.save_credential()

        credential_exist = Credential.credential_exist("pamine")
        self.assertTrue(credential_exist)

    def test_display_all_credentials(self):
        '''
        This method is for the purpose of testing whether all credentials can be displayed
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    def test_copy_password(self):
        self.new_credentials.save_credential()
        Credential.copy_password("account_name")
        self.assertEqual(self.new_credentials.password,pyperclip.paste())








if __name__ == '__main__':
    unittest.main()