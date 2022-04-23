class Cridentials:
    '''
    Class that generates the users cridentials
    '''
    cridential_list = []
    user_cridentials_list = []

    @classmethod
    def check_user(cls,first_name,password:
        # The above 👆 method is for checking if the name and password entered match match entries in the users list

        curre_user = ''
        for user in User.user_list:
            if (user.firstname == firstname and user.password):
                current_user = user.first_name
        return curre_user
    def _init_(self,user_name, site_name, account_name, password):
        # This method defines the properties of each user

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password



    def save_cridential(self):
        '''
        save_cridential method saves a new cridential object to the cridential_list
        '''

        Cridentials.cridential_list.append(self)
        '''
        A method for creating new deails about the user
        '''