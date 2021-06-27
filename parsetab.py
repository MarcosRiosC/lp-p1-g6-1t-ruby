
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AND_LOGIC BEGIN BREAK CASE CLASS COINCIDENCE COMMA COMPOSITION CONSTANT DEF DIVIDE DO DOUBLE_QUOTE ELIF ELSE END ENSURE EQUAL EQUALITY EQUALITY_OF_CASE EXPONENT FALSE FOR GREATER_EQUAL GREATER_THAN IF IN L_PAREN MINUS MODULE MULTIPLICATION NEGATION NIL NOT NUMBER OR OR_LOGIC PLUS PUTS QUOTATION_MARK RESCUE RETRY RETURN R_PAREN SMALLER_EQUAL SMALLER_THAN THEN TRUE UNLESS UNTIL VARIABLE_CLASS VARIABLE_GLOBAL VARIABLE_INSTANCE VARIABLE_LOCAL WHEN WHILE WRENCH_L WRENCH_Rsentencia : funcion\n                | declaracion\n                | expresion\n                | printfuncion : DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo ENDparametros : VARIABLE_LOCAL\n            | VARIABLE_LOCAL COMMA parametroscuerpo : declaracion\n            | declaracion cuerpo\n            | print\n            | print cuerpo\n            | expresion\n            | expresion cuerpo\n    declaracion : variable EQUAL expresionvariable : VARIABLE_LOCAL\n            | VARIABLE_INSTANCE\n            | VARIABLE_CLASS\n            | VARIABLE_GLOBAL\n            | CONSTANTexpresion : expresion PLUS termexpresion : expresion MINUS termexpresion : expresion MULTIPLICATION termexpresion : expresion DIVIDE termexpresion : expresion EXPONENT termexpresion : expresion MODULE termexpresion : expresion AND_LOGIC termexpresion : expresion OR_LOGIC termexpresion : expresion EQUALITY termexpresion : expresion EQUALITY_OF_CASE termexpresion : expresion GREATER_EQUAL termexpresion : expresion GREATER_THAN termexpresion : expresion SMALLER_THAN termexpresion : expresion SMALLER_EQUAL termexpresion : termterm : NUMBERterm : variableterm : L_PAREN expresion R_PARENprint : PUTS L_PAREN expresion R_PARENprint : PUTS L_PAREN variable R_PARENprint : PUTS L_PAREN R_PAREN'
    
_lr_action_items = {'DEF':([0,],[6,]),'PUTS':([0,7,9,10,12,13,14,15,16,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[11,-15,-36,-34,-16,-17,-18,-19,-35,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,11,11,11,11,]),'VARIABLE_LOCAL':([0,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,58,59,60,61,64,65,66,],[7,31,-15,7,-36,-34,-16,-17,-18,-19,-35,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-36,7,7,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,56,-37,-14,-40,-38,-39,56,7,7,7,7,]),'VARIABLE_INSTANCE':([0,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[12,-15,12,-36,-34,-16,-17,-18,-19,-35,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-36,12,12,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,12,12,12,12,]),'VARIABLE_CLASS':([0,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[13,-15,13,-36,-34,-16,-17,-18,-19,-35,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-36,13,13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,13,13,13,13,]),'VARIABLE_GLOBAL':([0,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[14,-15,14,-36,-34,-16,-17,-18,-19,-35,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-36,14,14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,14,14,14,14,]),'CONSTANT':([0,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[15,-15,15,-36,-34,-16,-17,-18,-19,-35,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-36,15,15,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,15,15,15,15,]),'NUMBER':([0,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[16,-15,16,-36,-34,-16,-17,-18,-19,-35,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-36,16,16,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,16,16,16,16,]),'L_PAREN':([0,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,61,64,65,66,],[8,-15,8,-36,-34,35,-16,-17,-18,-19,-35,8,8,8,8,8,8,8,8,8,8,8,8,8,8,50,-36,8,8,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,8,8,8,8,]),'$end':([1,2,3,4,5,7,9,10,12,13,14,15,16,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,67,],[0,-1,-2,-3,-4,-15,-36,-34,-16,-17,-18,-19,-35,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,-5,]),'PLUS':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[17,-15,-36,-34,-16,-17,-18,-19,-35,17,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,17,17,-36,17,]),'MINUS':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[18,-15,-36,-34,-16,-17,-18,-19,-35,18,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,18,18,-36,18,]),'MULTIPLICATION':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[19,-15,-36,-34,-16,-17,-18,-19,-35,19,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,19,19,-36,19,]),'DIVIDE':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[20,-15,-36,-34,-16,-17,-18,-19,-35,20,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,20,20,-36,20,]),'EXPONENT':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[21,-15,-36,-34,-16,-17,-18,-19,-35,21,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,21,21,-36,21,]),'MODULE':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[22,-15,-36,-34,-16,-17,-18,-19,-35,22,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,22,22,-36,22,]),'AND_LOGIC':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[23,-15,-36,-34,-16,-17,-18,-19,-35,23,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,23,23,-36,23,]),'OR_LOGIC':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[24,-15,-36,-34,-16,-17,-18,-19,-35,24,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,24,24,-36,24,]),'EQUALITY':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[25,-15,-36,-34,-16,-17,-18,-19,-35,25,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,25,25,-36,25,]),'EQUALITY_OF_CASE':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[26,-15,-36,-34,-16,-17,-18,-19,-35,26,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,26,26,-36,26,]),'GREATER_EQUAL':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[27,-15,-36,-34,-16,-17,-18,-19,-35,27,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,27,27,-36,27,]),'GREATER_THAN':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[28,-15,-36,-34,-16,-17,-18,-19,-35,28,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,28,28,-36,28,]),'SMALLER_THAN':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[29,-15,-36,-34,-16,-17,-18,-19,-35,29,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,29,29,-36,29,]),'SMALLER_EQUAL':([4,7,9,10,12,13,14,15,16,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,55,66,],[30,-15,-36,-34,-16,-17,-18,-19,-35,30,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,30,30,-36,30,]),'EQUAL':([7,9,12,13,14,15,],[-15,34,-16,-17,-18,-19,]),'R_PAREN':([7,10,12,13,14,15,16,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,53,55,56,57,62,],[-15,-34,-16,-17,-18,-19,-35,51,-36,54,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,58,59,-6,61,-7,]),'END':([7,9,10,12,13,14,15,16,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,54,58,59,63,64,65,66,68,69,70,],[-15,-36,-34,-16,-17,-18,-19,-35,-36,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-37,-14,-40,-38,-39,67,-8,-10,-12,-9,-11,-13,]),'COMMA':([56,],[60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,],[1,]),'funcion':([0,],[2,]),'declaracion':([0,61,64,65,66,],[3,64,64,64,64,]),'expresion':([0,8,34,35,61,64,65,66,],[4,32,52,53,66,66,66,66,]),'print':([0,61,64,65,66,],[5,65,65,65,65,]),'variable':([0,8,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,35,61,64,65,66,],[9,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,55,9,9,9,9,]),'term':([0,8,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,35,61,64,65,66,],[10,10,36,37,38,39,40,41,42,43,44,45,46,47,48,49,10,10,10,10,10,10,]),'parametros':([50,60,],[57,62,]),'cuerpo':([61,64,65,66,],[63,68,69,70,]),}

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
  ('sentencia -> print','sentencia',1,'p_sentencia','Analizador_Sintactico.py',10),
  ('funcion -> DEF VARIABLE_LOCAL L_PAREN parametros R_PAREN cuerpo END','funcion',7,'p_funcion','Analizador_Sintactico.py',15),
  ('parametros -> VARIABLE_LOCAL','parametros',1,'p_parametros','Analizador_Sintactico.py',17),
  ('parametros -> VARIABLE_LOCAL COMMA parametros','parametros',3,'p_parametros','Analizador_Sintactico.py',18),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',20),
  ('cuerpo -> declaracion cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',21),
  ('cuerpo -> print','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',22),
  ('cuerpo -> print cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',23),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','Analizador_Sintactico.py',24),
  ('cuerpo -> expresion cuerpo','cuerpo',2,'p_cuerpo','Analizador_Sintactico.py',25),
  ('declaracion -> variable EQUAL expresion','declaracion',3,'p_declaracion','Analizador_Sintactico.py',31),
  ('variable -> VARIABLE_LOCAL','variable',1,'p_variable','Analizador_Sintactico.py',33),
  ('variable -> VARIABLE_INSTANCE','variable',1,'p_variable','Analizador_Sintactico.py',34),
  ('variable -> VARIABLE_CLASS','variable',1,'p_variable','Analizador_Sintactico.py',35),
  ('variable -> VARIABLE_GLOBAL','variable',1,'p_variable','Analizador_Sintactico.py',36),
  ('variable -> CONSTANT','variable',1,'p_variable','Analizador_Sintactico.py',37),
  ('expresion -> expresion PLUS term','expresion',3,'p_expresion_plus','Analizador_Sintactico.py',42),
  ('expresion -> expresion MINUS term','expresion',3,'p_expresion_minus','Analizador_Sintactico.py',44),
  ('expresion -> expresion MULTIPLICATION term','expresion',3,'p_expresion_multiplication','Analizador_Sintactico.py',46),
  ('expresion -> expresion DIVIDE term','expresion',3,'p_expresion_divide','Analizador_Sintactico.py',48),
  ('expresion -> expresion EXPONENT term','expresion',3,'p_expresion_exponent','Analizador_Sintactico.py',50),
  ('expresion -> expresion MODULE term','expresion',3,'p_expresion_module','Analizador_Sintactico.py',52),
  ('expresion -> expresion AND_LOGIC term','expresion',3,'p_expresion_and_logic','Analizador_Sintactico.py',54),
  ('expresion -> expresion OR_LOGIC term','expresion',3,'p_expresion_or_logic','Analizador_Sintactico.py',56),
  ('expresion -> expresion EQUALITY term','expresion',3,'p_expresion_equality','Analizador_Sintactico.py',58),
  ('expresion -> expresion EQUALITY_OF_CASE term','expresion',3,'p_expresion_equality_of_case','Analizador_Sintactico.py',60),
  ('expresion -> expresion GREATER_EQUAL term','expresion',3,'p_expresion_greater_equal','Analizador_Sintactico.py',62),
  ('expresion -> expresion GREATER_THAN term','expresion',3,'p_expresion_greater_than','Analizador_Sintactico.py',64),
  ('expresion -> expresion SMALLER_THAN term','expresion',3,'p_expresion_smaller_than','Analizador_Sintactico.py',66),
  ('expresion -> expresion SMALLER_EQUAL term','expresion',3,'p_expresion_smaller_equal','Analizador_Sintactico.py',68),
  ('expresion -> term','expresion',1,'p_expresion_term','Analizador_Sintactico.py',70),
  ('term -> NUMBER','term',1,'p_term_number','Analizador_Sintactico.py',72),
  ('term -> variable','term',1,'p_term_var','Analizador_Sintactico.py',74),
  ('term -> L_PAREN expresion R_PAREN','term',3,'p_term_expr','Analizador_Sintactico.py',76),
  ('print -> PUTS L_PAREN expresion R_PAREN','print',4,'p_print_exp','Analizador_Sintactico.py',81),
  ('print -> PUTS L_PAREN variable R_PAREN','print',4,'p_print_var','Analizador_Sintactico.py',83),
  ('print -> PUTS L_PAREN R_PAREN','print',3,'p_print_vac','Analizador_Sintactico.py',85),
]
