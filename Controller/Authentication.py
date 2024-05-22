from Model.User import User
from Controller.UserRepository import UserRepository
import hashlib
import re


''' Class Authentication : 
contains the method authenticate, create_account '''

class Authentication:
    def __init__(self, name=None, mail=None, password=None):
        self.user_repo = UserRepository()
        self.user = User(name, mail, password)


    def authenticate(self, mail, password):
        '''
        method for authentication: check the mail input
        if user exist, check the input password 
        '''
        user_data = self.user_repo.read_user(conditions=f"mail = '{mail}'")

        mail_user = user_data[0][3]
        # if the user exists in the database
        if mail_user == mail :

            # collect the hashed password from the Db
            hashed_password_db = user_data[0][4]

            # Hash the password give by the user 
            password_bytes = password.encode('utf-8')
            hash_password = hashlib.sha256()
            hash_password.update(password_bytes)
            hashed_password_input = hash_password.hexdigest()

            # Compare the hashed password of the db and the one we just hash
            if hashed_password_input == hashed_password_db:
                return True
        else:
            test_connection = "wrong"
            return test_connection


    def email_enter(self, mail):
        '''
        Method for email verification: check if the email is in a valid format
        '''
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_pattern, mail):
            return True
        else:
            return False
        

    def password_enter(self, password):
        '''
        method for password verification: check if the password contains at least 8 characters, 1 uppercase, 1 lowercase, 1 digit and 1 special character
        '''
        autorized_Special_Char = "!@#$%^&*"
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            return False
        return True
    
    def check_existing_name(self, name):
        '''
        method for checking if the name already exists in the database
        '''
        user_data = self.user_repo.read_user(conditions=f"name = '{name}'")
        if user_data:
            return False
        return True
    
    def check_existing_mail(self, mail):
        '''
        method for checking if the mail already exists in the database
        '''
        user_data = self.user_repo.read_user(conditions=f"mail = '{mail}'")
        if user_data:
            return False
        return True
    
    def create_account(self, name, mail, password):
        '''
        method for account creation: check the password input first 
        '''
        check_existing_name = self.check_existing_name(name)
        check_existing_mail = self.check_existing_mail(mail)

        # Step to check if all the conditions are met to create an account
        if check_existing_name == False:
            return 1
        elif check_existing_mail == False:
            return 2
        else:
            check_password = self.password_enter(password)
            check_mail = self.email_enter(mail)
            if check_password == True and check_mail == True:
                self.user_repo.create_user(name, mail, password)
                User(name, mail, password)
                return 5
            else :
                if check_password == False:
                    return 3
                if check_mail == False:
                    return 4
                
    def update_information(self, name, mail, password):
        '''
        method for updating the user information
        '''
        self.user_repo.update_information(name, mail, password)

    def delete_user(self, conditions):
        '''
        method for deleting a user
        '''
        self.user_repo.delete_user(conditions)