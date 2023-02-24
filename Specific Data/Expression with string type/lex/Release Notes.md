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
 
To do this, I use vars()[ <string_name> ]= <variable> 
### Advantage to the first code of the following website in Ref section.

# Ref
MORE details and knowledge of lex, visit the following websites.

https://www.dabeaz.com/ply/ply.html#ply_nn0
