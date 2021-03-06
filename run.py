#!/usr/bin/env python3.8
from credentials import Credential

def create_new_credential(username,site_name,account_name,password):
    '''
    Function to create new credentials for preffered site
    '''
    new_credentials = Credential(username,site_name,account_name,password)
    return new_credentials

def save_new_credential(credentials):
    '''
    Function to save newly created credentials
    '''
    Credential.save_credential(credentials)

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    Credential.delete_credential(credential)

def find_credential(name):
    '''
    Function that finds a credential by name and returns the credential
    '''
    return Credential.find_by_name(name)

def check_existing_credentials(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return Credential.credential_exist(name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def copy_password(name):
    return Credential.copy_password(name)

def main():
    print("Hello Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create new credentials, dc - display credentials, fc -find a name, del - delete credential, cp - copy password,  ex -exit the password locker ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print ("username ....")
            username = input()

            print("site_name ...")
            site_name = input()

            print("account_name ...")
            account_name = input()

            print("password ...")
            password = input()


            save_new_credential(create_new_credential(username,site_name,account_name,password)) # create and save new credentials.
            print(create_new_credential(username,site_name,account_name,password))
            print ('\n')
            print(f"New credentials {username} {site_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for Credential in display_credentials():
                            print(f"{Credential.username} {Credential.site_name} {Credential.account_name} {Credential.password}")

                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == 'fc':

                print("Enter the name you want to search for")

                search_name = input()
                if check_existing_credentials(search_name):
                        search_credential = find_credential(search_name)
                        print(f"{search_credential.username} {search_credential.password}")
                        print('-' * 20)

                        print(f"Username.......{search_credential.username}")
                        print(f"password.......{search_credential.password}")
                else:
                        print("That credential does not exist")

        elif short_code == 'del':
                print("Enter the credential you want to delete")

                delete_credential = input()
                if check_existing_credentials(delete_credential):
                    delete_credential = find_credential(delete_credential)
                    del_credential(delete_credential)
                    print("Credential deleted successfully")
                else:
                    print("The credential does not exist")

        elif short_code == 'cp':
            print("Enter the credential you want to copy")

            search_account = input()
            if check_existing_credentials(search_account):
                returned_credential = find_credential(search_account)
                copy_password(returned_credential.site_name)
                print("password copied successfully")
            else:
                print("password does not exist")


                




        elif short_code == "ex":
                print(f"Bye {user_name}")
                break
        else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()

    
