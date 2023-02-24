import ply.lex as lex
class LEX():

    def __init__(self
    ,tokens:tuple
    ,data:str
    ,validToken:dict
    ,func_dict:dict
    ):
        for k,v in validToken.items():
            k="t_"+k
            vars()[k]=v

        for k,v in func_dict.items():
            k="t_"+k
            vars()[k]=v
    
        self.lexer= lex.lex()
        self.tokens=tokens
        self.data=data
        self.lexer.input(data)

    def Input(self
    ,data:str
    ):
        self.data=data
        self.lexer.input(data)

    def Tokenize(self,func):
        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            func(tok)

def test():

    tokens_op = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ignore',
    )

    tokens_number=(
    'NUMBER',
    )

    tokens=tokens_op+tokens_number

    tokens_other=(
        "error",
        "newline",
    )

    tokens_other=tokens_number+tokens_other

    data = '''
    3 + 4 * 10
    + -20 *2
    '''

    validToken_key=[
        r'\+'
        ,r'-'
        ,r'\*'
        ,r'/'
        ,r'\('
        ,r'\)'
        ,' \t'
    ]
    length=len(validToken_key)
    validToken=dict()
    for idx in range(0,length,1):
        v=validToken_key[idx]
        k=tokens_op[idx]
        validToken.update({k:v})

    for k,v in validToken.items():
            k="t_"+k
            vars()[k]=v

    def func(msg):
        print(msg)

    def func_int(t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def func_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def func_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    func_list=[
        func_int,
        func_error,
        func_newline
    ]

    func_dict=dict()
    length=len(func_list)
    for idx in range(0,length,1):
        v=func_list[idx]
        k=tokens_other[idx]
        validToken.update({k:v})

    lexer=LEX(tokens=tokens,data=data,validToken=validToken,func_dict=func_dict)
    lexer.Tokenize(func=func)

if __name__=='__main__':
    test()


"""
If you run this code directly, you will see
output:
LexToken(NUMBER,3,2,5)
LexToken(PLUS,'+',2,7)
LexToken(NUMBER,4,2,9)
LexToken(TIMES,'*',2,11)
LexToken(NUMBER,10,2,13)
LexToken(PLUS,'+',3,20)
LexToken(MINUS,'-',3,22)
LexToken(NUMBER,20,3,23)
LexToken(TIMES,'*',3,26)
LexToken(NUMBER,2,3,27)
"""
