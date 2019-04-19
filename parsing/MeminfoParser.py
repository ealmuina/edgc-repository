# Generated from D:/Zchool/Computer Science/MSc. Ciencia y Tecnolog�a Inform�tica/II Cuatrimestre/TFM/Elastic DGC/edgc-repository/parsing\Meminfo.g4 by ANTLR 4.7.2
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\23\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\21\2\7\3\2\2\2")
        buf.write("\4\r\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3")
        buf.write("\2\2\2\t\n\3\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2")
        buf.write("\2\r\16\7\5\2\2\16\17\7\3\2\2\17\20\7\5\2\2\20\21\7\4")
        buf.write("\2\2\21\5\3\2\2\2\3\t")
        return buf.getvalue()


class MeminfoParser(Parser):
    grammarFileName = "Meminfo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "':'", "'kB'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "TEXT", "WS"]

    RULE_compileUnit = 0
    RULE_attribute = 1

    ruleNames = ["compileUnit", "attribute"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    TEXT = 3
    WS = 4

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class CompileUnitContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return MeminfoParser.RULE_compileUnit

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class FileContext(CompileUnitContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a MeminfoParser.CompileUnitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(MeminfoParser.EOF, 0)

        def attribute(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(MeminfoParser.AttributeContext)
            else:
                return self.getTypedRuleContext(MeminfoParser.AttributeContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile"):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)

    def compileUnit(self):

        localctx = MeminfoParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        self._la = 0  # Token type
        try:
            localctx = MeminfoParser.FileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.attribute()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == MeminfoParser.TEXT):
                    break

            self.state = 9
            self.match(MeminfoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return MeminfoParser.RULE_attribute

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class AttrContext(AttributeContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a MeminfoParser.AttributeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self, i: int = None):
            if i is None:
                return self.getTokens(MeminfoParser.TEXT)
            else:
                return self.getToken(MeminfoParser.TEXT, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttr"):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)

    def attribute(self):

        localctx = MeminfoParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_attribute)
        try:
            localctx = MeminfoParser.AttrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(MeminfoParser.TEXT)
            self.state = 12
            self.match(MeminfoParser.T__0)
            self.state = 13
            self.match(MeminfoParser.TEXT)
            self.state = 14
            self.match(MeminfoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
