
def validar_variables(p, variables_asignadas, op):
    if(type(p[1]) == type(p[3]) == str):
        if((variables_asignadas.__contains__(p[1])) & variables_asignadas.__contains__(p[3])):
            print( '%s entre variables' % op )
        else:
            print('variable no asignada 1')
    else:
        if (type(p[1]) == int):
            if (variables_asignadas.__contains__(p[3])):
                print('%s entre una variable y un número 1' % op)
            else:
                print('variable no asignada 2')
        if (type(p[3]) == int):
            if(variables_asignadas.__contains__(p[1])):
                print( '%s entre una variable y un número 2' % op)
            else:
                print('variable no asignada 3')


