grammar CPUinfo;

/*
 * Parser Rules
 */

compileUnit
    :   processor_info+                                 # File
    ;

processor_info
    :   attribute+ ('||' | EOF)                         # Processor
    ;

attribute
    :   TEXT ':' TEXT?                                  # Attr
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