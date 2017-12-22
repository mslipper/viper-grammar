# viper-grammar

An attempt to create a custom Viper parser using ANTLR4. This is a **proof of concept**, not production ready software.

## Usage

To regenerate the parser, run `make generate-parser`. This will output the new parser to the `vipergrammar.grammar` module. A copy of the JRE must be installed for this to work.

To parse a contract, run `python vipergrammar/parser.py <file>`, where `<file>` is the path to your source file. The example auction contract from the Viper docs is included in the `example/` directory.