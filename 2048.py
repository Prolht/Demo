import curses
from random import randrange,choice
from collections import defaultdict

actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes,actions*2))

def main(stdscr):
    def init():
        return 'Game'
    def not_game(state):
        #draw gameover or win 
        # read user's input to restart or exit
        responses = defaultdict(lambda:state) ＃默认是当前状态，没有行为就会一直在当前界面循环
        
