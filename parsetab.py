
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLPARRPARleftANDORIMPLIESDIMPLIESUNTILrightNEXTEVENTUALLYGLOBALLYrightNOTAND DIMPLIES EVENTUALLY FALSE GLOBALLY IMPLIES LPAR NEXT NOT OR RPAR TERM TRUE UNTIL\n    ltl : expression\n        | empty\n    \n    expression : expression AND expression\n               | expression OR expression\n               | expression IMPLIES expression\n               | expression DIMPLIES expression\n               | expression UNTIL expression\n    \n    expression : NOT expression\n               | NEXT expression\n               | EVENTUALLY expression\n               | GLOBALLY expression\n    \n    expression : LPAR expression RPAR\n    \n    expression : TERM\n               | TRUE\n               | FALSE\n    \n    empty :\n    '
    
_lr_action_items = {'NOT':([0,4,5,6,7,8,12,13,14,15,16,],[4,4,4,4,4,4,4,4,4,4,4,]),'NEXT':([0,4,5,6,7,8,12,13,14,15,16,],[5,5,5,5,5,5,5,5,5,5,5,]),'EVENTUALLY':([0,4,5,6,7,8,12,13,14,15,16,],[6,6,6,6,6,6,6,6,6,6,6,]),'GLOBALLY':([0,4,5,6,7,8,12,13,14,15,16,],[7,7,7,7,7,7,7,7,7,7,7,]),'LPAR':([0,4,5,6,7,8,12,13,14,15,16,],[8,8,8,8,8,8,8,8,8,8,8,]),'TERM':([0,4,5,6,7,8,12,13,14,15,16,],[9,9,9,9,9,9,9,9,9,9,9,]),'TRUE':([0,4,5,6,7,8,12,13,14,15,16,],[10,10,10,10,10,10,10,10,10,10,10,]),'FALSE':([0,4,5,6,7,8,12,13,14,15,16,],[11,11,11,11,11,11,11,11,11,11,11,]),'$end':([0,1,2,3,9,10,11,17,18,19,20,22,23,24,25,26,27,],[-16,0,-1,-2,-13,-14,-15,-8,-9,-10,-11,-3,-4,-5,-6,-7,-12,]),'AND':([2,9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[12,-13,-14,-15,-8,-9,-10,-11,12,-3,-4,-5,-6,-7,-12,]),'OR':([2,9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[13,-13,-14,-15,-8,-9,-10,-11,13,-3,-4,-5,-6,-7,-12,]),'IMPLIES':([2,9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[14,-13,-14,-15,-8,-9,-10,-11,14,-3,-4,-5,-6,-7,-12,]),'DIMPLIES':([2,9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[15,-13,-14,-15,-8,-9,-10,-11,15,-3,-4,-5,-6,-7,-12,]),'UNTIL':([2,9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[16,-13,-14,-15,-8,-9,-10,-11,16,-3,-4,-5,-6,-7,-12,]),'RPAR':([9,10,11,17,18,19,20,21,22,23,24,25,26,27,],[-13,-14,-15,-8,-9,-10,-11,27,-3,-4,-5,-6,-7,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ltl':([0,],[1,]),'expression':([0,4,5,6,7,8,12,13,14,15,16,],[2,17,18,19,20,21,22,23,24,25,26,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ltl","S'",1,None,None,None),
  ('ltl -> expression','ltl',1,'p_ltl','ltl_parser.py',56),
  ('ltl -> empty','ltl',1,'p_ltl','ltl_parser.py',57),
  ('expression -> expression AND expression','expression',3,'p_expr_binary','ltl_parser.py',63),
  ('expression -> expression OR expression','expression',3,'p_expr_binary','ltl_parser.py',64),
  ('expression -> expression IMPLIES expression','expression',3,'p_expr_binary','ltl_parser.py',65),
  ('expression -> expression DIMPLIES expression','expression',3,'p_expr_binary','ltl_parser.py',66),
  ('expression -> expression UNTIL expression','expression',3,'p_expr_binary','ltl_parser.py',67),
  ('expression -> NOT expression','expression',2,'p_expr_unary','ltl_parser.py',74),
  ('expression -> NEXT expression','expression',2,'p_expr_unary','ltl_parser.py',75),
  ('expression -> EVENTUALLY expression','expression',2,'p_expr_unary','ltl_parser.py',76),
  ('expression -> GLOBALLY expression','expression',2,'p_expr_unary','ltl_parser.py',77),
  ('expression -> LPAR expression RPAR','expression',3,'p_expr_group','ltl_parser.py',137),
  ('expression -> TERM','expression',1,'p_expr_term','ltl_parser.py',143),
  ('expression -> TRUE','expression',1,'p_expr_term','ltl_parser.py',144),
  ('expression -> FALSE','expression',1,'p_expr_term','ltl_parser.py',145),
  ('empty -> <empty>','empty',0,'p_empty','ltl_parser.py',151),
]
