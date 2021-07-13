
def validar_variables(p, variables_asignadas, op):
    if(type(p[1]) == type(p[3]) == str):
        if((variables_asignadas.__contains__(p[1])) & variables_asignadas.__contains__(p[3])):
            print( '%s entre variables' % op )
        else:
            print('ALERTA TIPO 1: variable no asignada')
    else:
        if (type(p[1]) == int):
            if (variables_asignadas.__contains__(p[3])):
                print('%s entre una número y una variable' % op)
            else:
                print('ALERTA TIPO 2: variable no asignada')
        if (type(p[3]) == int):
            if(variables_asignadas.__contains__(p[1])):
                print( '%s entre una variable y un número' % op)
            else:
                print('ALERTA TIPO 3: variable no asignada')


