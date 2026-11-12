# Generated from Deliverable1.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Deliverable1Parser import Deliverable1Parser
else:
    from Deliverable1Parser import Deliverable1Parser

# This class defines a complete generic visitor for a parse tree produced by Deliverable1Parser.

class Deliverable1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Deliverable1Parser#program.
    def visitProgram(self, ctx:Deliverable1Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#statement.
    def visitStatement(self, ctx:Deliverable1Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#assignment.
    def visitAssignment(self, ctx:Deliverable1Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:Deliverable1Parser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#expression.
    def visitExpression(self, ctx:Deliverable1Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:Deliverable1Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:Deliverable1Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:Deliverable1Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:Deliverable1Parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Deliverable1Parser#listLiteral.
    def visitListLiteral(self, ctx:Deliverable1Parser.ListLiteralContext):
        return self.visitChildren(ctx)



del Deliverable1Parser