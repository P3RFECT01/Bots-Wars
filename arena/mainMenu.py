import curses
from curses import wrapper
from curses import *



def main(mainsrc):
    mainsrc.clear()
    mainsrc.addstr(4,0)
    mainsrc.refresh()
    mainsrc.getch()

wrapper(main)


