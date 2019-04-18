# Generated from D:/Zchool/Computer Science/MSc. Ciencia y Tecnolog�a Inform�tica/II Cuatrimestre/TFM/Elastic DGC/edgc-repository/parsing\CPUinfo.g4 by ANTLR 4.7.2
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\32\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\6\3\17\n\3\r\3\16\3\20\3\3\3\3\3\4\3\4\3\4\5\4\30")
        buf.write("\n\4\3\4\2\2\5\2\4\6\2\3\3\3\3\3\2\31\2\t\3\2\2\2\4\16")
        buf.write("\3\2\2\2\6\24\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2")
        buf.write("\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\17\5\6\4")
        buf.write("\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2\20\21\3\2")
        buf.write("\2\2\21\22\3\2\2\2\22\23\t\2\2\2\23\5\3\2\2\2\24\25\7")
        buf.write("\5\2\2\25\27\7\4\2\2\26\30\7\5\2\2\27\26\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\7\3\2\2\2\5\13\20\27")
        return buf.getvalue()


class CPUinfoParser(Parser):
    grammarFileName = "CPUinfo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'||'", "':'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "TEXT", "WS"]

    RULE_compileUnit = 0
    RULE_processor_info = 1
    RULE_attribute = 2

    ruleNames = ["compileUnit", "processor_info", "attribute"]

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
            return CPUinfoParser.RULE_compileUnit

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class FileContext(CompileUnitContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a CPUinfoParser.CompileUnitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processor_info(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(CPUinfoParser.Processor_infoContext)
            else:
                return self.getTypedRuleContext(CPUinfoParser.Processor_infoContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile"):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)

    def compileUnit(self):

        localctx = CPUinfoParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        self._la = 0  # Token type
        try:
            localctx = CPUinfoParser.FileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.processor_info()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == CPUinfoParser.TEXT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Processor_infoContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return CPUinfoParser.RULE_processor_info

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class ProcessorContext(Processor_infoContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a CPUinfoParser.Processor_infoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(CPUinfoParser.EOF, 0)

        def attribute(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(CPUinfoParser.AttributeContext)
            else:
                return self.getTypedRuleContext(CPUinfoParser.AttributeContext, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProcessor"):
                return visitor.visitProcessor(self)
            else:
                return visitor.visitChildren(self)

    def processor_info(self):

        localctx = CPUinfoParser.Processor_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_processor_info)
        self._la = 0  # Token type
        try:
            localctx = CPUinfoParser.ProcessorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.attribute()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == CPUinfoParser.TEXT):
                    break

            self.state = 16
            _la = self._input.LA(1)
            if not (_la == CPUinfoParser.EOF or _la == CPUinfoParser.T__0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            return CPUinfoParser.RULE_attribute

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class AttrContext(AttributeContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a CPUinfoParser.AttributeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self, i: int = None):
            if i is None:
                return self.getTokens(CPUinfoParser.TEXT)
            else:
                return self.getToken(CPUinfoParser.TEXT, i)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttr"):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)

    def attribute(self):

        localctx = CPUinfoParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_attribute)
        try:
            localctx = CPUinfoParser.AttrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(CPUinfoParser.TEXT)
            self.state = 19
            self.match(CPUinfoParser.T__1)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(CPUinfoParser.TEXT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
