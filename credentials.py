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