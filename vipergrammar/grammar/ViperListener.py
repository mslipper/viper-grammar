# Generated from vipergrammar/grammar/Viper.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ViperParser import ViperParser
else:
    from ViperParser import ViperParser

# This class defines a complete listener for a parse tree produced by ViperParser.
class ViperListener(ParseTreeListener):

    # Enter a parse tree produced by ViperParser#single_input.
    def enterSingle_input(self, ctx:ViperParser.Single_inputContext):
        pass

    # Exit a parse tree produced by ViperParser#single_input.
    def exitSingle_input(self, ctx:ViperParser.Single_inputContext):
        pass


    # Enter a parse tree produced by ViperParser#file_input.
    def enterFile_input(self, ctx:ViperParser.File_inputContext):
        pass

    # Exit a parse tree produced by ViperParser#file_input.
    def exitFile_input(self, ctx:ViperParser.File_inputContext):
        pass


    # Enter a parse tree produced by ViperParser#eval_input.
    def enterEval_input(self, ctx:ViperParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by ViperParser#eval_input.
    def exitEval_input(self, ctx:ViperParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by ViperParser#decorator.
    def enterDecorator(self, ctx:ViperParser.DecoratorContext):
        pass

    # Exit a parse tree produced by ViperParser#decorator.
    def exitDecorator(self, ctx:ViperParser.DecoratorContext):
        pass


    # Enter a parse tree produced by ViperParser#decorators.
    def enterDecorators(self, ctx:ViperParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by ViperParser#decorators.
    def exitDecorators(self, ctx:ViperParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by ViperParser#decorated.
    def enterDecorated(self, ctx:ViperParser.DecoratedContext):
        pass

    # Exit a parse tree produced by ViperParser#decorated.
    def exitDecorated(self, ctx:ViperParser.DecoratedContext):
        pass


    # Enter a parse tree produced by ViperParser#funcdef.
    def enterFuncdef(self, ctx:ViperParser.FuncdefContext):
        pass

    # Exit a parse tree produced by ViperParser#funcdef.
    def exitFuncdef(self, ctx:ViperParser.FuncdefContext):
        pass


    # Enter a parse tree produced by ViperParser#parameters.
    def enterParameters(self, ctx:ViperParser.ParametersContext):
        pass

    # Exit a parse tree produced by ViperParser#parameters.
    def exitParameters(self, ctx:ViperParser.ParametersContext):
        pass


    # Enter a parse tree produced by ViperParser#typedargslist.
    def enterTypedargslist(self, ctx:ViperParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by ViperParser#typedargslist.
    def exitTypedargslist(self, ctx:ViperParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by ViperParser#tfpdef.
    def enterTfpdef(self, ctx:ViperParser.TfpdefContext):
        pass

    # Exit a parse tree produced by ViperParser#tfpdef.
    def exitTfpdef(self, ctx:ViperParser.TfpdefContext):
        pass


    # Enter a parse tree produced by ViperParser#varargslist.
    def enterVarargslist(self, ctx:ViperParser.VarargslistContext):
        pass

    # Exit a parse tree produced by ViperParser#varargslist.
    def exitVarargslist(self, ctx:ViperParser.VarargslistContext):
        pass


    # Enter a parse tree produced by ViperParser#vfpdef.
    def enterVfpdef(self, ctx:ViperParser.VfpdefContext):
        pass

    # Exit a parse tree produced by ViperParser#vfpdef.
    def exitVfpdef(self, ctx:ViperParser.VfpdefContext):
        pass


    # Enter a parse tree produced by ViperParser#stmt.
    def enterStmt(self, ctx:ViperParser.StmtContext):
        pass

    # Exit a parse tree produced by ViperParser#stmt.
    def exitStmt(self, ctx:ViperParser.StmtContext):
        pass


    # Enter a parse tree produced by ViperParser#simple_stmt.
    def enterSimple_stmt(self, ctx:ViperParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#simple_stmt.
    def exitSimple_stmt(self, ctx:ViperParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#small_stmt.
    def enterSmall_stmt(self, ctx:ViperParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#small_stmt.
    def exitSmall_stmt(self, ctx:ViperParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#expr_stmt.
    def enterExpr_stmt(self, ctx:ViperParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#expr_stmt.
    def exitExpr_stmt(self, ctx:ViperParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:ViperParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:ViperParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#augassign.
    def enterAugassign(self, ctx:ViperParser.AugassignContext):
        pass

    # Exit a parse tree produced by ViperParser#augassign.
    def exitAugassign(self, ctx:ViperParser.AugassignContext):
        pass


    # Enter a parse tree produced by ViperParser#del_stmt.
    def enterDel_stmt(self, ctx:ViperParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#del_stmt.
    def exitDel_stmt(self, ctx:ViperParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#pass_stmt.
    def enterPass_stmt(self, ctx:ViperParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#pass_stmt.
    def exitPass_stmt(self, ctx:ViperParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#flow_stmt.
    def enterFlow_stmt(self, ctx:ViperParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#flow_stmt.
    def exitFlow_stmt(self, ctx:ViperParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#break_stmt.
    def enterBreak_stmt(self, ctx:ViperParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#break_stmt.
    def exitBreak_stmt(self, ctx:ViperParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#continue_stmt.
    def enterContinue_stmt(self, ctx:ViperParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#continue_stmt.
    def exitContinue_stmt(self, ctx:ViperParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#return_stmt.
    def enterReturn_stmt(self, ctx:ViperParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#return_stmt.
    def exitReturn_stmt(self, ctx:ViperParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#yield_stmt.
    def enterYield_stmt(self, ctx:ViperParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#yield_stmt.
    def exitYield_stmt(self, ctx:ViperParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#raise_stmt.
    def enterRaise_stmt(self, ctx:ViperParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#raise_stmt.
    def exitRaise_stmt(self, ctx:ViperParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#import_stmt.
    def enterImport_stmt(self, ctx:ViperParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#import_stmt.
    def exitImport_stmt(self, ctx:ViperParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#import_name.
    def enterImport_name(self, ctx:ViperParser.Import_nameContext):
        pass

    # Exit a parse tree produced by ViperParser#import_name.
    def exitImport_name(self, ctx:ViperParser.Import_nameContext):
        pass


    # Enter a parse tree produced by ViperParser#import_from.
    def enterImport_from(self, ctx:ViperParser.Import_fromContext):
        pass

    # Exit a parse tree produced by ViperParser#import_from.
    def exitImport_from(self, ctx:ViperParser.Import_fromContext):
        pass


    # Enter a parse tree produced by ViperParser#import_as_name.
    def enterImport_as_name(self, ctx:ViperParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by ViperParser#import_as_name.
    def exitImport_as_name(self, ctx:ViperParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by ViperParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:ViperParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by ViperParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:ViperParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by ViperParser#import_as_names.
    def enterImport_as_names(self, ctx:ViperParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by ViperParser#import_as_names.
    def exitImport_as_names(self, ctx:ViperParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by ViperParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:ViperParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by ViperParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:ViperParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by ViperParser#dotted_name.
    def enterDotted_name(self, ctx:ViperParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by ViperParser#dotted_name.
    def exitDotted_name(self, ctx:ViperParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by ViperParser#global_stmt.
    def enterGlobal_stmt(self, ctx:ViperParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#global_stmt.
    def exitGlobal_stmt(self, ctx:ViperParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#contract_global_stmt.
    def enterContract_global_stmt(self, ctx:ViperParser.Contract_global_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#contract_global_stmt.
    def exitContract_global_stmt(self, ctx:ViperParser.Contract_global_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:ViperParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:ViperParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#assert_stmt.
    def enterAssert_stmt(self, ctx:ViperParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#assert_stmt.
    def exitAssert_stmt(self, ctx:ViperParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#compound_stmt.
    def enterCompound_stmt(self, ctx:ViperParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#compound_stmt.
    def exitCompound_stmt(self, ctx:ViperParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#if_stmt.
    def enterIf_stmt(self, ctx:ViperParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#if_stmt.
    def exitIf_stmt(self, ctx:ViperParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#while_stmt.
    def enterWhile_stmt(self, ctx:ViperParser.While_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#while_stmt.
    def exitWhile_stmt(self, ctx:ViperParser.While_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#for_stmt.
    def enterFor_stmt(self, ctx:ViperParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#for_stmt.
    def exitFor_stmt(self, ctx:ViperParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#try_stmt.
    def enterTry_stmt(self, ctx:ViperParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#try_stmt.
    def exitTry_stmt(self, ctx:ViperParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#with_stmt.
    def enterWith_stmt(self, ctx:ViperParser.With_stmtContext):
        pass

    # Exit a parse tree produced by ViperParser#with_stmt.
    def exitWith_stmt(self, ctx:ViperParser.With_stmtContext):
        pass


    # Enter a parse tree produced by ViperParser#with_item.
    def enterWith_item(self, ctx:ViperParser.With_itemContext):
        pass

    # Exit a parse tree produced by ViperParser#with_item.
    def exitWith_item(self, ctx:ViperParser.With_itemContext):
        pass


    # Enter a parse tree produced by ViperParser#except_clause.
    def enterExcept_clause(self, ctx:ViperParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by ViperParser#except_clause.
    def exitExcept_clause(self, ctx:ViperParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by ViperParser#suite.
    def enterSuite(self, ctx:ViperParser.SuiteContext):
        pass

    # Exit a parse tree produced by ViperParser#suite.
    def exitSuite(self, ctx:ViperParser.SuiteContext):
        pass


    # Enter a parse tree produced by ViperParser#test.
    def enterTest(self, ctx:ViperParser.TestContext):
        pass

    # Exit a parse tree produced by ViperParser#test.
    def exitTest(self, ctx:ViperParser.TestContext):
        pass


    # Enter a parse tree produced by ViperParser#test_nocond.
    def enterTest_nocond(self, ctx:ViperParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by ViperParser#test_nocond.
    def exitTest_nocond(self, ctx:ViperParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by ViperParser#lambdef.
    def enterLambdef(self, ctx:ViperParser.LambdefContext):
        pass

    # Exit a parse tree produced by ViperParser#lambdef.
    def exitLambdef(self, ctx:ViperParser.LambdefContext):
        pass


    # Enter a parse tree produced by ViperParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:ViperParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by ViperParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:ViperParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by ViperParser#or_test.
    def enterOr_test(self, ctx:ViperParser.Or_testContext):
        pass

    # Exit a parse tree produced by ViperParser#or_test.
    def exitOr_test(self, ctx:ViperParser.Or_testContext):
        pass


    # Enter a parse tree produced by ViperParser#and_test.
    def enterAnd_test(self, ctx:ViperParser.And_testContext):
        pass

    # Exit a parse tree produced by ViperParser#and_test.
    def exitAnd_test(self, ctx:ViperParser.And_testContext):
        pass


    # Enter a parse tree produced by ViperParser#not_test.
    def enterNot_test(self, ctx:ViperParser.Not_testContext):
        pass

    # Exit a parse tree produced by ViperParser#not_test.
    def exitNot_test(self, ctx:ViperParser.Not_testContext):
        pass


    # Enter a parse tree produced by ViperParser#comparison.
    def enterComparison(self, ctx:ViperParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ViperParser#comparison.
    def exitComparison(self, ctx:ViperParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ViperParser#comp_op.
    def enterComp_op(self, ctx:ViperParser.Comp_opContext):
        pass

    # Exit a parse tree produced by ViperParser#comp_op.
    def exitComp_op(self, ctx:ViperParser.Comp_opContext):
        pass


    # Enter a parse tree produced by ViperParser#star_expr.
    def enterStar_expr(self, ctx:ViperParser.Star_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#star_expr.
    def exitStar_expr(self, ctx:ViperParser.Star_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#expr.
    def enterExpr(self, ctx:ViperParser.ExprContext):
        pass

    # Exit a parse tree produced by ViperParser#expr.
    def exitExpr(self, ctx:ViperParser.ExprContext):
        pass


    # Enter a parse tree produced by ViperParser#xor_expr.
    def enterXor_expr(self, ctx:ViperParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#xor_expr.
    def exitXor_expr(self, ctx:ViperParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#and_expr.
    def enterAnd_expr(self, ctx:ViperParser.And_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#and_expr.
    def exitAnd_expr(self, ctx:ViperParser.And_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#shift_expr.
    def enterShift_expr(self, ctx:ViperParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#shift_expr.
    def exitShift_expr(self, ctx:ViperParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#arith_expr.
    def enterArith_expr(self, ctx:ViperParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#arith_expr.
    def exitArith_expr(self, ctx:ViperParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#term.
    def enterTerm(self, ctx:ViperParser.TermContext):
        pass

    # Exit a parse tree produced by ViperParser#term.
    def exitTerm(self, ctx:ViperParser.TermContext):
        pass


    # Enter a parse tree produced by ViperParser#factor.
    def enterFactor(self, ctx:ViperParser.FactorContext):
        pass

    # Exit a parse tree produced by ViperParser#factor.
    def exitFactor(self, ctx:ViperParser.FactorContext):
        pass


    # Enter a parse tree produced by ViperParser#power.
    def enterPower(self, ctx:ViperParser.PowerContext):
        pass

    # Exit a parse tree produced by ViperParser#power.
    def exitPower(self, ctx:ViperParser.PowerContext):
        pass


    # Enter a parse tree produced by ViperParser#atom.
    def enterAtom(self, ctx:ViperParser.AtomContext):
        pass

    # Exit a parse tree produced by ViperParser#atom.
    def exitAtom(self, ctx:ViperParser.AtomContext):
        pass


    # Enter a parse tree produced by ViperParser#testlist_comp.
    def enterTestlist_comp(self, ctx:ViperParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by ViperParser#testlist_comp.
    def exitTestlist_comp(self, ctx:ViperParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by ViperParser#trailer.
    def enterTrailer(self, ctx:ViperParser.TrailerContext):
        pass

    # Exit a parse tree produced by ViperParser#trailer.
    def exitTrailer(self, ctx:ViperParser.TrailerContext):
        pass


    # Enter a parse tree produced by ViperParser#subscriptlist.
    def enterSubscriptlist(self, ctx:ViperParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by ViperParser#subscriptlist.
    def exitSubscriptlist(self, ctx:ViperParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by ViperParser#subscript.
    def enterSubscript(self, ctx:ViperParser.SubscriptContext):
        pass

    # Exit a parse tree produced by ViperParser#subscript.
    def exitSubscript(self, ctx:ViperParser.SubscriptContext):
        pass


    # Enter a parse tree produced by ViperParser#sliceop.
    def enterSliceop(self, ctx:ViperParser.SliceopContext):
        pass

    # Exit a parse tree produced by ViperParser#sliceop.
    def exitSliceop(self, ctx:ViperParser.SliceopContext):
        pass


    # Enter a parse tree produced by ViperParser#exprlist.
    def enterExprlist(self, ctx:ViperParser.ExprlistContext):
        pass

    # Exit a parse tree produced by ViperParser#exprlist.
    def exitExprlist(self, ctx:ViperParser.ExprlistContext):
        pass


    # Enter a parse tree produced by ViperParser#testlist.
    def enterTestlist(self, ctx:ViperParser.TestlistContext):
        pass

    # Exit a parse tree produced by ViperParser#testlist.
    def exitTestlist(self, ctx:ViperParser.TestlistContext):
        pass


    # Enter a parse tree produced by ViperParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:ViperParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by ViperParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:ViperParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by ViperParser#classdef.
    def enterClassdef(self, ctx:ViperParser.ClassdefContext):
        pass

    # Exit a parse tree produced by ViperParser#classdef.
    def exitClassdef(self, ctx:ViperParser.ClassdefContext):
        pass


    # Enter a parse tree produced by ViperParser#arglist.
    def enterArglist(self, ctx:ViperParser.ArglistContext):
        pass

    # Exit a parse tree produced by ViperParser#arglist.
    def exitArglist(self, ctx:ViperParser.ArglistContext):
        pass


    # Enter a parse tree produced by ViperParser#argument.
    def enterArgument(self, ctx:ViperParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ViperParser#argument.
    def exitArgument(self, ctx:ViperParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ViperParser#comp_iter.
    def enterComp_iter(self, ctx:ViperParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by ViperParser#comp_iter.
    def exitComp_iter(self, ctx:ViperParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by ViperParser#comp_for.
    def enterComp_for(self, ctx:ViperParser.Comp_forContext):
        pass

    # Exit a parse tree produced by ViperParser#comp_for.
    def exitComp_for(self, ctx:ViperParser.Comp_forContext):
        pass


    # Enter a parse tree produced by ViperParser#comp_if.
    def enterComp_if(self, ctx:ViperParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by ViperParser#comp_if.
    def exitComp_if(self, ctx:ViperParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by ViperParser#yield_expr.
    def enterYield_expr(self, ctx:ViperParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by ViperParser#yield_expr.
    def exitYield_expr(self, ctx:ViperParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by ViperParser#yield_arg.
    def enterYield_arg(self, ctx:ViperParser.Yield_argContext):
        pass

    # Exit a parse tree produced by ViperParser#yield_arg.
    def exitYield_arg(self, ctx:ViperParser.Yield_argContext):
        pass


    # Enter a parse tree produced by ViperParser#strr.
    def enterStrr(self, ctx:ViperParser.StrrContext):
        pass

    # Exit a parse tree produced by ViperParser#strr.
    def exitStrr(self, ctx:ViperParser.StrrContext):
        pass


    # Enter a parse tree produced by ViperParser#number.
    def enterNumber(self, ctx:ViperParser.NumberContext):
        pass

    # Exit a parse tree produced by ViperParser#number.
    def exitNumber(self, ctx:ViperParser.NumberContext):
        pass


    # Enter a parse tree produced by ViperParser#integer.
    def enterInteger(self, ctx:ViperParser.IntegerContext):
        pass

    # Exit a parse tree produced by ViperParser#integer.
    def exitInteger(self, ctx:ViperParser.IntegerContext):
        pass


