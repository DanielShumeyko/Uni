class FSM:
    def __init__(self, alphabet,transitions, initial, final):
        self.alph = alphabet
        self.trans = transitions
        self.ini = initial
        self.fin = final
    def accepts(self, line):
        state=self.ini
        for char in line:
            state = self.trans[state][char]
        return state in self.fin


dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}

fsm1 = FSM('01', dfa, 0, {0})

print(fsm1.accepts('1011101'))
print(fsm1.accepts('10111011'))