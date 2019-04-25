# Generated from D:/Zchool/Computer Science/MSc. Ciencia y Tecnolog�a Inform�tica/II Cuatrimestre/TFM/Elastic DGC/edgc-repository/parsing\Meminfo.g4 by ANTLR 4.7.2
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\5\6\36\n\6\3\7\3\7\3\7\7\7#\n\7\f\7\16\7&\13\7\3")
        buf.write("\7\3\7\3\7\5\7+\n\7\3\b\3\b\3\b\3\b\2\2\t\3\3\5\4\7\2")
        buf.write("\t\2\13\2\r\5\17\6\3\2\6\4\2C\\c|\3\2\62;\6\2*+.\60BB")
        buf.write("aa\4\2\"\"~~\2\61\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\26\3\2\2\2\t")
        buf.write("\30\3\2\2\2\13\35\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21\22")
        buf.write("\7<\2\2\22\4\3\2\2\2\23\24\7m\2\2\24\25\7D\2\2\25\6\3")
        buf.write("\2\2\2\26\27\t\2\2\2\27\b\3\2\2\2\30\31\t\3\2\2\31\n\3")
        buf.write("\2\2\2\32\36\5\7\4\2\33\36\5\t\5\2\34\36\t\4\2\2\35\32")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36\f\3\2\2\2\37$")
        buf.write("\5\13\6\2 #\5\13\6\2!#\7\"\2\2\" \3\2\2\2\"!\3\2\2\2#")
        buf.write("&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'")
        buf.write("(\5\13\6\2(+\3\2\2\2)+\5\13\6\2*\37\3\2\2\2*)\3\2\2\2")
        buf.write("+\16\3\2\2\2,-\t\5\2\2-.\3\2\2\2./\b\b\2\2/\20\3\2\2\2")
        buf.write("\7\2\35\"$*\3\b\2\2")
        return buf.getvalue()


class MeminfoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    TEXT = 3
    WS = 4

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "':'", "'kB'"]

    symbolicNames = ["<INVALID>",
                     "TEXT", "WS"]

    ruleNames = ["T__0", "T__1", "LETTER", "DIGIT", "SYMBOL", "TEXT", "WS"]

    grammarFileName = "Meminfo.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
