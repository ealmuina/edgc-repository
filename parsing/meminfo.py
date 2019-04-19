from .MeminfoParser import MeminfoParser
from .MeminfoVisitor import MeminfoVisitor


class Evaluator(MeminfoVisitor):
    def visitFile(self, ctx: MeminfoParser.FileContext):
        result = {}
        for a in ctx.attribute():
            attr, val = self.visit(a)
            result[attr] = val
        return result

    def visitAttr(self, ctx: MeminfoParser.AttrContext):
        attr = ctx.TEXT(0).getText()
        val = ctx.TEXT(1).getText() if ctx.TEXT(1) else ''
        return attr, val
