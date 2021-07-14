import ply.yacc as yacc
from Analizador_Lexico import tokens
import Funciones_Analizador_Semántico as semantico

#REGLA PADRE
def p_sentencia(p):
    '''sentencia : funcion
                | declaracion
                | estructura
                '''
    p[0] = p [1]


#FUNCION
def p_funcion(p):
    '''funcion : DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo END'''
    p [0] = 'funcion'

def p_parametros(p):
    '''parametros : VARIABLE_LOCAL
            | VARIABLE_LOCAL COMMA parametros'''

def p_cuerpo(p):
    '''cuerpo : declaracion
            | declaracion cuerpo
            | print
            | print cuerpo
            | estructura
            | estructura cuerpo
    '''


#DECLARACION
variables_asignadas = []
tipo_datos_asignados = []

def p_declaracion_termino(p):
    'declaracion : variable EQUAL termino'
    p[0] = p[1]
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(type(p[3]))
    print('variable asignada')

def p_declaracion_string(p):
    'declaracion : variable EQUAL STRING'
    p[0] = p[1]
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(str)
    print('variable asignada')

def p_declaracion_booleano(p):
    'declaracion : variable EQUAL booleano'
    p[0] = p[1]
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(bool)
    print('variable asignada')

def p_declaracion_operacion(p):
    'declaracion : variable EQUAL operacion'
    p[0] = p[1]
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(type(p[3]))
    print('variable asignada')

def p_declaracion_gets(p):
    'declaracion : variable EQUAL GETS'
    p[0] = str(p[1]) + p[2] + str(p[3])
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(str)
    print('variable asignada')

def p_declaracion_metodo(p):
    'declaracion : variable EQUAL metodo'
    p[0] = p[1]
    variables_asignadas.append(p[0])
    tipo_datos_asignados.append(type(p[3]))
    print('variable asignada')

def p_variable(p):
    '''variable : VARIABLE_LOCAL
            | VARIABLE_INSTANCE
            | VARIABLE_CLASS
            | VARIABLE_GLOBAL
            | CONSTANT'''
    p[0] = p[1]

def p_booleano_and_logic(p):
    'booleano : booleano AND_LOGIC booleano'
    p[0] = p[1] & p[3]

def p_booleano_or_logic(p):
    'booleano : booleano OR_LOGIC booleano'
    p[0] = p[1] | p[3]

def p_booleano_equality(p):
    'booleano : termino EQUALITY termino'
    p[0] = p[1] == p[3]

def p_booleano_greater_equal(p):
    'booleano : termino GREATER_EQUAL termino'
    p[0] = p[1] >= p[3]

def p_booleano_greater_than(p):
    'booleano : termino GREATER_THAN termino'
    p[0] = p[1] > p[3]

def p_booleano_smaller_than(p):
    'booleano : termino SMALLER_THAN termino'
    p[0] = p[1] < p[3]

def p_booleano_smaller_equal(p):
    'booleano : termino SMALLER_EQUAL termino'
    p[0] = p[1] <= p[3]


#ESTRUCTURAS DE CONTROL
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
    'estructuraif : IF booleano cuerpo'
    p[0] = str(p[1]) + " " + str(p[2])

def p_estructuraelsif(p):
    'estructuraelseif : ELSIF booleano cuerpo'

def p_estructuraelse(p):
    'estructuraelse : ELSE cuerpo'

def p_estructuraSelectCase(p):
    'estructuraSelectCase : CASE variable cuerpoSelectCase estructuraelse END'

def p_cuerpoSelectCase(p):
    '''cuerpoSelectCase : WHEN termino booleano
                        | WHEN termino booleano cuerpoSelectCase
                        | WHEN termino print
                        | WHEN termino print cuerpoSelectCase'''

def p_estructuraDoLoop(p):
    '''estructuraDoLoop : LOOP DO booleano BREAK END
                        | LOOP DO booleano print BREAK END'''

def p_estructuraIterativa(p):
    '''estructuraIterativa : sentenciafor END
                            | sentenciawhile END
                            | estructuraDoLoop'''

def p_sentenciafor(p):
    'sentenciafor : FOR variable IN L_PAREN ENTERO DOUBLE_POINT ENTERO R_PAREN cuerpo'

def p_sentenciawhile(p):
    'sentenciawhile : WHILE booleano cuerpo'

def p_estructuraDato(p):
    'estructuraDato : estructuraDatoArray'

def p_estructuraDatoArray(p):
    '''estructuraDatoArray : variable EQUAL L_SQUARE_BRACKET R_SQUARE_BRACKET
        | variable EQUAL L_SQUARE_BRACKET arrayContext R_SQUARE_BRACKET
    '''

def p_arrayContext(p):
    '''arrayContext : variable
        | ENTERO
        | FLOAT
        | STRING
        | variable COMMA arrayContext
        | ENTERO COMMA arrayContext
        | FLOAT COMMA arrayContext
        | STRING COMMA arrayContext
    '''


#PRINT
def p_puts_operacion(p):
    'puts : PUTS L_PAREN operacion R_PAREN'

def p_puts_booleano(p):
    'puts : PUTS L_PAREN booleano R_PAREN'

def p_puts_var(p):
    'puts : PUTS L_PAREN variable R_PAREN'

def p_puts_vac(p):
    'puts : PUTS L_PAREN R_PAREN'


#Metodos
def p_metodo_class(p):
    'metodo : termino POINT CLASS'

def p_metodo_to_i(p):
    'metodo : termino POINT TO_I'

def p_metodo_to_f(p):
    'metodo : termino POINT TO_F'

def p_metodo_to_s(p):
    'metodo : termino POINT TO_S'


#REGLA SEMÁNTICA PARA OPERACIONES MATEMÁTICAS (INICIO)

def p_operacion_plus(p):
    'operacion : termino PLUS termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] + p[3]
        print('suma entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'suma')

def p_operacion_minus(p):
    'operacion : termino MINUS termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] - p[3]
        print('resta entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'resta')

def p_operacion_multiplication(p):
    'operacion : termino MULTIPLICATION termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] * p[3]
        print('multiplicación entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'multiplicación')

def p_operacion_divide(p):
    'operacion : termino DIVIDE termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] / p[3]
        print('división entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'división')

def p_operacion_exponent(p):
    'operacion : termino EXPONENT termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] ** p[3]
        print('potencia entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'potencia')

def p_operacion_module(p):
    'operacion : termino MODULE termino'
    if (type(p[1]) == type(p[3]) == int):
        p[0] = p[1] % p[3]
        print('módulo entre números')
    else:
        semantico.validar_variables(p, variables_asignadas, tipo_datos_asignados, 'módulo')

def p_termino_entero(p):
    'termino : ENTERO'
    p[0] = int(p[1])

def p_termino_float(p):
    'termino : FLOAT'
    p[0] = float(p[1])

def p_termino_var(p):
    'termino : variable'
    p[0] = p[1]

def p_termino_expr(p):
    'termino : L_PAREN operacion R_PAREN'
    p[0] = p[2]

def p_termino_operacion(p):
    'termino : operacion'
    p[0] = p[1]
#REGLA SEMÁNTICA PARA OPERACIONES MATEMÁTICAS (FIN)

#DE AQUÍ EN ADELANTE EMPIEZA EL COPY PASTE SALVAJE (CÓDIGO RECICLADO DE LA PRÁCTICA EN CLASES)
#EVALUADOR DE ERRORES
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        #return "Syntax error at token "+ p.type
        raise TypeError("Syntax error at %r with type %s" % (p.value,p.type))
    else:
        print("Syntax error at EOF")
        #return "Syntax error at EOF"


#CONSTRUCCION DEL PARSER
parser = yacc.yacc()

#aqui hizo marcos
def evaluar(texto):
    try:
        s = texto
    except EOFError:
        return ''
    if not s:
        return ''
    try:
        result = parser.parse(s)
        return result
    except Exception as e:
        return str(e)

# aqui finalizo marcos

estructuras = []
'''
while True:
    try:
        s = input('calc >> ')

    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(variables_asignadas)
    print(tipo_datos_asignados)
'''