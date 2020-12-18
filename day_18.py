#%% Part1
# Before using this you have to run `antlr4 -Dlanguage=Python3 -no-listener -visitor Day18Part1.g4`
from antlr4 import InputStream, CommonTokenStream, ParseTreeVisitor
from Day18Part1Lexer import Day18Part1Lexer
from Day18Part1Parser import Day18Part1Parser
from Day18Part1Visitor import Day18Part1Visitor
from Day18Part2Lexer import Day18Part2Lexer
from Day18Part2Parser import Day18Part2Parser
from Day18Part2Visitor import Day18Part2Visitor


class Day18Part1ExprVisitor(Day18Part1Visitor):
    def visitOpExpr(self, ctx: Day18Part1Parser.OpExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right

    def visitAtomExpr(self, ctx: Day18Part1Parser.AtomExprContext):
        return int(ctx.getText())

    def visitBraceExpr(self, ctx: Day18Part1Parser.BraceExprContext):
        return self.visit(ctx.expr())


lexer = Day18Part1Lexer()
parser = Day18Part1Parser(CommonTokenStream(lexer))
visitor = Day18Part1ExprVisitor()

with open("day_18_input.txt") as input_data:
    result = []
    for line in input_data:
        lexer.inputStream = InputStream(line.strip())
        parser.setTokenStream(CommonTokenStream(lexer))
        result.append(visitor.visit(parser.expr()))

print(f"Sum of all results: {sum(result)}")


#%%
# Before using this you have to run `antlr4 -Dlanguage=Python3 -no-listener -visitor Day18Part2.g4`
class Day18Part2ExprVisitor(Day18Part2Visitor):
    def visitOpExpr(self, ctx: Day18Part2Parser.OpExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right

    def visitAtomExpr(self, ctx: Day18Part2Parser.AtomExprContext):
        return int(ctx.getText())

    def visitBraceExpr(self, ctx: Day18Part2Parser.BraceExprContext):
        return self.visit(ctx.expr())


lexer = Day18Part2Lexer()
parser = Day18Part2Parser(CommonTokenStream(lexer))
visitor = Day18Part2ExprVisitor()

with open("day_18_input.txt") as input_data:
    result = []
    for line in input_data:
        lexer.inputStream = InputStream(line.strip())
        parser.setTokenStream(CommonTokenStream(lexer))
        result.append(visitor.visit(parser.expr()))

print(f"Sum of all results: {sum(result)}")
