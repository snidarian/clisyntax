#! /usr/local/bin/python3.9
# cli syntax

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
    def __init__(self, data_types, for_loop, while_loop, case_statement, define_class):
        self.data_types = data_types
        self.for_loop = for_loop
        self.while_loop = while_loop
        self.case_statement = case_statement

    def return_not_available(self):
        print("Error: Syntax item is not available currently")
    def not_a_part_of_language(self):
        print("Error: That syntax item is not a part of the lanaguage")


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
        print("Common LISP:\n\tParadigm: Multi-paradigm - \n\tprocedural, functional, object-oriented, meta, reflective, generic")
        print("Designed by:\n\tScott Fahlman, Richard P. Gabriel, David A. Moon, Kent Pitman, Guy Steele, Dan Weinreb")
        print("Typing discipline:\n\tDynamic, Strong")
    elif args.syntax == "forloop":
        print("(loop for [loopvar] in <list>\n\tdo (action)\n)")
        if args.verbose:
            print("For loop explanation in detail.. blah blah blah")
    elif args.syntax == "whileloop" or "while" in args.syntax:
        print("mark 2")
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











