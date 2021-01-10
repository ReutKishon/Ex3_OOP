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

    def __lt__(self, other):
        return self.tag < other.tag

    # def __eq__(self, other):
    #     # if self.tag > other.tag:
    #     #     return self
    #     # elif self.tag < other.tag:
    #     #     return other
    #     # else:
    #     return self.tag == other.tag
