# Generated from Deliverable1.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\7\2$\n\2\f")
        buf.write("\2\16\2\'\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\7\78\n\7\f\7\16\7;\13\7\3\b\3\b\3")
        buf.write("\b\7\b@\n\b\f\b\16\bC\13\b\3\t\3\t\3\t\3\t\3\t\5\tJ\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nU\n\n\3\13\3")
        buf.write("\13\3\13\3\13\7\13[\n\13\f\13\16\13^\13\13\5\13`\n\13")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2")
        buf.write("\3\7\3\2\b\t\3\2\n\f\2g\2\31\3\2\2\2\4*\3\2\2\2\6,\3\2")
        buf.write("\2\2\b\60\3\2\2\2\n\62\3\2\2\2\f\64\3\2\2\2\16<\3\2\2")
        buf.write("\2\20I\3\2\2\2\22T\3\2\2\2\24V\3\2\2\2\26\30\7\26\2\2")
        buf.write("\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2")
        buf.write("\2\32%\3\2\2\2\33\31\3\2\2\2\34 \5\4\3\2\35\37\7\26\2")
        buf.write("\2\36\35\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!$")
        buf.write("\3\2\2\2\" \3\2\2\2#\34\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%")
        buf.write("&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\2\2\3)\3\3\2\2\2*+")
        buf.write("\5\6\4\2+\5\3\2\2\2,-\7\25\2\2-.\5\b\5\2./\5\n\6\2/\7")
        buf.write("\3\2\2\2\60\61\t\2\2\2\61\t\3\2\2\2\62\63\5\f\7\2\63\13")
        buf.write("\3\2\2\2\649\5\16\b\2\65\66\t\3\2\2\668\5\16\b\2\67\65")
        buf.write("\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\r\3\2\2\2;9")
        buf.write("\3\2\2\2<A\5\20\t\2=>\t\4\2\2>@\5\20\t\2?=\3\2\2\2@C\3")
        buf.write("\2\2\2A?\3\2\2\2AB\3\2\2\2B\17\3\2\2\2CA\3\2\2\2DE\7\b")
        buf.write("\2\2EJ\5\20\t\2FG\7\t\2\2GJ\5\20\t\2HJ\5\22\n\2ID\3\2")
        buf.write("\2\2IF\3\2\2\2IH\3\2\2\2J\21\3\2\2\2KU\7\23\2\2LU\7\24")
        buf.write("\2\2MU\7\22\2\2NU\7\25\2\2OU\5\24\13\2PQ\7\r\2\2QR\5\n")
        buf.write("\6\2RS\7\16\2\2SU\3\2\2\2TK\3\2\2\2TL\3\2\2\2TM\3\2\2")
        buf.write("\2TN\3\2\2\2TO\3\2\2\2TP\3\2\2\2U\23\3\2\2\2V_\7\17\2")
        buf.write("\2W\\\5\n\6\2XY\7\21\2\2Y[\5\n\6\2ZX\3\2\2\2[^\3\2\2\2")
        buf.write("\\Z\3\2\2\2\\]\3\2\2\2]`\3\2\2\2^\\\3\2\2\2_W\3\2\2\2")
        buf.write("_`\3\2\2\2`a\3\2\2\2ab\7\20\2\2b\25\3\2\2\2\13\31 %9A")
        buf.write("IT\\_")
        return buf.getvalue()


class Deliverable1Parser ( Parser ):

    grammarFileName = "Deliverable1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "COMMA", "BOOLEAN", "NUMBER", "STRING", "NAME", "NEWLINE", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assignmentOperator = 3
    RULE_expression = 4
    RULE_additiveExpression = 5
    RULE_multiplicativeExpression = 6
    RULE_unaryExpression = 7
    RULE_primaryExpression = 8
    RULE_listLiteral = 9

    ruleNames =  [ "program", "statement", "assignment", "assignmentOperator", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression", "listLiteral" ]

    EOF = Token.EOF
    ASSIGN=1
    ADD_ASSIGN=2
    SUB_ASSIGN=3
    MUL_ASSIGN=4
    DIV_ASSIGN=5
    ADD=6
    SUB=7
    MUL=8
    DIV=9
    MOD=10
    LPAREN=11
    RPAREN=12
    LBRACKET=13
    RBRACKET=14
    COMMA=15
    BOOLEAN=16
    NUMBER=17
    STRING=18
    NAME=19
    NEWLINE=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Deliverable1Parser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.NEWLINE)
            else:
                return self.getToken(Deliverable1Parser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.StatementContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Deliverable1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Deliverable1Parser.NEWLINE:
                self.state = 20
                self.match(Deliverable1Parser.NEWLINE)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Deliverable1Parser.NAME:
                self.state = 26
                self.statement()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Deliverable1Parser.NEWLINE:
                    self.state = 27
                    self.match(Deliverable1Parser.NEWLINE)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(Deliverable1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Deliverable1Parser.AssignmentContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Deliverable1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Deliverable1Parser.NAME, 0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(Deliverable1Parser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = Deliverable1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(Deliverable1Parser.NAME)
            self.state = 43
            self.assignmentOperator()
            self.state = 44
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(Deliverable1Parser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(Deliverable1Parser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(Deliverable1Parser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(Deliverable1Parser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(Deliverable1Parser.DIV_ASSIGN, 0)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = Deliverable1Parser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Deliverable1Parser.ASSIGN) | (1 << Deliverable1Parser.ADD_ASSIGN) | (1 << Deliverable1Parser.SUB_ASSIGN) | (1 << Deliverable1Parser.MUL_ASSIGN) | (1 << Deliverable1Parser.DIV_ASSIGN))) != 0)):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(Deliverable1Parser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Deliverable1Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.MultiplicativeExpressionContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.ADD)
            else:
                return self.getToken(Deliverable1Parser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.SUB)
            else:
                return self.getToken(Deliverable1Parser.SUB, i)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = Deliverable1Parser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.multiplicativeExpression()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Deliverable1Parser.ADD or _la==Deliverable1Parser.SUB:
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==Deliverable1Parser.ADD or _la==Deliverable1Parser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.multiplicativeExpression()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.UnaryExpressionContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.MUL)
            else:
                return self.getToken(Deliverable1Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.DIV)
            else:
                return self.getToken(Deliverable1Parser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.MOD)
            else:
                return self.getToken(Deliverable1Parser.MOD, i)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = Deliverable1Parser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.unaryExpression()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Deliverable1Parser.MUL) | (1 << Deliverable1Parser.DIV) | (1 << Deliverable1Parser.MOD))) != 0):
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Deliverable1Parser.MUL) | (1 << Deliverable1Parser.DIV) | (1 << Deliverable1Parser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.unaryExpression()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(Deliverable1Parser.ADD, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Deliverable1Parser.UnaryExpressionContext,0)


        def SUB(self):
            return self.getToken(Deliverable1Parser.SUB, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(Deliverable1Parser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = Deliverable1Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unaryExpression)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Deliverable1Parser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(Deliverable1Parser.ADD)
                self.state = 67
                self.unaryExpression()
                pass
            elif token in [Deliverable1Parser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(Deliverable1Parser.SUB)
                self.state = 69
                self.unaryExpression()
                pass
            elif token in [Deliverable1Parser.LPAREN, Deliverable1Parser.LBRACKET, Deliverable1Parser.BOOLEAN, Deliverable1Parser.NUMBER, Deliverable1Parser.STRING, Deliverable1Parser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Deliverable1Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(Deliverable1Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(Deliverable1Parser.BOOLEAN, 0)

        def NAME(self):
            return self.getToken(Deliverable1Parser.NAME, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(Deliverable1Parser.ListLiteralContext,0)


        def LPAREN(self):
            return self.getToken(Deliverable1Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Deliverable1Parser.RPAREN, 0)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = Deliverable1Parser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primaryExpression)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Deliverable1Parser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(Deliverable1Parser.NUMBER)
                pass
            elif token in [Deliverable1Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(Deliverable1Parser.STRING)
                pass
            elif token in [Deliverable1Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(Deliverable1Parser.BOOLEAN)
                pass
            elif token in [Deliverable1Parser.NAME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(Deliverable1Parser.NAME)
                pass
            elif token in [Deliverable1Parser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.listLiteral()
                pass
            elif token in [Deliverable1Parser.LPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.match(Deliverable1Parser.LPAREN)
                self.state = 79
                self.expression()
                self.state = 80
                self.match(Deliverable1Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(Deliverable1Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(Deliverable1Parser.RBRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Deliverable1Parser.COMMA)
            else:
                return self.getToken(Deliverable1Parser.COMMA, i)

        def getRuleIndex(self):
            return Deliverable1Parser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = Deliverable1Parser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(Deliverable1Parser.LBRACKET)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Deliverable1Parser.ADD) | (1 << Deliverable1Parser.SUB) | (1 << Deliverable1Parser.LPAREN) | (1 << Deliverable1Parser.LBRACKET) | (1 << Deliverable1Parser.BOOLEAN) | (1 << Deliverable1Parser.NUMBER) | (1 << Deliverable1Parser.STRING) | (1 << Deliverable1Parser.NAME))) != 0):
                self.state = 85
                self.expression()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Deliverable1Parser.COMMA:
                    self.state = 86
                    self.match(Deliverable1Parser.COMMA)
                    self.state = 87
                    self.expression()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 95
            self.match(Deliverable1Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





