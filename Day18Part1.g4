grammar Day18Part1;

/* * Parser Rules */
expr: expr op=(MUL | ADD) expr #opExpr
| INT #atomExpr
| '('expr')' #braceExpr
;

/* * Lexer Rules */
fragment DIGIT: ('0'..'9');
INT: DIGIT+;
MUL: '*';
ADD: '+';
WS: [\t\r\n ]+ -> skip;