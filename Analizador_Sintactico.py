import ply.yacc as yacc
from Analizador_Lexico import tokens


#AQUÍ EMPIEZA MI TRABAJO - AARÓN REYES

#REGLA PADRE
def p_sentencia(p):
    '''sentencia : funcion| asignacion''' #''' | print| expresion| estructuta'''

#FUNCION
def p_funcion(p):
    '''funcion : DEF VARIABLE_LOCAL L_PAREN variables R_PAREN cuerpo END'''

def p_variables(p):
    '''variables : VARIABLE_LOCAL
            | VARIABLE_LOCAL COMMA variables'''

def p_cuerpo(p):
    '''cuerpo : asignacion | asignacion cuerpo
            | PRINT | PRINT cuerpo
            | variables | variables cuerpo
    '''
def p_asignacion(p):
    '''definiendo'''

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
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)