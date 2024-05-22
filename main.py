from current_render import *
from View.RenderAuthentication import RenderAuthentication

auth = RenderAuthentication()
set_state(auth.render_main_menu)

try : 
    running = True
    
    while running :
        get_state()()
    
except Exception as e:
    print(f"Error: {e}")

