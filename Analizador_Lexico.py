import ply.lex as lex
# Reserved words hash
# Aarón reyes - palabras reservadas
reserved = {
    'and' : 'AND',
    'begin' : 'BEGIN',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'do' : 'DO',
    'else' : 'ELSE',
    'elsif' : 'ELIF',
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
    'while' : 'WHILE',
}


# start Aarón Reyes - tokens
tokens = (
    'AND_LOGIC',
    'COINCIDENCE',
    'COMPOSITION',
    'DIVIDE',
    'EQUAL',
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
    'SMALLER_EQUAL',
    'QUOTATION_MARK',
    'WRENCH_L',
    'WRENCH_R',
    'COMMA',
    'DOUBLE_QUOTE',
    #end Aarón Reyes - tokens
    # start Katiuska Marín S.
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCE',
    'VARIABLE_CLASS',
    'VARIABLE_GLOBAL',
    'CONSTANT',
    # end Katiuska Marín S.
) + tuple(reserved.values())


# Regular expression rules for simple tokens
# start Aarón Reyes - ERtokens
t_AND_LOGIC = r'&'
t_COINCIDENCE = r'=~'
t_COMPOSITION = r'\|&'
t_DIVIDE = r'/'
t_EQUAL = r'\='
t_EQUALITY = r'=='
t_EQUALITY_OF_CASE = r'==='
t_EXPONENT = r'\*\*'
t_GREATER_EQUAL = r'>='
t_GREATER_THAN = r'>'
t_L_PAREN = r'\('
t_MINUS = r'-'
t_MODULE = r'%'
t_MULTIPLICATION = r'\*'
t_NEGATION = r'!'
t_OR_LOGIC = r'\|'
t_PLUS = r'\+'
t_R_PAREN = r'\)'
t_SMALLER_THAN = r'<'
t_SMALLER_EQUAL = r'<='
t_QUOTATION_MARK = r'\''
t_WRENCH_L = r'\{'
t_WRENCH_R = r'\}'
t_COMMA = r','
t_DOUBLE_QUOTE = r'"'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# end Aarón Reyes - ERtokens


# Expreciones que definen una variable
# start Katiuska Marín S.
def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z_]+\d*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t

def t_VARIABLE_INSTANCE(t):
    r'@[a-z_][a-zA-Z_]+\d*'
    t.type = reserved.get(t.value, 'VARIABLE_INSTANCE')
    return t

def t_VARIABLE_CLASS(t):
    r'@{2}[a-z_][a-zA-Z_]+\d*'
    t.type = reserved.get(t.value, 'VARIABLE_CLASS')
    return t

def t_CONSTANT(t):
    r'[A-Z_]+'
    t.type = reserved.get(t.value, 'CONSTANT')
    return t

def t_VARIABLE_GLOBAL(t):
    r'\$[a-z_][a-zA-Z_]+\d*'
    t.type = reserved.get(t.value, 'VARIABLE_GLOBAL')
    return t
# end Katiuska Marín S.

# De aquí en adelante el código fue reciclado de la práctica en clases.
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

linea = " "

while linea != "":
    linea = input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")