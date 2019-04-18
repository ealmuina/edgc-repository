# Generated from D:/Zchool/Computer Science/MSc. Ciencia y Tecnolog�a Inform�tica/II Cuatrimestre/TFM/Elastic DGC/edgc-repository/parsing\CPUinfo.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CPUinfoParser import CPUinfoParser
else:
    from CPUinfoParser import CPUinfoParser


# This class defines a complete generic visitor for a parse tree produced by CPUinfoParser.

class CPUinfoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPUinfoParser#File.
    def visitFile(self, ctx: CPUinfoParser.FileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPUinfoParser#Processor.
    def visitProcessor(self, ctx: CPUinfoParser.ProcessorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CPUinfoParser#Attr.
    def visitAttr(self, ctx: CPUinfoParser.AttrContext):
        return self.visitChildren(ctx)


del CPUinfoParser
