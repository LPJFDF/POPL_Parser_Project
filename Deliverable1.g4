
grammar Deliverable1;

program
    : NEWLINE* (statement NEWLINE*)* EOF
    ;

statement
    : assignment
    ;

assignment
    : NAME assignmentOperator expression
    ;

assignmentOperator
    : ASSIGN
    | ADD_ASSIGN
    | SUB_ASSIGN
    | MUL_ASSIGN
    | DIV_ASSIGN
    ;

expression
    : additiveExpression
    ;

additiveExpression
    : multiplicativeExpression ((ADD | SUB) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MUL | DIV | MOD) unaryExpression)*
    ;

unaryExpression
    : ADD unaryExpression
    | SUB unaryExpression
    | primaryExpression
    ;

primaryExpression
    : NUMBER
    | STRING
    | BOOLEAN
    | NAME
    | listLiteral
    | LPAREN expression RPAREN
    ;

listLiteral
    : LBRACKET (expression (COMMA expression)*)? RBRACKET
    ;

// Assignment operators
ASSIGN      : '=';
ADD_ASSIGN  : '+=';
SUB_ASSIGN  : '-=';
MUL_ASSIGN  : '*=';
DIV_ASSIGN  : '/=';

// Arithmetic operators
ADD         : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';

// Delimiters
LPAREN      : '(';
RPAREN      : ')';
LBRACKET    : '[';
RBRACKET    : ']';
COMMA       : ',';

// Literals
BOOLEAN
    : 'True'
    | 'False'
    ;

NUMBER
    : DIGIT+ ('.' DIGIT+)?
    ;

STRING
    : '"' (~["\r\n])* '"'
    | '\'' (~['\r\n])* '\''
    ;

// Identifiers
NAME
    : LETTER (LETTER | DIGIT | '_')*
    ;

// Newlines
NEWLINE
    : '\r'? '\n'
    ;

// Fragments
fragment DIGIT
    : [0-9]
    ;

fragment LETTER
    : [a-zA-Z_]
    ;

// Ignore spaces and tabs
WS
    : [ \t]+ -> skip
    ;
