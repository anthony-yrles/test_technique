'''
This file is used to store the current state of the menu. It is used to determine which menu is currently being displayed.
'''


state = False

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state