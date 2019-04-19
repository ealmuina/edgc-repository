grammar Meminfo;

/*
 * Parser Rules
 */

compileUnit
    :   attribute+ EOF                                  # File
    ;

attribute
    :   TEXT ':' TEXT 'kB'                              # Attr
    ;

/*
 * Lexer Rules
 */

fragment LETTER		:	[a-zA-Z]			                                                    ;
fragment DIGIT		:	[0-9]				                                                    ;
fragment SYMBOL     :   (LETTER | DIGIT | '_' | '.' | '@' | '(' | ')' | '-' | ',')              ;

TEXT
	:	SYMBOL (SYMBOL | ' ')* SYMBOL
	|   SYMBOL
	;

WS
	:	(' ' | '|') -> skip
	;