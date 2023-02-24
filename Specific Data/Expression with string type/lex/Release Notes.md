# Release Notes
## In version 1
### Release Date:
2022/02/24 10:03 a.m.
### Bugs
There are NO bugs.
### Function:
One can use lex to split the expression with string type into tokens and handle it.

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
     
        
       1) Flexible

# Ref
1. MORE details and knowledge of lex, visit the following websites.

        https://www.dabeaz.com/ply/ply.html#ply_nn0
        
 2. Way to define either a variable or a function with the name with string type.
        
        https://www.geeksforgeeks.org/python-program-to-create-dynamically-named-variables-from-user-input/
