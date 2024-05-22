import tkinter as tk

'''
This class is used to create the screen of the application
We need it twice in the application, one for the authentication and one for the main menu
'''

class Screen():
    def __init__(self):
        self.__screen = tk.Tk()
        self.__screen.geometry("900x600")
        self.__width = 900
        self.__height = 600
        self.__canvas = tk.Canvas(self.__screen, width=self.__width, height=self.__height)
        self.__window_canvas = tk.Canvas(self.__screen, width=self.__width, height=self.__height)

    def get_screen(self):
        return self.__screen
    
    def get_canvas(self):
        return self.__canvas

    def get_window_canvas(self):
        return self.__window_canvas
        
    def draw_window_canvas(self):
        self.__window_canvas = tk.Canvas(self.__screen, width = self.__width, height = self.__height - 100)
        self.__window_canvas.pack()

    def destroy_canvas(self):
        self.__canvas.destroy()