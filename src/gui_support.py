import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def BROWSE():
    print('test_support.BROWSE')
    sys.stdout.flush()
def ONLY_PLATE():
    print('test_support.ONLY_PLATE')
    sys.stdout.flush()
def SHOW_FULL_STEPS():
    print('test_support.SHOW_FULL_STEPS')
    sys.stdout.flush()
def START():
    import product
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
if __name__ == '__main__':
    import test
    test.vp_start_gui()
