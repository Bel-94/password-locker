class Credential:
    # '''
    # Class that generates the users cridentials
    # '''
    credential_list = []

    def _init_(self, user_name, site_name, account_name, password)

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password



    def save_credential(self):
        '''
        save_cridential method saves a new cridential object to the cridential_list
        '''

        Cridentials.cridential_list.append(self)
        '''
        A method for creating new deails about the user
        '''

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,site_name):
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def credential_exist(cls,name):
        for credential in cls.credential_list:
            if credential.site_name == name:
                return True 
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credential_list