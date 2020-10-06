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


dfa1 = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}

dfa2 = {0:{'0':1, '1':2},
       1:{'0':0, '1':2},
       2:{'0':2, '1':1}}


fsm1 = FSM('01', dfa1, 0, {0})
fsm2 = FSM('01', dfa2, 0, {1})

words = ['1011101', '0101', '00101', '11101010', '010101010', '010101010', '1111', '10101010', '101010101110', '010101', '11011001']

def common_words(fsm1, fsm2, word_list):
    if fsm1.alph != fsm2.alph:
        return "alphabets not equal"
    else:
        alph = fsm1.alph
        common = []
        for word in word_list:
            for char in ''.join(set(word)):
                if char not in alph:
                    return 'Words have letters that aren\'t in the alphabet'
            if fsm1.accepts(word) and fsm2.accepts(word):
                common.append(word)
        return min(common)

print(common_words(fsm1, fsm2, words))