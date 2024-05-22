from current_render import *
from View.RenderAuthentication import RenderAuthentication

'''
You have to change your password for the database in the file Model/RequestDb.py
'''

auth = RenderAuthentication()
set_state(auth.render_main_menu)

try : 
    running = True
    
    while running :
        get_state()()
    
except Exception as e:
    print(f"Error: {e}")

