class Node:

    def __init__(self, key, pos: tuple):
        self.key = key
        self.tag = 0
        self.pos = pos

    def __call__(self):
        print('called')

    def set_tag(self, t):
        self.tag = t

    def set_pos(self, pos: tuple):
        self.pos = pos
