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
        print("This will print list of available syntax argument terms you can search")

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


# LanguageSyntax object class instantiations

LISP_syntax = LanguageSyntax("options",
                             "keywords",
                             "data types",
                             "Arithmetic Operators:\n+\t-\t*\t/\nmod|rem\tincf\tdecf\t\n"
                             "Comparison Operators:\n=\t/=\t>\t<\n>=\t<=\tmax\tmin\n"
                             "Logical Operators:\n(and A B)\t(or A B)\t(not A B)\t\n",
                             "forloop",
                             "whileloop",
                             "(case (keyform)\n"
                             "((key1)   (action1   action2 ...) )\n"
                             "((key2)   (action1   action2 ...) )\n"
                             "...\n"
                             "((keyn)   (action1   action2 ...) ))\n",
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
                                "break\t:\tbreak out of loop\n"
                                ""
                                + dash_band,
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
        LanguageSyntax.display_syntax_selection_options()
    elif args.syntax == "keywords":
        print(LISP_syntax.keywords)
        if args.verbose:
            print("")
    elif args.syntax == "datatypes":
        print(LISP_syntax.data_types)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(LISP_syntax.operators)
        if args.verbose:
            print("EXAMPLE:\n(+ 43 15)\t(/ 56 8)\t(mod 10 5)\n(incf var 2)\t(or 0 1)\t(and 1 1)")
    elif args.syntax == "forloop":
        print(LISP_syntax.forloop)
        if args.verbose:
            print("")
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
        print(LISP_syntax.define_class)
        if args.verbose:
            print("")
    elif args.syntax == "variable":
        print(LISP_syntax.variable_definition)
        if args.verbose:
            print("")
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
        print(skeleton_syntax.forloop)
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
        print(skeleton_syntax.define_class)
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


elif "python" in args.language:
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
        print(skeleton_syntax.forloop)
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
        print(skeleton_syntax.define_class)
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
        print(skeleton_syntax.forloop)
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
        print(skeleton_syntax.define_class)
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
        print(skeleton_syntax.forloop)
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
        print(skeleton_syntax.define_class)
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

