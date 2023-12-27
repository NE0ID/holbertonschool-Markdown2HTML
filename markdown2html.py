#!/usr/bin/python3

""" 
    Markdown2HTML
"""
import sys


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise("Usage: ./markdown2html.py README.md README.html")
        exit (1)
    if exists(sys.argv[2]) == False:
        raise("Missing <filename>")
        exit (1)
    exit (0) 