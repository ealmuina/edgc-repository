# Generated from D:/Zchool/Computer Science/MSc. Ciencia y Tecnolog�a Inform�tica/II Cuatrimestre/TFM/Elastic DGC/edgc-repository/parsing\Meminfo.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .MeminfoParser import MeminfoParser
else:
    from MeminfoParser import MeminfoParser


# This class defines a complete generic visitor for a parse tree produced by MeminfoParser.

class MeminfoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MeminfoParser#File.
    def visitFile(self, ctx: MeminfoParser.FileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MeminfoParser#Attr.
    def visitAttr(self, ctx: MeminfoParser.AttrContext):
        return self.visitChildren(ctx)


del MeminfoParser
