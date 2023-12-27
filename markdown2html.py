#!/usr/bin/python3

""" 
    Markdown2HTML
"""
import sys


if __name__ == "__main__":

    try:
        if len(sys.argv) != 3:
            raise InvalidNumberOfArgs
        elif exists(sys.argv[2]) == False:
            raise NonExistingFile
    except InvalidNumberOfArgs as e:
        print ("Usage: ./markdown2html.py README.md README.html")
        exit (1)
    except NonExistingFile as e:
        print("Missing {}".format(sys.argv[2]))
        exit (1)
    exit (0) 