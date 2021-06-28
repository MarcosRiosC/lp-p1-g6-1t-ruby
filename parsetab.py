
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AND_LOGIC BEGIN BREAK CASE CLASS COINCIDENCE COMMA COMPOSITION CONSTANT DEF DIVIDE DO DOUBLE_POINT DOUBLE_QUOTE ELSE ELSIF END ENSURE EQUAL EQUALITY EQUALITY_OF_CASE EXPONENT FALSE FLOAT FOR GETS GREATER_EQUAL GREATER_THAN IF IN L_PAREN L_SQUARE_BRACKET MINUS MODULE MULTIPLICATION NEGATION NIL NOT NUMBER OR OR_LOGIC PLUS PUTS QUOTATION_MARK RESCUE RETRY RETURN R_PAREN R_SQUARE_BRACKET SMALLER_EQUAL SMALLER_THAN STRING THEN TRUE UNLESS UNTIL VARIABLE_CLASS VARIABLE_GLOBAL VARIABLE_INSTANCE VARIABLE_LOCAL WHEN WHILE WRENCH_L WRENCH_Rsentencia : funcion\n                | declaracion\n                | expresion\n                | estructura\n                | print\n                funcion : DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo ENDparametros : VARIABLE_LOCAL\n            | VARIABLE_LOCAL COMMA parametroscuerpo : declaracion\n            | declaracion cuerpo\n            | print\n            | print cuerpo\n            | expresion\n            | expresion cuerpo\n    declaracion : variable EQUAL expresiondeclaracion : variable EQUAL GETSvariable : VARIABLE_LOCAL\n            | VARIABLE_INSTANCE\n            | VARIABLE_CLASS\n            | VARIABLE_GLOBAL\n            | CONSTANTexpresion : expresion PLUS termexpresion : expresion MINUS termexpresion : expresion MULTIPLICATION termexpresion : expresion DIVIDE termexpresion : expresion EXPONENT termexpresion : expresion MODULE termexpresion : expresion AND_LOGIC termexpresion : expresion OR_LOGIC termexpresion : expresion EQUALITY termexpresion : expresion EQUALITY_OF_CASE termexpresion : expresion GREATER_EQUAL termexpresion : expresion GREATER_THAN termexpresion : expresion SMALLER_THAN termexpresion : expresion SMALLER_EQUAL termexpresion : termterm : NUMBERterm : FLOATterm : variableterm : L_PAREN expresion R_PARENprint : PUTS L_PAREN expresion R_PARENprint : PUTS L_PAREN variable R_PARENprint : PUTS L_PAREN R_PARENprint : PUTS STRINGestructura : estructuraCondicional\n                    | estructuraIterativaestructuraCondicional : estructuraif END\n                             | estructuraif estructuraelse END\n                             | estructuraif estructuraelseif ENDestructuraif : IF expresion cuerpoestructuraelseif : ELSIF expresion cuerpoestructuraelse : ELSE cuerpoestructuraIterativa : sentenciafor END\n                            | sentenciawhile ENDsentenciafor : FOR variable IN L_PAREN NUMBER DOUBLE_POINT NUMBER R_PAREN cuerposentenciawhile : WHILE expresion cuerpo'
    
_lr_action_items = {'DEF':([0,],[7,]),'PUTS':([0,8,10,11,15,16,17,18,19,20,43,46,50,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[14,-17,-39,-36,-18,-19,-20,-21,-37,-38,-39,-44,14,14,14,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,14,14,14,14,-41,-42,14,14,]),'VARIABLE_LOCAL':([0,7,8,9,10,11,15,16,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,81,82,83,84,90,91,97,98,105,],[8,41,-17,8,-39,-36,-18,-19,-20,-21,-37,-38,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-39,8,8,-44,8,8,8,8,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,88,-40,-15,-16,-43,8,8,8,8,-41,-42,88,8,8,]),'VARIABLE_INSTANCE':([0,8,9,10,11,15,16,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[15,-17,15,-39,-36,-18,-19,-20,-21,-37,-38,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-39,15,15,-44,15,15,15,15,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,15,15,15,15,-41,-42,15,15,]),'VARIABLE_CLASS':([0,8,9,10,11,15,16,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[16,-17,16,-39,-36,-18,-19,-20,-21,-37,-38,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-39,16,16,-44,16,16,16,16,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,16,16,16,16,-41,-42,16,16,]),'VARIABLE_GLOBAL':([0,8,9,10,11,15,16,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[17,-17,17,-39,-36,-18,-19,-20,-21,-37,-38,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-39,17,17,-44,17,17,17,17,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,17,17,17,17,-41,-42,17,17,]),'CONSTANT':([0,8,9,10,11,15,16,17,18,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[18,-17,18,-39,-36,-18,-19,-20,-21,-37,-38,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-39,18,18,-44,18,18,18,18,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,18,18,18,18,-41,-42,18,18,]),'NUMBER':([0,8,9,10,11,15,16,17,18,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,96,98,102,105,],[19,-17,19,-39,-36,-18,-19,-20,-21,-37,-38,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-39,19,19,-44,19,19,19,19,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,19,19,19,19,-41,-42,99,19,104,19,]),'FLOAT':([0,8,9,10,11,15,16,17,18,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,90,91,98,105,],[20,-17,20,-39,-36,-18,-19,-20,-21,-37,-38,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-39,20,20,-44,20,20,20,20,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,20,20,20,20,-41,-42,20,20,]),'L_PAREN':([0,8,9,10,11,14,15,16,17,18,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,84,86,90,91,98,105,],[9,-17,9,-39,-36,45,-18,-19,-20,-21,-37,-38,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,71,-39,9,9,-44,9,9,9,9,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,9,9,9,9,96,-41,-42,9,9,]),'IF':([0,],[24,]),'FOR':([0,],[25,]),'WHILE':([0,],[26,]),'$end':([1,2,3,4,5,6,8,10,11,12,13,15,16,17,18,19,20,43,46,47,52,53,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,78,79,90,91,103,],[0,-1,-2,-3,-4,-5,-17,-39,-36,-45,-46,-18,-19,-20,-21,-37,-38,-39,-44,-47,-53,-54,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,-48,-49,-41,-42,-6,]),'PLUS':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[27,-17,-39,-36,-18,-19,-20,-21,-37,-38,27,-39,27,27,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,27,27,-39,27,27,]),'MINUS':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[28,-17,-39,-36,-18,-19,-20,-21,-37,-38,28,-39,28,28,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,28,28,-39,28,28,]),'MULTIPLICATION':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[29,-17,-39,-36,-18,-19,-20,-21,-37,-38,29,-39,29,29,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,29,29,-39,29,29,]),'DIVIDE':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[30,-17,-39,-36,-18,-19,-20,-21,-37,-38,30,-39,30,30,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,30,30,-39,30,30,]),'EXPONENT':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[31,-17,-39,-36,-18,-19,-20,-21,-37,-38,31,-39,31,31,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,31,31,-39,31,31,]),'MODULE':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[32,-17,-39,-36,-18,-19,-20,-21,-37,-38,32,-39,32,32,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,32,32,-39,32,32,]),'AND_LOGIC':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[33,-17,-39,-36,-18,-19,-20,-21,-37,-38,33,-39,33,33,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,33,33,-39,33,33,]),'OR_LOGIC':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[34,-17,-39,-36,-18,-19,-20,-21,-37,-38,34,-39,34,34,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,34,34,-39,34,34,]),'EQUALITY':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[35,-17,-39,-36,-18,-19,-20,-21,-37,-38,35,-39,35,35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,35,35,-39,35,35,]),'EQUALITY_OF_CASE':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[36,-17,-39,-36,-18,-19,-20,-21,-37,-38,36,-39,36,36,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,36,36,-39,36,36,]),'GREATER_EQUAL':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[37,-17,-39,-36,-18,-19,-20,-21,-37,-38,37,-39,37,37,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,37,37,-39,37,37,]),'GREATER_THAN':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[38,-17,-39,-36,-18,-19,-20,-21,-37,-38,38,-39,38,38,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,38,38,-39,38,38,]),'SMALLER_THAN':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[39,-17,-39,-36,-18,-19,-20,-21,-37,-38,39,-39,39,39,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,39,39,-39,39,39,]),'SMALLER_EQUAL':([4,8,10,11,15,16,17,18,19,20,42,43,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,75,77,83,84,],[40,-17,-39,-36,-18,-19,-20,-21,-37,-38,40,-39,40,40,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,40,40,-39,40,40,]),'EQUAL':([8,10,15,16,17,18,],[-17,44,-18,-19,-20,-21,]),'R_PAREN':([8,11,15,16,17,18,19,20,42,43,45,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,75,77,88,89,100,104,],[-17,-36,-18,-19,-20,-21,-37,-38,72,-39,76,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,90,91,-7,98,-8,105,]),'IN':([8,15,16,17,18,55,],[-17,-18,-19,-20,-21,86,]),'END':([8,10,11,15,16,17,18,19,20,21,22,23,43,46,48,49,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,80,81,82,83,85,87,90,91,92,93,94,95,101,106,],[-17,-39,-36,-18,-19,-20,-21,-37,-38,47,52,53,-39,-44,78,79,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,-52,-9,-11,-13,-50,-56,-41,-42,-10,-12,-14,-51,103,-55,]),'ELSE':([8,10,11,15,16,17,18,19,20,21,43,46,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,85,90,91,92,93,94,],[-17,-39,-36,-18,-19,-20,-21,-37,-38,50,-39,-44,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,-9,-11,-13,-50,-41,-42,-10,-12,-14,]),'ELSIF':([8,10,11,15,16,17,18,19,20,21,43,46,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,76,81,82,83,85,90,91,92,93,94,],[-17,-39,-36,-18,-19,-20,-21,-37,-38,51,-39,-44,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-40,-15,-16,-43,-9,-11,-13,-50,-41,-42,-10,-12,-14,]),'STRING':([14,],[46,]),'GETS':([44,],[74,]),'COMMA':([88,],[97,]),'DOUBLE_POINT':([99,],[102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,],[1,]),'funcion':([0,],[2,]),'declaracion':([0,50,54,56,81,82,83,84,98,105,],[3,81,81,81,81,81,81,81,81,81,]),'expresion':([0,9,24,26,44,45,50,51,54,56,81,82,83,84,98,105,],[4,42,54,56,73,75,83,84,83,83,83,83,83,83,83,83,]),'estructura':([0,],[5,]),'print':([0,50,54,56,81,82,83,84,98,105,],[6,82,82,82,82,82,82,82,82,82,]),'variable':([0,9,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,50,51,54,56,81,82,83,84,98,105,],[10,43,43,55,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,77,10,43,10,10,10,10,10,10,10,10,]),'term':([0,9,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,50,51,54,56,81,82,83,84,98,105,],[11,11,11,11,57,58,59,60,61,62,63,64,65,66,67,68,69,70,11,11,11,11,11,11,11,11,11,11,11,11,]),'estructuraCondicional':([0,],[12,]),'estructuraIterativa':([0,],[13,]),'estructuraif':([0,],[21,]),'sentenciafor':([0,],[22,]),'sentenciawhile':([0,],[23,]),'estructuraelse':([21,],[48,]),'estructuraelseif':([21,],[49,]),'cuerpo':([50,54,56,81,82,83,84,98,105,],[80,85,87,92,93,94,95,101,106,]),'parametros':([71,97,],[89,100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',7),
  ('sentencia -> declaracion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',8),
  ('sentencia -> expresion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',9),
  ('sentencia -> estructura','sentencia',1,'p_sentencia','Analizador_Sintactico.py',10),
  ('sentencia -> print','sentencia',1,'p_sentencia','Analizador_Sintactico.py',11),
  ('funcion -> DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo END','funcion',7,'p_funcion','Analizador_Sintactico.py',17),
  ('parametros -> VARIABLE_LOCAL','parametros',1,'p_parametros','Analizador_Sintactico.py',19),
  ('parametros -> VARIABLE_LOCAL COMMA parametros','parametros',3,'p_parametros','Analizador_Sintactico.py',20),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',22),
  ('cuerpo -> declaracion cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',23),
  ('cuerpo -> print','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',24),
  ('cuerpo -> print cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',25),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',26),
  ('cuerpo -> expresion cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',27),
  ('declaracion -> variable EQUAL expresion','declaracion',3,'p_declaracion','Analizador_Sintactico.py',33),
  ('declaracion -> variable EQUAL GETS','declaracion',3,'p_declaracion_gets','Analizador_Sintactico.py',35),
  ('variable -> VARIABLE_LOCAL','variable',1,'p_variable','Analizador_Sintactico.py',37),
  ('variable -> VARIABLE_INSTANCE','variable',1,'p_variable','Analizador_Sintactico.py',38),
  ('variable -> VARIABLE_CLASS','variable',1,'p_variable','Analizador_Sintactico.py',39),
  ('variable -> VARIABLE_GLOBAL','variable',1,'p_variable','Analizador_Sintactico.py',40),
  ('variable -> CONSTANT','variable',1,'p_variable','Analizador_Sintactico.py',41),
  ('expresion -> expresion PLUS term','expresion',3,'p_expresion_plus','Analizador_Sintactico.py',46),
  ('expresion -> expresion MINUS term','expresion',3,'p_expresion_minus','Analizador_Sintactico.py',48),
  ('expresion -> expresion MULTIPLICATION term','expresion',3,'p_expresion_multiplication','Analizador_Sintactico.py',50),
  ('expresion -> expresion DIVIDE term','expresion',3,'p_expresion_divide','Analizador_Sintactico.py',52),
  ('expresion -> expresion EXPONENT term','expresion',3,'p_expresion_exponent','Analizador_Sintactico.py',54),
  ('expresion -> expresion MODULE term','expresion',3,'p_expresion_module','Analizador_Sintactico.py',56),
  ('expresion -> expresion AND_LOGIC term','expresion',3,'p_expresion_and_logic','Analizador_Sintactico.py',58),
  ('expresion -> expresion OR_LOGIC term','expresion',3,'p_expresion_or_logic','Analizador_Sintactico.py',60),
  ('expresion -> expresion EQUALITY term','expresion',3,'p_expresion_equality','Analizador_Sintactico.py',62),
  ('expresion -> expresion EQUALITY_OF_CASE term','expresion',3,'p_expresion_equality_of_case','Analizador_Sintactico.py',64),
  ('expresion -> expresion GREATER_EQUAL term','expresion',3,'p_expresion_greater_equal','Analizador_Sintactico.py',66),
  ('expresion -> expresion GREATER_THAN term','expresion',3,'p_expresion_greater_than','Analizador_Sintactico.py',68),
  ('expresion -> expresion SMALLER_THAN term','expresion',3,'p_expresion_smaller_than','Analizador_Sintactico.py',70),
  ('expresion -> expresion SMALLER_EQUAL term','expresion',3,'p_expresion_smaller_equal','Analizador_Sintactico.py',72),
  ('expresion -> term','expresion',1,'p_expresion_term','Analizador_Sintactico.py',74),
  ('term -> NUMBER','term',1,'p_term_number','Analizador_Sintactico.py',76),
  ('term -> FLOAT','term',1,'p_term_float','Analizador_Sintactico.py',78),
  ('term -> variable','term',1,'p_term_var','Analizador_Sintactico.py',80),
  ('term -> L_PAREN expresion R_PAREN','term',3,'p_term_expr','Analizador_Sintactico.py',82),
  ('print -> PUTS L_PAREN expresion R_PAREN','print',4,'p_print_exp','Analizador_Sintactico.py',87),
  ('print -> PUTS L_PAREN variable R_PAREN','print',4,'p_print_var','Analizador_Sintactico.py',89),
  ('print -> PUTS L_PAREN R_PAREN','print',3,'p_print_vac','Analizador_Sintactico.py',91),
  ('print -> PUTS STRING','print',2,'p_print_str','Analizador_Sintactico.py',99),
  ('estructura -> estructuraCondicional','estructura',1,'p_estructura','Analizador_Sintactico.py',102),
  ('estructura -> estructuraIterativa','estructura',1,'p_estructura','Analizador_Sintactico.py',103),
  ('estructuraCondicional -> estructuraif END','estructuraCondicional',2,'p_estructuraCondicional','Analizador_Sintactico.py',106),
  ('estructuraCondicional -> estructuraif estructuraelse END','estructuraCondicional',3,'p_estructuraCondicional','Analizador_Sintactico.py',107),
  ('estructuraCondicional -> estructuraif estructuraelseif END','estructuraCondicional',3,'p_estructuraCondicional','Analizador_Sintactico.py',108),
  ('estructuraif -> IF expresion cuerpo','estructuraif',3,'p_estructuraif','Analizador_Sintactico.py',111),
  ('estructuraelseif -> ELSIF expresion cuerpo','estructuraelseif',3,'p_estructuraelsif','Analizador_Sintactico.py',114),
  ('estructuraelse -> ELSE cuerpo','estructuraelse',2,'p_estructuraelse','Analizador_Sintactico.py',117),
  ('estructuraIterativa -> sentenciafor END','estructuraIterativa',2,'p_estructuraIterativa','Analizador_Sintactico.py',121),
  ('estructuraIterativa -> sentenciawhile END','estructuraIterativa',2,'p_estructuraIterativa','Analizador_Sintactico.py',122),
  ('sentenciafor -> FOR variable IN L_PAREN NUMBER DOUBLE_POINT NUMBER R_PAREN cuerpo','sentenciafor',9,'p_sentenciafor','Analizador_Sintactico.py',125),
  ('sentenciawhile -> WHILE expresion cuerpo','sentenciawhile',3,'p_sentenciawhile','Analizador_Sintactico.py',128),
]
