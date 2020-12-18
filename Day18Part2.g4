grammar Day18Part2;

/* * Parser Rules */
expr: expr op=ADD expr #opExpr
| expr op=MUL expr #opExpr
| INT #atomExpr
| '('expr')' #braceExpr
;

/* * Lexer Rules */
INT: ('0'..'9')+;
MUL: '*';
ADD: '+';
WS: [\t\r\n ]+ -> skip;