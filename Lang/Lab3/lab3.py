alph_empty=' \n\t' #spacing symbols
alph_decimal = '0123456789' # decimal numbers
alph_hexa = '0123456789ABCDEFabcdef' #hexadecimal numbers
alph_hexa_letters = 'ABCDEFabcdef'
alph_operator = '+-*/=%|&^><~!' #operators
alph_word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789'
alph_dividers = '}{)(][,:.' #dividing symbols
alph_str = ["'",'"'] # strings 
reserved ="""and except lambda with as finally nonlocal while assert False None yield break for not class 
from or continue global pass def if raise del import return elif in True else is try""".split() # list of reserved words

def parse_words(inp_str):
    q=0 #initial state
    last_token = ''
    last_class = ''
    tokens = []
    classes = []
    first_iter = True
    for letter in inp_str:
        if q == 0:
            if not first_iter:
                if last_token not in ['','\n','\t']:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                last_token = ''
                last_class = ''
            first_iter = False
            if letter in alph_operator:
                q=1
                last_class = 'operator' 
            elif letter in alph_decimal:
                q=3
                last_class = 'decimal number'
            elif letter in alph_hexa_letters:
                q=7
                last_class = 'hexadecimal number'
            elif letter in alph_dividers:
                last_class = 'dividing symbol'
            elif letter is '#':
                q=6
                last_class = 'comment'
            elif letter in alph_word:
                q=8
                last_class = 'word'
            elif letter in alph_str:
                q=10
                last_class = 'String constant'
            else:
                last_class = 'unknown token - unknown symbol'

        elif q==1: #assume operator
            if letter in alph_empty:
                q=0 
            elif letter not in alph_operator:
                tokens.append(last_token)
                classes.append('operator')
                last_token = ''
                if letter in alph_decimal:
                    q=3
                    last_class = 'decimal number'
                elif letter in alph_hexa_letters:
                    q=7
                    last_class = 'hexadecimal number'
                elif letter in alph_dividers:
                    last_class = 'dividing symbol'
                elif letter is '#':
                    q=6
                    last_class = 'comment'
                elif letter in alph_word:
                    q=8
                    last_class = 'word'
                elif letter in alph_str:
                    q=10
                    last_class = 'String constant'
                else:
                    last_class = 'unknown token - unknown symbol'            

        elif q==2: #error case 
            if letter in alph_empty:
                q=0

        elif q==3: #assume decimal
            if letter is '.':
                q=5
                last_class ='float'
            elif letter in alph_hexa_letters:
                q=4
                last_class='hexadecimal number'
            elif letter in alph_empty:
                q=0
            elif letter not in alph_decimal:
                if letter in alph_operator:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'operator'
                    q=1
                elif letter in alph_dividers:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'divider'
                    q=0
                else:
                    q=2
                    last_class='unknown token - incorrect number'

        elif q==4: #assume hexadecimal
            if letter in alph_empty:
                q=0
            elif letter not in alph_hexa:
                if letter in alph_operator:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'operator'
                    q=1
                elif letter in alph_dividers:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'divider'
                    q=0
                else:
                    q=2
                    last_class='unknown token - incorrect hexadecimal'

        elif q==5: #assume floating point
            if letter in alph_empty:
                q=0
            elif letter not in alph_decimal:
                if letter in alph_operator:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'operator'
                    q=1
                elif letter in alph_dividers:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'divider'
                    q=0
                else:
                    q=2
                    last_class = 'unknown token - incorrect float'

        elif q==6: #comment
            if letter == '\n':
                q=0

        elif q==7: #assume hexa OR word
            if letter in alph_empty:
                q=0
            elif letter not in alph_hexa:
                if letter in alph_word:
                    q=8
                    last_class='word'
                else:
                    if letter in alph_operator:
                        tokens.append(last_token.strip())
                        classes.append(last_class)
                        last_token = ''
                        last_class = 'operator'
                        q=1
                    elif letter in alph_dividers:
                        tokens.append(last_token.strip())
                        classes.append(last_class)
                        last_token = ''
                        last_class = 'divider'
                        q=0
                    else:
                        q=2
                        last_class = 'unknown token - incorrect hexadecimal'

        elif q==8:# assume word
            if letter in alph_empty:
                q=0
            elif letter not in alph_word:
                if letter in alph_dividers:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = letter
                    last_class = 'divider'
                else:
                    if letter in alph_operator:
                        tokens.append(last_token.strip())
                        classes.append(last_class)
                        last_token = ''
                        last_class = 'operator'
                        q=1
                    elif letter in alph_dividers:
                        tokens.append(last_token.strip())
                        classes.append(last_class)
                        last_token = ''
                        last_class = 'divider'
                        q=0
                    else:
                        q=2
                        last_class= 'unknown token - unknown symbol'

        elif q==9: #dividers
            pass
        elif q==10: #string begins
            if letter in alph_str:
                q=11
        elif q==11: #string end - expect empty symbol
            if letter in alph_empty:
                q=0
            else:
                if letter in alph_operator:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'operator'
                    q=1
                elif letter in alph_dividers:
                    tokens.append(last_token.strip())
                    classes.append(last_class)
                    last_token = ''
                    last_class = 'divider'
                    q=0
                elif letter not in alph_str:
                    q=2
                    last_class = 'unknown token - expected end of str'
            
        last_token += letter
    tokens.append(last_token)
    classes.append(last_class)
    return tokens, classes
    
def analyse_code():
    path = input('Please enter path to your input file: ')
    inp = open(path, 'r').read()
    tokens, classes = parse_words(inp)
    tokenized = [list(x) for x in zip(tokens, classes)]
    output_str = ''
    for item in tokenized:
        if not (item[0] in ['', '\t', '\n']):
            if item[1] == 'word':
                if item[0] in reserved:
                    item[1] = 'reserved word'
                elif item[0][0] in alph_decimal:
                    item[1] = 'error - identifier begins with number'
                else:
                    item[1] = 'identifier'
            output_str += item[0] + ' -> ' + item[1] + '\n\n'
    file = open("C:\dev\Lang\Lab3\output.txt", "w") 
    file.write(output_str) 
    file.close() 

#C:\dev\Lang\Lab3\test.txt
#C:\dev\Lang\Lab3\test2.txt
analyse_code()