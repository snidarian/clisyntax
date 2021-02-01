



#! /usr/local/bin/python3.9
# cli syntax

import argparse

parser = argparse.ArgumentParser()

args = parser.add_argument("language", help="Specify programming language", type=str)
args = parser.add_argument("syntax", help="Syntactic structure sought", type=str)
args = parser.add_argument("-v", "--verbose", help="Verbose output flag", action="store_true")

args = parser.parse_args()

print(args.language)
print(args.syntax)


# language specific arg-trees - - trying to keep cyclomatic complexity low

# EXAMPLE LISP
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

# Language template
elif "lang" in args.language:
    if args.syntax == "classification":
        print("Paradigm: ...")
        print("Designed by: ...")
        print("Typing discipline: ...")
    elif args.syntax == "forloop":
        print("(loop for [loopvar] in <list>\n\tdo (action)\n)")
        if args.verbose:
            print("loop explanation")
    elif args.syntax == "whileloop" or "while" in args.syntax:
        print("mark 2")
    else:
        print("Error: syntactic query not found: try --help")

















