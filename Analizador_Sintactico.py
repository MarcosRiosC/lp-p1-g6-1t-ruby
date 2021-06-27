import ply.yacc as yacc
from Analizador_Lexico import tokens

#AQUÍ EMPIEZA MI TRABAJO - AARÓN REYES
#REGLA PADRE
def p_sentencia(p):
    '''sentencia : funcion
                | declaracion
                | expresion
                | print'''


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


#ASIGNACION
def p_declaracion(p):
    'declaracion : variable EQUAL expresion'
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
'''def p_print_str(p):
    'print : PUTS L_PAREN STRING R_PAREN'''


#EVALUADOR DE ERRORES
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")


#CONSTRUCCION DEL PARSER
parser = yacc.yacc()
while True:
    try:
        s = input('calc >> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
#AQUÍ TERMINA MI TRABAJO - AARÓN REYES