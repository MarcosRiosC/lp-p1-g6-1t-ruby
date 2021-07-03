import ply.lex as lex

# AQUÍ EMPIEZA UNA PARTE DE MI TRABAJO - AARÓN REYES
# Mapa de palabras reservadas
reserved = {
    'and' : 'AND',
    'begin' : 'BEGIN',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'do' : 'DO',
    'else' : 'ELSE',
    'elsif' : 'ELSIF',
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
    'puts' : 'PUTS',
    'rescue' : 'RESCUE',
    'retry' : 'RETRY',
    'return' : 'RETURN',
    'then' : 'THEN',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'while' : 'WHILE',
    'gets' : 'GETS',
    'loop' : 'LOOP',
    'do' : 'DO'
}

# Tupla de tokens
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
    'L_SQUARE_BRACKET',
    'MINUS',
    'MODULE',
    'MULTIPLICATION',
    'NEGATION',
    'NUMBER',
    'OR_LOGIC',
    'PLUS',
    'R_SQUARE_BRACKET',
    'R_PAREN',
    'SMALLER_THAN',
    'SMALLER_EQUAL',
    'QUOTATION_MARK',
    'WRENCH_L',
    'WRENCH_R',
    'COMMA',
    'DOUBLE_QUOTE',
    'DOUBLE_POINT',
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCE',
    'VARIABLE_CLASS',
    'VARIABLE_GLOBAL',
    'CONSTANT',
    'STRING',
    'FLOAT'
) + tuple(reserved.values())
# AQUÍ TERMINA UNA PARTE DE MI TRABAJO - AARÓN REYES

# AQUÍ EMPIEZA UNA PARTE DE MI TRABAJO - AARÓN REYES
# Regla de expresiones regulares para los tokens
t_AND_LOGIC = r'&'
t_DIVIDE = r'/'
t_EQUALITY = r'=='
t_EQUALITY_OF_CASE = r'==='
t_EXPONENT = r'\*\*'
t_GREATER_EQUAL = r'>='
t_GREATER_THAN = r'>'
t_MINUS = r'-'
t_MODULE = r'%'
t_MULTIPLICATION = r'\*'
t_OR_LOGIC = r'\|'
t_PLUS = r'\+'
t_SMALLER_THAN = r'<'
t_SMALLER_EQUAL = r'<='
#################################################
t_COINCIDENCE = r'=~'
t_COMPOSITION = r'\|&'
t_EQUAL = r'\='
t_L_PAREN = r'\('
t_L_SQUARE_BRACKET = r'\['
t_NEGATION = r'!'
t_R_SQUARE_BRACKET = r'\]'
t_R_PAREN = r'\)'
t_WRENCH_L = r'\{'
t_WRENCH_R = r'\}'
t_COMMA = r'\,'
t_DOUBLE_POINT = r'\.\.'
t_ignore = ' \t'

def t_float(t):
    r'[0-9]+\.[0-9]+'
    t.type = reserved.get(t.value, 'FLOAT')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# AQUÍ TERMINA UNA PARTE DE MI TRABAJO - AARÓN REYES

#AQUÍ EMPIEZA TRABAJO - KATIUSKA MARÍN
# Expreciones que definen una variable
def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z_]*\d*'
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

def t_COMMENT(t):
    r'\#.*'
    pass

def t_STRING(t):
    r'\"[a-zA-Z0-9\s]*\"$'
    t.type = reserved.get(t.value, 'STRING')
    return t
#AQUÍ TERMINA KATIUSKA MARÍN


#DE AQUÍ EN ADELANTE EL CÓDIGO FUE RECICLADO DE LA PRÁCTICA EN CLASES
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