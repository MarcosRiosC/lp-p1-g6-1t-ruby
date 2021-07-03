import ply.yacc as yacc
from Analizador_Lexico import tokens

#AQUÍ EMPIEZA UNA PARTE DE MI TRABAJO - AARÓN REYES
#REGLA PADRE
def p_sentencia(p):
    '''sentencia : funcion
                | declaracion
                | expresion
                | estructura
                | print
                '''


#FUNCION
def p_funcion(p):
    '''funcion : DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo END'''
def p_parametros(p):
    '''parametros : VARIABLE_LOCAL
            | VARIABLE_LOCAL COMMA parametros'''
def p_cuerpo(p):
    '''cuerpo : declaracion
            | declaracion cuerpo
            | print
            | print cuerpo
            | expresion
            | expresion cuerpo
    '''


#DECLARACION
def p_declaracion(p):
    'declaracion : variable EQUAL expresion'
def p_declaracion_gets(p):
    'declaracion : variable EQUAL GETS'
def p_variable(p):
    '''variable : VARIABLE_LOCAL
            | VARIABLE_INSTANCE
            | VARIABLE_CLASS
            | VARIABLE_GLOBAL
            | CONSTANT'''


#EXPRESION
def p_expresion_plus(p):
    'expresion : expresion PLUS term'
def p_expresion_minus(p):
    'expresion : expresion MINUS term'
def p_expresion_multiplication(p):
    'expresion : expresion MULTIPLICATION term'
def p_expresion_divide(p):
    'expresion : expresion DIVIDE term'
def p_expresion_exponent(p):
    'expresion : expresion EXPONENT term'
def p_expresion_module(p):
    'expresion : expresion MODULE term'
def p_expresion_and_logic(p):
    'expresion : expresion AND_LOGIC term'
def p_expresion_or_logic(p):
    'expresion : expresion OR_LOGIC term'
def p_expresion_equality(p):
    'expresion : expresion EQUALITY term'
def p_expresion_equality_of_case(p):
    'expresion : expresion EQUALITY_OF_CASE term'
def p_expresion_greater_equal(p):
    'expresion : expresion GREATER_EQUAL term'
def p_expresion_greater_than(p):
    'expresion : expresion GREATER_THAN term'
def p_expresion_smaller_than(p):
    'expresion : expresion SMALLER_THAN term'
def p_expresion_smaller_equal(p):
    'expresion : expresion SMALLER_EQUAL term'
def p_expresion_term(p):
    'expresion : term'
def p_term_number(p):
    'term : NUMBER'
def p_term_float(p):
    'term : FLOAT'
def p_term_var(p):
    'term : variable'
def p_term_expr(p):
    'term : L_PAREN expresion R_PAREN'


#PRINT
def p_print_exp(p):
    'print : PUTS L_PAREN expresion R_PAREN'
def p_print_var(p):
    'print : PUTS L_PAREN variable R_PAREN'
def p_print_vac(p):
    'print : PUTS L_PAREN R_PAREN'
##def p_print_str(p):
##    'print : PUTS L_PAREN STRING R_PAREN'''
#AQUÍ TERMINA UNA PARTE DE MI TRABAJO - AARÓN REYES


#AQUÍ EMPIEZA TRABAJO - KATIUSKA MARÍN
def p_print_str(p):
    '''print : PUTS STRING
            | PUTS L_PAREN STRING R_PAREN'''

def p_estructura(p):
    '''estructura : estructuraCondicional
                    | estructuraIterativa
                    | estructuraDato
                    '''

def p_estructuraCondicional(p):
    '''estructuraCondicional : estructuraif END
                             | estructuraif estructuraelse END
                             | estructuraif estructuraelseif END
                             | estructuraSelectCase estructuraelse END'''

def p_estructuraif(p):
    'estructuraif : IF expresion cuerpo'

def p_estructuraelsif(p):
    'estructuraelseif : ELSIF expresion cuerpo'

def p_estructuraelse(p):
    'estructuraelse : ELSE cuerpo'

def p_estructuraSelectCase(p):
    'estructuraSelectCase : CASE variable cuerpoSelectCase estructuraelse END'

def p_cuerpoSelectCase(p):
    '''cuerpoSelectCase : WHEN term expresion
                        | WHEN term expresion cuerpoSelectCase'''

def p_estructuraIterativa(p):
    '''estructuraIterativa : sentenciafor END
                            | sentenciawhile END'''

def p_sentenciafor(p):
    'sentenciafor : FOR variable IN L_PAREN NUMBER DOUBLE_POINT NUMBER R_PAREN cuerpo'

def p_sentenciawhile(p):
    'sentenciawhile : WHILE expresion cuerpo'


#AQUÍ TERMINA KATIUSKA MARÍN
# marcos rios
def p_estructuraDato(p):
    'estructuraDato : estructuraDatoArray'
def p_estructuraDatoArray(p):
    '''estructuraDatoArray : variable EQUAL L_SQUARE_BRACKET R_SQUARE_BRACKET
        | variable EQUAL L_SQUARE_BRACKET arrayContext R_SQUARE_BRACKET
    '''
def p_arrayContext(p):
    '''arrayContext : variable
        | NUMBER
        | variable COMMA arrayContext
        | NUMBER COMMA arrayContext
    '''
# marcos rios fin

#DE AQUÍ EN ADELANTE EL CÓDIGO FUE RECICLADO DE LA PRÁCTICA EN CLASES
#EVALUADOR DE ERRORES
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")


#CONSTRUCCION DEL PARSER
parser = yacc.yacc()
'''
#aqui hizo marcos
def evaluar(texto):
    try:
        s = texto
    except EOFError:
        return ''
    if not s:
        return ''
    result = parser.parse(s)
    return result
# aqui finalizo marcos
'''
while True:
    try:
        s = input('calc >> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)