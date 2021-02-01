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
        print(self.name + " was created by " + self.creators + " first appearing in " + self.first_appeared +
              "Wikipedia writes: \n" + self.history)


class LanguageSyntax:
    def __init__(self, data_types, operators, for_loop, while_loop, case_statement, class_definition, define_variable,
                 array, function_definition, control_flow, user_input, output, arithmetic, hello_world):
        self.operators = operators
        self.data_types = data_types
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
        self.hello_world = hello_world

    def return_not_available(self, structure_in_question):
        print("Error: " + str(structure_in_question) + " is not available currently")

    def not_a_part_of_language(self, structure_in_question):
        print("Error: " + str(structure_in_question) + " is not a part of the language")


# ProgrammingLanguage object instantiations
LISP_lang = ProgrammingLanguage("Common LISP", "Multi-paradigm: functional, procedural, reflective, meta",
                    "Dynamic, strong", "John McCarthy", "1958",
                    "John McCarthy developed Lisp in 1958 while at the Massachusetts Institute of Technology (MIT)",
                    "https://en.wikipedia.org/wiki/Lisp_(programming_language)")

LISP_syntax = LanguageSyntax("")

# LanguageSyntax object class instatiations
# LISP_syntax = LanguageSyntax("all syntax data here")


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
    elif args.syntax == "datatypes":
        print(LISP_syntax.user_input)
        if args.verbose:
            print("")
    elif args.syntax == "operators":
        print(LISP_syntax.hello_world)
        if args.verbose:
            print("")
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
            print("")
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











