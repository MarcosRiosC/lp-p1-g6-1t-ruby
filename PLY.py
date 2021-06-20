import ply.lex as lex
# Reserved words hash
reserved = {
    'and' : 'AND',
    'begin' : 'BEGIN',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'do' : 'DO',
    'else' : 'ELSE',
    'elif' : 'ELIF',
    'end' : 'END',
    'ensure' : 'ENSURE',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'if' : 'IF',
    'in' : 'IN',
    'nil' : 'NIL',
    'not' : 'NOT',
    'or' : 'OR',
    'rescue' : 'RESCUE',
    'retry' : 'RETRY',
    'return' : 'RETURN',
    'then' : 'THEN',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'while' : 'WHILE'
}

tokens = (
    'AND_LOGIC',
    'COINCIDENCE',
    'COMPOSITION',
    'DIVIDE',
    'EQUALITY',
    'EQUALITY_OF_CASE',
    'EXPONENT',
    'GREATER_EQUAL',
    'GREATER_THAN',
    'L_PAREN',
    'MINUS',
    'MODULE',
    'MULTIPLICATION',
    'NEGATION',
    'NUMBER',
    'OR_LOGIC',
    'PLUS',
    'R_PAREN',
    'SMALLER_THAN',
    'SMALLER_EQUAL'
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_AND_LOGIC = r'\&'
t_COINCIDENCE = r'=~'
t_COMPOSITION = r'\|&'
t_DIVIDE = r'\/'
t_EQUALITY = r'=='
t_EQUALITY_OF_CASE = r'==='
t_EXPONENT = r'\*\*'
t_GREATER_EQUAL = r'>='
t_GREATER_THAN = r'>'
t_L_PAREN = r'\('
t_MINUS = r'\-'
t_MODULE = r'\%'
t_MULTIPLICATION = r'\*'
t_NEGATION = r'\!'
t_OR_LOGIC = r'\|'
t_PLUS = r'\+'
t_R_PAREN = r'\)'
t_SMALLER_THAN = r'<'
t_SMALLER_EQUAL = r'<='
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")