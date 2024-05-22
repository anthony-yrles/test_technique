from View.Entry import CustomEntry
from View.Screen import Screen
from View.Image import Image
from View.Button import Button
from Controller.Authentication import Authentication
from current_render import *
from tkinter import messagebox

'''
This class is responsible for rendering the authentication page
'''

class RenderAuthentication:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        self.custom_entries = []
        self.authentication = Authentication()

    def get_screen_object(self):
        return self.screen_object

    def draw_canvas(self):
        self.screen_object.get_canvas().pack()
    
    #First page of the application where you can chose to sign in or log in 
    def render_main_menu(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_menu.png')
        self.draw_canvas()
        background_image.draw()

        sign_in_button = Button(self.canvas, 50, 500, './assets/sign_in_button.png', None)
        sign_in_button.bind('<Button-1>', lambda event: self.render_sign_in())

        log_in_button = Button(self.canvas, 580, 500, './assets/log_in_button.png', None)
        log_in_button.bind('<Button-1>', lambda event: self.render_log_in())

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    #Check if the password is valid and create the account in the database
    def check_sign_in(self, entry1, entry3, entry4):
        name = entry1.get_value()
        email = entry3.get_value()
        password = entry4.get_value()

        validation_create_account = self.authentication.create_account(name, email, password)

        # Step to render error message if the conditions of creation are not meet. If all the conditions are meet back to the log in page
        if validation_create_account == 1:
            messagebox.showerror("Error", "Name already used")
        elif validation_create_account == 2:
            messagebox.showerror("Error", "Email already used")
        elif validation_create_account == 3:
            messagebox.showerror("Error", "Your password have to contain at least 8 characters, 1 uppercase, 1 lowercase, 1 number and 1 special character")
        elif validation_create_account == 4:
            messagebox.showerror("Error", "Your Email is not an email adress")
        elif validation_create_account == 5:
            messagebox.showinfo("Success", "Your account has been created")
            self.render_log_in()

        self.screen_object.get_screen().mainloop()
        self.canvas.update()
                       
    #Render the sign in page with the inputs
    def render_sign_in(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_sign_menu.png')
        background_image.draw()

        entry1 = CustomEntry(self.canvas, "Name", x=300, y=141)
        entry3 = CustomEntry(self.canvas, "Email", x=300, y=293)
        entry4 = CustomEntry(self.canvas, "Password", x=300, y=369, show='*')


        self.custom_entries.extend([entry1, entry3, entry4])

        real_sign_in_button = Button(self.canvas, 330, 450, './assets/sign_in_button_page.png', None)
        real_sign_in_button.bind('<Button-1>', lambda event: self.check_sign_in(entry1, entry3, entry4))
        
        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    
    #Check if the email and password are correct and destroy the actual window to render the budget menu
    def check_authenticate(self, entry5, entry6):
        email = entry5
        password = entry6
        test_connection = self.authentication.authenticate(email, password)
        if test_connection:
            self.render_change_information()
        else:
            messagebox.showerror("Error", "Email or password invalide")

    #Render the log in page with the inputs
    def render_log_in(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_log_menu.png')
        background_image.draw()

        entry5 = CustomEntry(self.canvas, "Email", x=300, y=195)
        entry6 = CustomEntry(self.canvas, "Password", x=300, y=283, show='*')

        self.custom_entries.extend([entry5, entry6])

        real_log_in_button = Button(self.canvas, 340, 360, './assets/log_in_button_page.png', None)
        real_log_in_button.bind('<Button-1>', lambda event: self.check_authenticate(entry5.get_value(), entry6.get_value()))

        new_here_button = Button(self.canvas, 485, 452, './assets/sign_in_button_log_page.png', None)
        new_here_button.bind('<Button-1>', lambda event : self.render_sign_in())

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_change_information(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        entryName = CustomEntry(self.canvas, "Name", x=300, y=141)
        entryEmail = CustomEntry(self.canvas, "Email", x=300, y=293)
        entryBio = CustomEntry(self.canvas, "Bio", x=300, y=369)

        update_button = Button(self.canvas, 330, 450, './assets/update_button.png', None)
        delete_button = Button(self.canvas, 330, 500, './assets/delete_button.png', None)
        deconnexion_button = Button(self.canvas, 330, 550, './assets/disconnect_button.png', None)

        update_button.bind('<Button-1>', lambda event: self.update_information(entryName.get_value(), entryEmail.get_value(), entryBio.get_value()))
        delete_button.bind('<Button-1>', lambda event: self.delete_user())
        deconnexion_button.bind('<Button-1>', lambda event: self.render_main_menu())


