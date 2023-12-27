#!/usr/bin/python3

""" 
    Markdown2HTML
"""
import sys
import os


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print ("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit (1)
    elif os.path.exists(sys.argv[1]) == False:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit (1)
    exit (0) 
