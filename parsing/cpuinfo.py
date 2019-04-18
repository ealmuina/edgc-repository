from .CPUinfoParser import CPUinfoParser
from .CPUinfoVisitor import CPUinfoVisitor


class Evaluator(CPUinfoVisitor):
    def visitFile(self, ctx: CPUinfoParser.FileContext):
        return [self.visit(p) for p in ctx.processor_info()]

    def visitProcessor(self, ctx: CPUinfoParser.ProcessorContext):
        result = {}
        for a in ctx.attribute():
            attr, val = self.visit(a)
            result[attr] = val
        return result

    def visitAttr(self, ctx: CPUinfoParser.AttrContext):
        attr = ctx.TEXT(0).getText()
        val = ctx.TEXT(1).getText() if ctx.TEXT(1) else ''
        return attr, val
