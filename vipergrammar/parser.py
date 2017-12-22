import sys
from antlr4 import *
from grammar.ViperLexer import ViperLexer
from grammar.ViperParser import ViperParser
from grammar.ViperListener import ViperListener


def parse(file):
    print('Parsing file %s' % file)
    lexer = ViperLexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = ViperParser(stream)
    return parser.file_input()

def get_contracts_and_defs_and_globals(tree):
    _defs = []
    _globals = []

    class ExtractorListener(ViperListener):
      def enterFuncdef(self, ctx:ViperParser.FuncdefContext):
          _defs.append(ctx)

      def enterContract_global_stmt(self, ctx:ViperParser.Contract_global_stmtContext):
          _globals.append(ctx)

    walker = ParseTreeWalker()
    walker.walk(ExtractorListener(), tree)

    return _defs, _globals


def main(file):
    tree = parse(file)
    defs, globals = get_contracts_and_defs_and_globals(tree)
    print(defs)
    print(globals)


if __name__ == '__main__':
    main(sys.argv[1])
