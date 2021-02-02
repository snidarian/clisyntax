#! /usr/local/bin/python3.9
# cli syntax - provides syntax information and history from the command line

import argparse


class ProgrammingLanguage:
    def __init__(self, name, paradigm, typing, creators, first_appeared, history, wiki_link):
        self.name = name  # both
        self.paradigm = paradigm  # technical
        self.typing = typing  # technical
        self.creators = creators  # historical
        self.first_appeared = first_appeared  # historical
        self.history = history  # historical
        self.wiki_link = wiki_link  # both

    def output_language_classifications(self):
        print(self.name + " is a " + self.paradigm + " language with " + self.typing + " typing discipline"
              "for more information, visit the language's wikipedia page: " + self.wiki_link)

    def output_historical_information(self):
        print(self.name + " was created by " + self.creators + " first appearing in " + self.first_appeared + ". "
              "\nWikipedia writes: " + self.history)


class LanguageSyntax:
    def __init__(self, options_list, data_types, operators, for_loop, while_loop, case_statement, class_definition,
                 define_variable, array, function_definition, control_flow, user_input, output, arithmetic,
                 arithmetic_operators, comparison_operators, logical_operators, builtin_functions, hello_world):
        self.options = options_list
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
                    "John McCarthy developed Lisp in 1958 while at the Massachusetts Institute of Technology (MIT)",
                    "https://en.wikipedia.org/wiki/Lisp_(programming_language)")

bash_lang = ProgrammingLanguage("", "", "", "", "", "", "")

python3_lang = ProgrammingLanguage("", "", "", "", "", "", "")

javascript_lang = ProgrammingLanguage("", "", "", "", "", "", "")

c_lang = ProgrammingLanguage("", "", "", "", "", "", "")

cpp_lang = ProgrammingLanguage("", "", "", "", "", "", "")

java_lang = ProgrammingLanguage("", "", "", "", "", "", "")

perl_lang = ProgrammingLanguage("", "", "", "", "", "", "")

ruby_lang = ProgrammingLanguage("", "", "", "", "", "", "")

next0_lang = ProgrammingLanguage("", "", "", "", "", "", "")

next1_lang = ProgrammingLanguage("", "", "", "", "", "", "")



# Variable definitions
dash_band = "-------------------------------------------------------\n"

# LanguageSyntax object class instantiations

LISP_syntax = LanguageSyntax("options", "data types",
                             dash_band +
                             "Arithmetic Operators:\n+\t-\t*\t/\nmod|rem\tincf\tdecf\t\n"
                             "Comparison Operators:\n=\t/=\t>\t<\n>=\t<=\tmax\tmin\n"
                             "Logical Operators:\n(and A B)\t(or A B)\t(not A B)\t\n"
                             + dash_band,
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

c_syntax = LanguageSyntax(      "options",
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
if "lisp" in args.language:
    if args.syntax == "classification":
        LISP_lang.output_language_classifications()
    elif args.syntax == "history" or args.syntax == "historical":
        LISP_lang.output_historical_information()
    elif args.syntax == "options":
        LanguageSyntax.display_syntax_selection_options()
    elif args.syntax == "datatypes":
        print(LISP_syntax.user_input)
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
                  "(3 (format t \"~% Wednesday\"))\n(4 (format t \"~% Thursday\"))\n(5 (format t \"~% Friday\"))"
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
        print("Error: syntactic query not found: try --help")

elif "python" in args.language:
    if args.syntax == "classification":
        print("Paradigm: Multi-paradigm:\n\tfunctional, imperative, object-oriented, structured, reflective")
        print("Designed by:\n\tGuido van Rossum")
        print("Typing Discipline:\n\tDuck, dynamic, strong typing")
    elif args.syntax == "forloop":
        print("for loopvar in list")
    elif args.syntax == "whileloop" or "while" in args.syntax:
        print("mark 4")
    else:
        print("Error: syntactic query not found: try --help")

elif "javascript" in args.language:
    print("mark 5")
else:
    print("Error: First argument - [Language] - not supported or else not recognized")




