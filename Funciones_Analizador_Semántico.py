
def validar_variables(p, variables_asignadas, tipo_datos_asignados, op):
    if(type(p[1]) == type(p[3]) == str):
        if((variables_asignadas.__contains__(p[1])) & variables_asignadas.__contains__(p[3])):
            if tipo_datos_asignados[variables_asignadas.index(p[1])] == tipo_datos_asignados[variables_asignadas.index(p[3])]:
                print( '%s entre variables' % op )
            else:
                print('esta operación no se puede realizar')
        else:
            print('ALERTA TIPO 1: variable no asignada')
    else:
        if (type(p[1]) == (int | float | str)):
            if (variables_asignadas.__contains__(p[3])):
                if tipo_datos_asignados[variables_asignadas.index(p[3])] == (int | float | str):
                    print('%s entre una número y una variable' % op)
                else:
                    print('esta operación no se puede realizar')
            else:
                print('ALERTA TIPO 2: variable no asignada')
        if (type(p[3]) == (int | float | str)):
            if(variables_asignadas.__contains__(p[1])):
                if tipo_datos_asignados[variables_asignadas.index(p[1])] == (int | float | str):
                    print( '%s entre una variable y un número' % op)
                else:
                    print('esta operación no se puede realizar')
            else:
                print('ALERTA TIPO 3: variable no asignada')
