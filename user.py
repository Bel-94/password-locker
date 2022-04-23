class User:
    '''
    This is the class that generates new user
    '''
    user_list = []

    def _init_(self, first_name, last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves a new user object to the user_list
        '''

        User.user_list.append(self)
        '''
        The append method is for adding new username or password that the user may create
        '''