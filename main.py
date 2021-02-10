#!/usr/local/bin/python3.9

# cli syntax - provides syntax information and history from the command line

import argparse


class ProgrammingLanguage:
    def __init__(self, name, paradigm, typing, creators, first_appeared, history, wiki_link, version):
        self.name = name  # both
        self.paradigm = paradigm  # technical
        self.typing = typing  # technical
        self.creators = creators  # historical
        self.first_appeared = first_appeared  # historical
        self.history = history  # historical
        self.wiki_link = wiki_link  # both
        self.version = version

    def output_language_classifications(self):
        print(self.name + " is a " + self.paradigm + " language with " + self.typing + " typing discipline"
              "for more information, visit the language's wikipedia page: " + self.wiki_link +
              "\nThe version represented here is: " + self.version)

    def output_historical_information(self):
        print(self.name + " was created by " + self.creators + "; first appearing in " + self.first_appeared + ". "
              "\nWikipedia writes: " + self.history)


class LanguageSyntax:
    def __init__(self, options_list, keywords, data_types, operators, for_loop, while_loop, case_statement,
                 class_definition, define_variable, array, function_definition, control_flow, user_input, output,
                 arithmetic, arithmetic_operators, comparison_operators, logical_operators, builtin_functions,
                 hello_world):
        self.options = options_list
        self.keywords = keywords
        self.data_types = data_types
        self.operators = operators
        self.for_loop = for_loop
        self.while_loop = while_loop
        self.case_statement = case_statement
        self.class_definition = class_definition
        self.variable_definition = define_variable
        self.array = array
        self.function_definition = function_definition
        self.control_flow = control_flow
        self.user_input = user_input
        self.output = output
        self.arithmetic = arithmetic
        self.arithmetic_operators = arithmetic_operators
        self.comparison_operators = comparison_operators
        self.logical_operators = logical_operators
        self.builtin_functions = builtin_functions
        self.hello_world = hello_world

    def display_syntax_selection_options(self):
        print("list of common syntax options\n" + str(options_list))

    def return_not_available(self, structure_in_question):
        print("Error: " + str(structure_in_question) + " is not available currently")

    def not_a_part_of_language(self, structure_in_question):
        print("Error: " + str(structure_in_question) + " is not a part of the language")


# ProgrammingLanguage object instantiations

LISP_lang = ProgrammingLanguage("Common LISP", "Multi-paradigm: functional, procedural, reflective, meta",
                                "Dynamic, strong", "John McCarthy", "1958",
                                "John McCarthy developed Lisp in 1958 while at"
                                " the Massachusetts Institute of Technology (MIT)",
                                "https://en.wikipedia.org/wiki/Lisp_(programming_language)",
                                "Common LISP")

bash_lang = ProgrammingLanguage("bash", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

python3_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "python3.9")

javascript_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

c_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

cpp_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

java_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

perl_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

ruby_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")

skeleton_lang = ProgrammingLanguage("name", "paradigm", "typing", "creators", "firstappeared", "history", "wikilink", "version")


# Variable definitions
dash_band = "-------------------------------------------------------\n"
options_list = ["options", "keywords", "data types", "operators", "forloop", "whileloop",
                "casestatements", "classdefinition", "variabledefinition", "arrays",
                "functiondefinition", "controlflow", "userinput", "output", "arithmetic",
                "arithmeticoperators", "comparisonoperators", "logicaloperators",
                "builtinfunctions", "helloworld"]

# LanguageSyntax object class instantiations

LISP_syntax = LanguageSyntax("options",
                             "keywords",
                             "DATA TYPES:\nScalar types: number types, chars, symbols\n"
                             "Data structures: lists, vectors, bit-vectors, strings\n",

                             "Arithmetic Operators:\n+\t-\t*\t/\nmod\tincf\tdecf\t\n\n"
                             "Comparison Operators:\n=\t/=\t>\t<\n>=\t<=\tmax\tmin\n\n"
                             "Logical Operators:\n(and A B)\t(or A B)\t(not A B)\t\n",
                             "FOR LOOPS in LISP:\n\n"
                             "1st variant:\n"
                             "(loop for [loopvar] in [list]\n\tdo (action))\n"
                             "2nd variant:\n"
                             "(loop for [loopvar] from [value1] to [value2]\n\tdo (action))\n",

                             "WHILE LOOP:\n"
                             "(setq a 10)\n(loop \n\t(setq a (+ a 1))\n\t(write a)\n\t(terpri)"
                             "\n\t(when (> a 17) (return a))\n)",

                             "(case (keyform)\n"
                             "((key1)   (action1   action2 ...) )\n"
                             "((key2)   (action1   action2 ...) )\n"
                             "...\n"
                             "((keyn)   (action1   action2 ...) ))\n",

                             "CLASS DEFINITION:\n(defclass class-name (superclass-name*)\n"
                             "(slot-description*)\n"
                             "class-option*))\n",

                             "variable definition:\nGlobal variables are generally set with 'defvar'\n"
                             "(defvar x 234)\n(write x)\n"
                             "Since there is no type declaration for variables in LISP, "
                             "you directly specify a value for a symbol with the setq construct:\n"
                             "(setq x 10)\t(write-line x)",

                             "ARRAYS:\n"
                             "To create an array with 10 cells:\n(setf my-array (array_name '(10)))\n"
                             "To access content of the tenth item in that array:\n(aref array_name 9)\n"
                             "To print an array\n(write array_name)\n",

                             "(defun function_name (param0 param1 param2) \"function comment\" body)"
                             "\n\nFunction call:\n\n(function_name param0 param1 param2)",

                             "control flow",

                             "Store user-input in a variable:\n"
                             "(defvar inputvar (read))\n",

                             "OUTPUT IN LISP:\n(defvar x 250)\n(write x)\t(print x)\t(write-line x)\n"
                             "(format t \"~a\" x)\n",

                             "ARITHMETIC EXAMPLES:\n(+ 10 12)\t(mod 36 6)\t(* 12 12)\n(/ 40 4)\t(- 6 4)\t\t(rem 12 5)",
                             "ARITHMETIC OPERATORS:\t+, -, *, /, mod, rem",

                             "comparison operators",

                             "logical operators",

                             "builtin functions",

                             "#! /usr/bin/clisp\n\n(write-line \"hello, world\")")


bash_syntax = LanguageSyntax("options",
                             "keywords",
                             "data types",
                             "operators",
                             "forloop",
                             "whileloop",
                             "case statements",
                             "class definition",
                             "variable definition",
                             "arrays",
                             "function definition",
                             "control flow",
                             "user input",
                             "output",
                             "arithmetic",
                             "arithmetic operators",
                             "comparison operators",
                             "logical operators",
                             "builtin functions",
                             "hello world")


python3_syntax = LanguageSyntax("options",
                                "Keywords\tdescription\n" + dash_band +
                                "and\t:\tlogical operator\n"
                                "as\t:\tto create an alias\n"
                                "assert\t:\tfor debugging\n"
                                "break\t:\tbreak out of loop\n" + dash_band,
                                "data types",
                                "operators",
                                "forloop",
                                "whileloop",
                                "case statements",
                                "class definition",
                                "variable definition",
                                "arrays",
                                "function definition",
                                "control flow",
                                "user input",
                                "output",
                                "arithmetic",
                                "arithmetic operators",
                                "comparison operators",
                                "logical operators",
                                "builtin functions",
                                "hello world")

c_syntax = LanguageSyntax("options",
                          "keywords",
                          "data types",
                          "operators",
                          "forloop",
                          "whileloop",
                          "case statements",
                          "class definition",
                          "variable definition",
                          "arrays",
                          "function definition",
                          "control flow",
                          "user input",
                          "output",
                          "arithmetic",
                          "arithmetic operators",
                          "comparison operators",
                          "logical operators",
                          "builtin functions",
                          "hello world")

cpp_syntax = LanguageSyntax("options",
                            "keywords",
                            "data types",
                            "operators",
                            "forloop",
                            "whileloop",
                            "case statements",
                            "class definition",
                            "variable definition",
                            "arrays",
                            "function definition",
                            "control flow",
                            "user input",
                            "output",
                            "arithmetic",
                            "arithmetic operators",
                            "comparison operators",
                            "logical operators",
                            "builtin functions",
                            "hello world")


skeleton_syntax = LanguageSyntax("options",
                            "keywords",
                            "data types",
                            "operators",
                            "forloop",
                            "whileloop",
                            "case statements",
                            "class definition",
                            "variable definition",
                            "arrays",
                            "function definition",
                            "control flow",
                            "user input",
                            "output",
                            "arithmetic",
                            "arithmetic operators",
                            "comparison operators",
                            "logical operators",
                            "builtin functions",
                            "hello world")


parser = argparse.ArgumentParser()

args = parser.add_argument("language", help="Specify programming language", type=str)
args = parser.add_argument("syntax", help="Syntactic structure sought", type=str)
args = parser.add_argument("-v", "--verbose", help="Verbose output flag", action="store_true")

args = parser.parse_args()

print(args.language)
print(args.syntax)


# language specific arg-trees - - trying to keep cyclomatic complexity low
# LISP arg-tree
print(dash_band)

# LISP

if "lisp" in args.language:
    if args.syntax == "classification":
        LISP_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        LISP_lang.output_historical_information()
    elif args.syntax == "options":
        LISP_syntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(LISP_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(LISP_syntax.data_types)
        if args.verbose:
            print("System-defined symbols for data types in LISP:\n"
                  "array\tfixnum\tpackage\tsimple-string\n"
                  "atom\tfloat\tpathname\tsimple-vector\n"
                  "bignum\tfunction\trandom-state\tsingle-float\n"
                  "bit-vector\tinteger\trational\tstream\n"
                  "character\tkeyword\treadtable\tstring\n"
                  "[common]\tlist\tsequence\t[string-char]\n"
                  "compiled-function\tlong-float\tshort-float\t symbol\n"
                  "complex\tnill\tsigned-byte\tt\n"
                  "cons\tnull\tsimple-array\tunsigned-byte\n"
                  "double-float\tnumber\tsimple-bit-vector\tvector\n")
    elif args.syntax == "operators":
        print(LISP_syntax.operators)
        if args.verbose:
            print("OPERATOR EXAMPLES:\n\n"
                  "Arithmetic:\n(+ 43 15)\t(/ 56 8)\t(mod 10 5)\n(incf var 2)\t(rem 10 5)\t(decf var 1)\n"
                  "comparison:\n(= A B)\t\t(/= A B)\t(> A B)\n(< A B)\t\t(>= A B)\t(<= A B)\n"
                  "logical:\n(or nil 1)\t(and 1 1)\t(not nil nil)")
    elif args.syntax == "forloop":
        print(LISP_syntax.for_loop)
        if args.verbose:
            print("Examples:\n(loop for x in '(one two three)\n\tdo (format t \" ~s\" x))\n\n"
                  "(loop for var from 10 to 10\n\tdo (print var))\n\n"
                  "(loop for x from 1 to 20\n\tif(evenpx)\n\tdo (print x))\n")
    elif args.syntax == "whileloop":
        print(LISP_syntax.while_loop)
        if args.verbose:
            print("")
    elif args.syntax == "casestatement" or "case" in args.syntax:
        print(LISP_syntax.case_statement)
        if args.verbose:
            print("EXAMPLE: \n(setq day 4)\n(case day\n(1 (format t \"~% Monday\"))\n(2 (format t \"~% Tuesday\"))\n"
                  "(3 (format t \"~% Wednesday\"))\n(4 (format t \"~% Thursday\"))\n(5 (format t \"~% Friday\"))\n"
                  "(6 (format t \"~% Saturday\"))\n(7 (format t \"~% Sunday\")))")
    elif args.syntax == "defineclass" or "class" in args.syntax:
        print(LISP_syntax.class_definition)
        if args.verbose:
            print("")
    elif args.syntax == "variable":
        print(LISP_syntax.variable_definition)
        if args.verbose:
            print("(setq x 10)\n(setq t 20)\n(format t \"x = ~2d ~%\" x y)\n\n"
                  "(setq x 100)\n(setq y 200)\n(format t \"x = ~2d y = ~2d\" x y)")
    elif args.syntax == "array":
        print(LISP_syntax.array)
        if args.verbose:
            print("")
    elif args.syntax == "function":
        print(LISP_syntax.function_definition)
        if args.verbose:
            print("")
    elif args.syntax == "controlflow":
        print(LISP_syntax.control_flow)
        if args.verbose:
            print("")
    elif args.syntax == "input":
        print(LISP_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "output":
        print(LISP_syntax.output)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic":
        print(LISP_syntax.arithmetic)
        if args.verbose:
            print("EXAMPLES:\naddition: (+ 43 72)\nsubtraction: (- 17 7)\n multiplication: (* 6 6)\nDivision: (/ 4 2)")
    elif args.syntax == "arithmetic operators" or ("arithmetic" and "operators") in args.syntax:  # works
        print(LISP_syntax.arithmetic_operators)
        if args.verbose:
            print("")
    elif args.syntax == "comparisonoperators" or ("comparison" and "operators") in args.syntax:
        print(LISP_syntax.comparison_operators)
        if args.verbose:
            print("")
    elif args.syntax == "logicaloperators" or ("logical" and "operators") in args.syntax:
        print(LISP_syntax.logical_operators)
        if args.verbosE:
            print("")
    elif args.syntax == "builtinfunctions":
        print(LISP_syntax.builtin_functions)
        if args.verbose:
            print("")
    elif args.syntax == "helloworld":
        print(LISP_syntax.hello_world)
        if args.verbose:
            print("")
    else:
        print("############################################")
        print("Error: syntactic query not found: try --help")
        print("############################################")

# BASH

elif "bash" in args.language:
    if args.syntax == "classification":
        skeleton_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        skeleton_lang.output_historical_information()
    elif args.syntax == "options":
        skeleton_syntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(skeleton_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(skeleton_syntax.data_types)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(skeleton_syntax.operators)
        if args.verbose:
            print("")
    elif args.syntax == "forloop":
        print(skeleton_syntax.for_loop)
        if args.verbose:
            print("")
    elif args.syntax == "whileloop":
        print(skeleton_syntax.while_loop)
        if args.verbose:
            print("")
    elif args.syntax == "casestatement" or "case" in args.syntax:
        print(skeleton_syntax.case_statement)
        if args.verbose:
            print("")
    elif args.syntax == "defineclass" or "class" in args.syntax:
        print(skeleton_syntax.class_definition)
        if args.verbose:
            print("")
    elif args.syntax == "definevariable" or "variable" in args.syntax:
        print(skeleton_syntax.variable_definition)
        if args.verbose:
            print("")
    elif args.syntax == "array":
        print(skeleton_syntax.array)
        if args.verbose:
            print("")
    elif args.syntax == "function":
        print(skeleton_syntax.function_definition)
        if args.verbose:
            print("")
    elif args.syntax == "controlflow":
        print(skeleton_syntax.control_flow)
        if args.verbose:
            print("")
    elif args.syntax == "input":
        print(skeleton_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "output":
        print(skeleton_syntax.output)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic":
        print(skeleton_syntax.arithmetic)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic operators" or ("arithmetic" and "operators") in args.syntax:  # works
        print(skeleton_syntax.arithmetic_operators)
        if args.verbose:
            print("")
    elif args.syntax == "comparisonoperators":
        print(skeleton_syntax.comparison_operators)
        if args.verbose:
            print("")
    elif args.syntax == "logicaloperators":
        print(skeleton_syntax.logical_operators)
        if args.verbose:
            print("")
    elif args.syntax == "builtinfunctions":
        print(skeleton_syntax.builtin_functions)
        if args.verbose:
            print("")
    elif args.syntax == "helloworld":
        print(skeleton_syntax.hello_world)
        if args.verbose:
            print("")

    else:
        print("############################################")
        print("Error: syntactic query not found: try --help")
        print("############################################")


# PYTHON3


elif "python" in args.language or "python3" in args.language:
    if args.syntax == "classification":
        skeleton_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        skeleton_lang.output_historical_information()
    elif args.syntax == "options":
        skeleton_syntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(skeleton_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(skeleton_syntax.data_types)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(skeleton_syntax.operators)
        if args.verbose:
            print("")
    elif args.syntax == "forloop":
        print(skeleton_syntax.for_loop)
        if args.verbose:
            print("")
    elif args.syntax == "whileloop":
        print(skeleton_syntax.while_loop)
        if args.verbose:
            print("")
    elif args.syntax == "casestatement" or "case" in args.syntax:
        print(skeleton_syntax.case_statement)
        if args.verbose:
            print("")
    elif args.syntax == "defineclass" or "class" in args.syntax:
        print(skeleton_syntax.class_definition)
        if args.verbose:
            print("")
    elif args.syntax == "definevariable" or "variable" in args.syntax:
        print(skeleton_syntax.variable_definition)
        if args.verbose:
            print("")
    elif args.syntax == "array":
        print(skeleton_syntax.array)
        if args.verbose:
            print("")
    elif args.syntax == "function":
        print(skeleton_syntax.function_definition)
        if args.verbose:
            print("")
    elif args.syntax == "controlflow":
        print(skeleton_syntax.control_flow)
        if args.verbose:
            print("")
    elif args.syntax == "input":
        print(skeleton_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "output":
        print(skeleton_syntax.output)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic":
        print(skeleton_syntax.arithmetic)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic operators" or ("arithmetic" and "operators") in args.syntax:  # works
        print(skeleton_syntax.arithmetic_operators)
        if args.verbose:
            print("")
    elif args.syntax == "comparisonoperators":
        print(skeleton_syntax.comparison_operators)
        if args.verbose:
            print("")
    elif args.syntax == "logicaloperators":
        print(skeleton_syntax.logical_operators)
        if args.verbose:
            print("")
    elif args.syntax == "builtinfunctions":
        print(skeleton_syntax.builtin_functions)
        if args.verbose:
            print("")
    elif args.syntax == "helloworld":
        print(skeleton_syntax.hello_world)
        if args.verbose:
            print("")

    else:
        print("############################################")
        print("Error: syntactic query not found: try --help")
        print("############################################")

# skelly 0

elif "skeleton" in args.language:
    if args.syntax == "classification":
        skeleton_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        skeleton_lang.output_historical_information()
    elif args.syntax == "options":
        skeleton_syntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(skeleton_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(skeleton_syntax.data_types)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(skeleton_syntax.operators)
        if args.verbose:
            print("")
    elif args.syntax == "forloop":
        print(skeleton_syntax.for_loop)
        if args.verbose:
            print("")
    elif args.syntax == "whileloop":
        print(skeleton_syntax.while_loop)
        if args.verbose:
            print("")
    elif args.syntax == "casestatement" or "case" in args.syntax:
        print(skeleton_syntax.case_statement)
        if args.verbose:
            print("")
    elif args.syntax == "defineclass" or "class" in args.syntax:
        print(skeleton_syntax.class_definition)
        if args.verbose:
            print("")
    elif args.syntax == "definevariable" or "variable" in args.syntax:
        print(skeleton_syntax.variable_definition)
        if args.verbose:
            print("")
    elif args.syntax == "array":
        print(skeleton_syntax.array)
        if args.verbose:
            print("")
    elif args.syntax == "function":
        print(skeleton_syntax.function_definition)
        if args.verbose:
            print("")
    elif args.syntax == "controlflow":
        print(skeleton_syntax.control_flow)
        if args.verbose:
            print("")
    elif args.syntax == "input":
        print(skeleton_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "output":
        print(skeleton_syntax.output)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic":
        print(skeleton_syntax.arithmetic)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic operators" or ("arithmetic" and "operators") in args.syntax:  # works
        print(skeleton_syntax.arithmetic_operators)
        if args.verbose:
            print("")
    elif args.syntax == "comparisonoperators":
        print(skeleton_syntax.comparison_operators)
        if args.verbose:
            print("")
    elif args.syntax == "logicaloperators":
        print(skeleton_syntax.logical_operators)
        if args.verbose:
            print("")
    elif args.syntax == "builtinfunctions":
        print(skeleton_syntax.builtin_functions)
        if args.verbose:
            print("")
    elif args.syntax == "helloworld":
        print(skeleton_syntax.hello_world)
        if args.verbose:
            print("")
    else:
        print("############################################")
        print("Error: syntactic query not found: try --help")
        print("############################################")

# skelly1

elif "skeleton" in args.language:
    if args.syntax == "classification":
        skeleton_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        skeleton_lang.output_historical_information()
    elif args.syntax == "options":
        skeleton_syntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(skeleton_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(skeleton_syntax.data_types)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(skeleton_syntax.operators)
        if args.verbose:
            print("")
    elif args.syntax == "forloop":
        print(skeleton_syntax.for_loop)
        if args.verbose:
            print("")
    elif args.syntax == "whileloop":
        print(skeleton_syntax.while_loop)
        if args.verbose:
            print("")
    elif args.syntax == "casestatement" or "case" in args.syntax:
        print(skeleton_syntax.case_statement)
        if args.verbose:
            print("")
    elif args.syntax == "defineclass" or "class" in args.syntax:
        print(skeleton_syntax.class_definition)
        if args.verbose:
            print("")
    elif args.syntax == "definevariable" or "variable" in args.syntax:
        print(skeleton_syntax.variable_definition)
        if args.verbose:
            print("")
    elif args.syntax == "array":
        print(skeleton_syntax.array)
        if args.verbose:
            print("")
    elif args.syntax == "function":
        print(skeleton_syntax.function_definition)
        if args.verbose:
            print("")
    elif args.syntax == "controlflow":
        print(skeleton_syntax.control_flow)
        if args.verbose:
            print("")
    elif args.syntax == "input":
        print(skeleton_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "output":
        print(skeleton_syntax.output)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic":
        print(skeleton_syntax.arithmetic)
        if args.verbose:
            print("")
    elif args.syntax == "arithmetic operators" or ("arithmetic" and "operators") in args.syntax:  # works
        print(skeleton_syntax.arithmetic_operators)
        if args.verbose:
            print("")
    elif args.syntax == "comparisonoperators":
        print(skeleton_syntax.comparison_operators)
        if args.verbose:
            print("")
    elif args.syntax == "logicaloperators":
        print(skeleton_syntax.logical_operators)
        if args.verbose:
            print("")
    elif args.syntax == "builtinfunctions":
        print(skeleton_syntax.builtin_functions)
        if args.verbose:
            print("")
    elif args.syntax == "helloworld":
        print(skeleton_syntax.hello_world)
        if args.verbose:
            print("")

    else:
        print("############################################")
        print("Error: syntactic query not found: try --help")
        print("############################################")

else:
    print("#########################################################################")
    print("Error: First argument - [Language] - not supported or else not recognized")
    print("#########################################################################")

print(dash_band)




