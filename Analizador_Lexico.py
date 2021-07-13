import ply.lex as lex

# Mapa de palabras reservadas
reserved = {
    'def' : 'DEF',
    'do' : 'DO',
    'else' : 'ELSE',
    'elsif' : 'ELSIF',
    'end' : 'END',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'if' : 'IF',
    'in' : 'IN',
    'nil' : 'NIL',
    'not' : 'NOT',
    'return' : 'RETURN',
    'then' : 'THEN',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'while' : 'WHILE',
    'case' : 'CASE',
    'loop' : 'LOOP',
    'break' : 'BREAK'
}

#Mapa de funciones
funciones = {
    'class': 'CLASS',
    'gets' : 'GETS',
    'puts': 'PUTS',
    'to_i' : 'TO_I',
    'to_f' : 'TO_F',
    'to_s' : 'TO_S'
}

# Tupla de tokens
tokens = (
    'AND_LOGIC',
    'DIVIDE',
    'EQUAL',
    'EQUALITY',
    'EXPONENT',
    'GREATER_EQUAL',
    'GREATER_THAN',
    'L_PAREN',
    'L_SQUARE_BRACKET',
    'MINUS',
    'MODULE',
    'MULTIPLICATION',
    'NEGATION',
    'ENTERO',
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
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCE',
    'VARIABLE_CLASS',
    'VARIABLE_GLOBAL',
    'CONSTANT',
    'STRING',
    'FLOAT',
    'POINT',
    'DOUBLE_POINT'
) + tuple(reserved.values()) + tuple(funciones.values())

# Regla de expresiones regulares para los tokens
t_AND_LOGIC = r'&'
t_DIVIDE = r'/'
t_EQUALITY = r'=='
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
t_EQUAL = r'\='
t_L_PAREN = r'\('
t_L_SQUARE_BRACKET = r'\['
t_NEGATION = r'!'
t_R_SQUARE_BRACKET = r'\]'
t_R_PAREN = r'\)'
t_WRENCH_L = r'\{'
t_WRENCH_R = r'\}'
t_COMMA = r'\,'
t_POINT = r'\.'
t_DOUBLE_POINT = r'\.\.'
t_ignore = ' \t'

def t_float(t):
    r'[0-9]+\.[0-9]+'
    t.type = 'FLOAT'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z_]*\d*'
    if reserved.keys().__contains__(t.value):
        t.type = reserved.get(t.value)
        print('Palabra reservada')
        return t
    elif funciones.keys().__contains__(t.value):
        t.type = funciones.get(t.value)
        print('Función')
        return t
    else:
        return t

def t_VARIABLE_INSTANCE(t):
    r'@[a-z_][a-zA-Z_]+\d*'
    if reserved.keys().__contains__(t.value[1:]):
        t.type = reserved.get(t.value[1:])
        print('Palabra reservada')
        return t
    elif funciones.keys().__contains__(t.value[1:]):
        t.type = funciones.get(t.value[1:])
        print('Función')
        return t
    else:
        return t

def t_VARIABLE_CLASS(t):
    r'@{2}[a-z_][a-zA-Z_]+\d*'
    if reserved.keys().__contains__(t.value[2:]):
        t.type = reserved.get(t.value[2:])
        print('Palabra reservada')
        return t
    elif funciones.keys().__contains__(t.value[2:]):
        t.type = funciones.get(t.value[2:])
        print('Función')
        return t
    else:
        return t

def t_CONSTANT(t):
    r'[A-Z_]+'
    if reserved.keys().__contains__(t.value.swapcase()):
        t.type = reserved.get(t.value.swapcase())
        print('Palabra reservada')
        return t
    elif funciones.keys().__contains__(t.value.swapcase()):
        t.type = funciones.get(t.value.swapcase())
        print('Función')
        return t
    else:
        return t

def t_VARIABLE_GLOBAL(t):
    r'\$[a-z_][a-zA-Z_]+\d*'
    if reserved.keys().__contains__(t.value[1:]):
        t.type = reserved.get(t.value[1:])
        print('Palabra reservada')
        return t
    elif funciones.keys().__contains__(t.value[1:]):
        t.type = funciones.get(t.value[1:])
        print('Función')
        return t
    else:
        return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_STRING(t):
    r'\"[a-zA-Z0-9\s\.]*\"'
    t.type = 'STRING'
    return t

#DE AQUÍ EN ADELANTE EMPIEZA EL COPY PASTE SALVAJE (CÓDIGO RECICLADO DE LA PRÁCTICA EN CLASES)
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

'''while linea != "":
    linea = input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")'''