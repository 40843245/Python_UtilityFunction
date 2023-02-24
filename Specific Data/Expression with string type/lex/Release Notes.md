# Release Notes
## In version 1
### Release Date:
2022/02/24 10:03 a.m. Finish my project

2022/02/24 11:15 a.m. Finish my Release Notes.md
### Bugs
There are NO bugs.
### Function:
One can use lex to split the expression with string type into tokens and handle it.

### NOTE 
Note that line 82 to line 87 are extraneous.

It does NOT take any effect to comment them.

In test function, the following code.

    """
    for k,v in validToken.items():
            k="t_"+k
            vars()[k]=v
    """
    
### intro to this code
1. In example of this code, it simply check each tokens is one of +,-,*, /, a number.

If the token is one of +,-,*,/ , just print it.

Else if the token is a number, convert it into integer then print it.

(Why converts it into an integer?

Since t_NUMBER is defined as 

        r'\d+'
        t.value = int(t.value)    
        return t
 )

Else if the token is either a whitespace or a tab, just ignore it. 

(since t_ignore=' \t') 

(NOTE that there is a whitespace in t_ignore)

Else if the token is a newline, just count the number of tokens in this line then go to the next line.
(since t_newline is defined as

        r'\n+'
        t.lexer.lineno += len(t.value)
)

Else, print that it is illegal character then skip the token.
(since t_error is defined as 
     
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
        
)

(P.S. one token represents one letter)

2. Assigning a string and make it either a variable or a function.
 
To do this, I use 

        vars()[ <string_name> ] = <value>
        
And I define a variable whose name is <string_name> and its value is <value>
        
Similarly for defining a function with the name with string type.
        
For more details, visit the following second website in Ref section.
        
### Advantage to the first code of the following first website in Ref section.
     
       1) Flexible:
       
       It is more flexible to define valid tokens and functions.
        
       One don't have to chnage the code of LEX class to perform different things.
        
       One just has to define the function, adding it into the list, adding the name to the tuple
        
       then pass the list and the tuple as parameters of the constructor of the LEX class.
        
        For more details, see the code or see the following section -- details to this code.
        
### Details to this code
        
1. The constructor of the LEX class is defined as follows.
        
     def __init__(self
    ,tokens:tuple
    ,data:str
    ,validToken:dict
    ,func_dict:dict
    ):
       
where
    
     1) data: 
        
        it represents the source data for lex. It must be a string.
        
     2) validToken: 
        
        it determines which token are a valid token NOT trash. It must be a dictionary whose keys are strings and values are also strings.
        
        For each key of validToken named k and each values of them named v,
        
        we define the variables named "t_" + k (the concatenation of "t_" and k) as v.
        
        i.e. < "t_" + k > = v.
        
        For each valid token named tok, the line func(tok) will be executed.
        
        def Tokenize(self,func):
        
           while True:
        
            tok = self.lexer.token()
        
            if not tok: 
        
                break      # No more input
        
            func(tok)
        
     3) func_dict:
        
        Similarly for validToken. It must also be a dictionary.
        
        For each key of func_dict named k and each values of them named v,
        
        we define these function named "t_" + k as v.
        
        i.e. < "t_" + k > = v.
        
        They are equivalent.
        
        To call a function named "t_" + k.
        
        and 

        To call a function named v (Note that NOT "v").
        
    4) tokens:
        
        it determines which tokens are valid tokens. It must be a tuple.
        
2. In the constructor of LEX class, the following code
    
defines "t_" + k as v.
        
        for k,v in validToken.items():
            k="t_"+k
            vars()[k]=v

        for k,v in func_dict.items():
            k="t_"+k
            vars()[k]=v
      
3. For flexiblity, I combine these name for variable definition and function definition as dictionary by the following codes.
        
        length=len(validToken_key)
        validToken=dict()
        for idx in range(0,length,1):
                v=validToken_key[idx]
                k=tokens_op[idx]
                validToken.update({k:v})
        
and
        
        func_dict=dict()
        length=len(func_list)
        for idx in range(0,length,1):
                v=func_list[idx]
                k=tokens_other[idx]
                validToken.update({k:v})
        
4. In this example, the function to handle each valid token are defined in the line 88 and are passed as the parameter func of the method Tokenize.
        
        def func(msg):
                print(msg)
        
        
5. To feed data into self.lexer, the following statement are typed.
        
        self.lexer.input(data)
        
6. The method Tokenize in LEX class, it tokenize the data.
        
# Ref
1. MORE details and knowledge of lex, visit the following websites.

        https://www.dabeaz.com/ply/ply.html#ply_nn0
        
 2. Way to define either a variable or a function with the name with string type.
        
        https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/
